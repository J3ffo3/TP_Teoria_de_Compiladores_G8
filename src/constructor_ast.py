from __future__ import annotations
from decimal import Decimal
from antlr4.tree.Tree import TerminalNode

import ast_voltio as A
from generated.VoltioLexer import VoltioLexer as L
from generated.VoltioParser import VoltioParser as P
from generated.VoltioVisitor import VoltioVisitor

OPERADORES = {
    L.O: "o", L.Y: "y", L.IGUAL: "==", L.DIFERENTE: "!=", L.MENOR: "<", L.MENOR_IGUAL: "<=",
    L.MAYOR: ">", L.MAYOR_IGUAL: ">=", L.SUMA: "+", L.RESTA: "-", L.MULT: "*", L.DIV: "/",
    L.MOD: "mod", L.ASIG: "=", L.MAS_ASIG: "+=", L.MENOS_ASIG: "-=",
}

def _pos(nodo) -> dict:
    tok = nodo.getSymbol() if isinstance(nodo, TerminalNode) else nodo.start
    return {"linea": tok.line, "columna": tok.column + 1}

def _terminal(ctx, i: int) -> int:
    hijo = ctx.getChild(i)
    return hijo.getSymbol().type if isinstance(hijo, TerminalNode) else -1

class ConstructorAST(VoltioVisitor):
    def visitPrograma(self, ctx: P.ProgramaContext):
        return A.Programa(self._lista_sentencias(ctx.listaSentencias()), linea=1, columna=1)

    def _lista_sentencias(self, ctx) -> list:
        salida = []
        while ctx is not None and ctx.sentencia() is not None:
            salida.append(self.visit(ctx.sentencia()))
            ctx = ctx.listaSentencias()
        return salida

    def visitSentencia(self, ctx: P.SentenciaContext):
        return self.visit(ctx.getChild(0))

    def visitBloque(self, ctx: P.BloqueContext):
        return A.Bloque(self._lista_sentencias(ctx.listaSentencias()), **_pos(ctx))

    def visitDeclaracion(self, ctx: P.DeclaracionContext):
        constante = ctx.CONST() is not None
        if constante:
            valor = self.visit(ctx.expresion())
        else:
            ini = ctx.inicializacion()
            valor = self.visit(ini.expresion()) if ini.expresion() is not None else None
        return A.Declaracion(constante, ctx.ID().getText(), self.visit(ctx.tipo()), valor, **_pos(ctx.ID()))

    def visitTipo(self, ctx: P.TipoContext):
        txt = ctx.getText()
        if "<" in txt and ">" in txt:
            base = txt.split("<")[0]
            unidad = txt.split("<")[1].replace(">", "")
            return A.Tipo(base, unidad)
        return A.Tipo(txt)

    def visitAsignacion(self, ctx: P.AsignacionContext):
        op = OPERADORES[ctx.opAsignacion().getChild(0).getSymbol().type]
        return A.Asignacion(ctx.ID().getText(), op, self.visit(ctx.expresion()), **_pos(ctx.ID()))

    def _binaria_o_paso(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        izq = self.visit(ctx.getChild(0))
        der = self.visit(ctx.getChild(2))
        op = OPERADORES[_terminal(ctx, 1)]
        return A.Binaria(op, izq, der, linea=izq.linea, columna=izq.columna)

    visitExpresion = _binaria_o_paso
    visitConjuncion = _binaria_o_paso
    visitIgualdad = _binaria_o_paso
    visitRelacional = _binaria_o_paso
    visitAritmetica = _binaria_o_paso
    visitTermino = _binaria_o_paso

    def visitNegacion(self, ctx: P.NegacionContext):
        if ctx.NO() is not None:
            return A.Unaria("no", self.visit(ctx.negacion()), **_pos(ctx))
        return self.visit(ctx.igualdad())

    def visitUnario(self, ctx: P.UnarioContext):
        if ctx.RESTA() is not None:
            return A.Unaria("-", self.visit(ctx.unario()), **_pos(ctx))
        return self.visit(ctx.primario())

    def visitPrimario(self, ctx: P.PrimarioContext):
        if ctx.PAR_IZQ() is not None:
            return self.visit(ctx.expresion())
        if ctx.llamada() is not None:
            return self.visit(ctx.llamada())
        if ctx.literal() is not None:
            return self.visit(ctx.literal())
        return A.Variable(ctx.ID().getText(), **_pos(ctx))

    def visitLiteral(self, ctx: P.LiteralContext):
        pos = _pos(ctx)
        # Literales con unidades de dominio
        for fn, unidad in [
            (ctx.UNIDAD_VOLTAJE, "V"), (ctx.UNIDAD_CORRIENTE, "A"),
            (ctx.UNIDAD_POTENCIA, ctx.UNIDAD_POTENCIA().getText() if ctx.UNIDAD_POTENCIA() else "W"),
            (ctx.UNIDAD_RESISTENCIA, "OHM"), (ctx.UNIDAD_ENERGIA, "KWH"),
            (ctx.UNIDAD_TIEMPO, ctx.UNIDAD_TIEMPO().getText() if ctx.UNIDAD_TIEMPO() else "H")
        ]:
            if fn is not None and fn():
                num_txt = ctx.numero().getText()
                val = Decimal(num_txt) if "." in num_txt else int(num_txt)
                return A.Literal("dominio", val, unidad, **pos)

        tok = ctx.getChild(0).getSymbol()
        texto = tok.text
        if tok.type == L.NUM_ENTERO:
            return A.Literal("entero", int(texto), **pos)
        if tok.type == L.NUM_DECIMAL:
            return A.Literal("decimal", Decimal(texto), **pos)
        if tok.type == L.LIT_PORCENTAJE:
            return A.Literal("porcentaje", Decimal(texto[:-1]), **pos)
        if tok.type == L.CADENA:
            return A.Literal("texto", texto[1:-1], **pos)
        return A.Literal("booleano", tok.type == L.VERDADERO, **pos)

    def visitLlamada(self, ctx: P.LlamadaContext):
        args = []
        a = ctx.argumentos()
        if a.expresion() is not None:
            args.append(self.visit(a.expresion()))
            args.extend(self._cola_argumentos(a.argumentosCola()))
        return A.Llamada(ctx.ID().getText(), args, **_pos(ctx.ID()))

    def _cola_argumentos(self, ctx) -> list:
        salida = []
        while ctx is not None and ctx.expresion() is not None:
            salida.append(self.visit(ctx.expresion()))
            ctx = ctx.argumentosCola()
        return salida

    def visitSeleccion(self, ctx: P.SeleccionContext):
        ramas = [(self.visit(ctx.expresion()), self.visit(ctx.bloque()))]
        sino = None
        parte = ctx.parteSino()
        while parte is not None and parte.SINO() is not None:
            cola = parte.colaSino()
            if cola.seleccion() is not None:
                sel = cola.seleccion()
                ramas.append((self.visit(sel.expresion()), self.visit(sel.bloque())))
                parte = sel.parteSino()
            else:
                sino = self.visit(cola.bloque())
                parte = None
        return A.Si(ramas, sino, **_pos(ctx))

    def visitIteracion(self, ctx: P.IteracionContext):
        if ctx.MIENTRAS() is not None:
            return A.Mientras(self.visit(ctx.expresion(0)), self.visit(ctx.bloque()), **_pos(ctx))
        paso_ctx = ctx.pasoOpcional()
        paso = self.visit(paso_ctx.expresion()) if paso_ctx.expresion() is not None else None
        return A.Para(ctx.ID().getText(), self.visit(ctx.expresion(0)), self.visit(ctx.expresion(1)),
                      paso, self.visit(ctx.bloque()), **_pos(ctx))

    def visitRegla(self, ctx: P.ReglaContext):
        params = []
        p = ctx.parametros()
        if p.parametro() is not None:
            params.append(self._parametro(p.parametro()))
            cola = p.parametrosCola()
            while cola is not None and cola.parametro() is not None:
                params.append(self._parametro(cola.parametro()))
                cola = cola.parametrosCola()
        tr = ctx.tipoRetorno()
        tipo_ret = self.visit(tr.tipo()) if tr.tipo() is not None else None
        return A.Regla(ctx.ID().getText(), params, tipo_ret, self.visit(ctx.bloque()), **_pos(ctx.ID()))

    def _parametro(self, ctx: P.ParametroContext) -> A.Parametro:
        return A.Parametro(ctx.ID().getText(), self.visit(ctx.tipo()), **_pos(ctx.ID()))

    def visitRetorno(self, ctx: P.RetornoContext):
        v = ctx.valorRetorno()
        return A.Retornar(self.visit(v.expresion()) if v.expresion() is not None else None, **_pos(ctx))

    def visitLlamadaSentencia(self, ctx: P.LlamadaSentenciaContext):
        llamada = self.visit(ctx.llamada())
        return A.LlamadaSentencia(llamada, linea=llamada.linea, columna=llamada.columna)

    def visitEntradaSalida(self, ctx: P.EntradaSalidaContext):
        if ctx.MOSTRAR() is not None:
            args = [self.visit(ctx.expresion())] + self._cola_argumentos(ctx.argumentosCola())
            return A.Mostrar(args, **_pos(ctx))
        return A.Leer(ctx.ID().getText(), **_pos(ctx.ID()))
