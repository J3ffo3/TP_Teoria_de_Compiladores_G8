# Generated from grammar/Voltio.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .VoltioParser import VoltioParser
else:
    from VoltioParser import VoltioParser

# This class defines a complete generic visitor for a parse tree produced by VoltioParser.

class VoltioVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VoltioParser#programa.
    def visitPrograma(self, ctx:VoltioParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#listaSentencias.
    def visitListaSentencias(self, ctx:VoltioParser.ListaSentenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#sentencia.
    def visitSentencia(self, ctx:VoltioParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#bloque.
    def visitBloque(self, ctx:VoltioParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#declaracion.
    def visitDeclaracion(self, ctx:VoltioParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#inicializacion.
    def visitInicializacion(self, ctx:VoltioParser.InicializacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#tipo.
    def visitTipo(self, ctx:VoltioParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#asignacion.
    def visitAsignacion(self, ctx:VoltioParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#opAsignacion.
    def visitOpAsignacion(self, ctx:VoltioParser.OpAsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#expresion.
    def visitExpresion(self, ctx:VoltioParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#conjuncion.
    def visitConjuncion(self, ctx:VoltioParser.ConjuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#negacion.
    def visitNegacion(self, ctx:VoltioParser.NegacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#igualdad.
    def visitIgualdad(self, ctx:VoltioParser.IgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#relacional.
    def visitRelacional(self, ctx:VoltioParser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#aritmetica.
    def visitAritmetica(self, ctx:VoltioParser.AritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#termino.
    def visitTermino(self, ctx:VoltioParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#unario.
    def visitUnario(self, ctx:VoltioParser.UnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#primario.
    def visitPrimario(self, ctx:VoltioParser.PrimarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#literal.
    def visitLiteral(self, ctx:VoltioParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#numero.
    def visitNumero(self, ctx:VoltioParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#llamada.
    def visitLlamada(self, ctx:VoltioParser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#argumentos.
    def visitArgumentos(self, ctx:VoltioParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#argumentosCola.
    def visitArgumentosCola(self, ctx:VoltioParser.ArgumentosColaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#seleccion.
    def visitSeleccion(self, ctx:VoltioParser.SeleccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#parteSino.
    def visitParteSino(self, ctx:VoltioParser.ParteSinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#colaSino.
    def visitColaSino(self, ctx:VoltioParser.ColaSinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#iteracion.
    def visitIteracion(self, ctx:VoltioParser.IteracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#pasoOpcional.
    def visitPasoOpcional(self, ctx:VoltioParser.PasoOpcionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#regla.
    def visitRegla(self, ctx:VoltioParser.ReglaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#parametros.
    def visitParametros(self, ctx:VoltioParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#parametrosCola.
    def visitParametrosCola(self, ctx:VoltioParser.ParametrosColaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#parametro.
    def visitParametro(self, ctx:VoltioParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#tipoRetorno.
    def visitTipoRetorno(self, ctx:VoltioParser.TipoRetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#retorno.
    def visitRetorno(self, ctx:VoltioParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#valorRetorno.
    def visitValorRetorno(self, ctx:VoltioParser.ValorRetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#llamadaSentencia.
    def visitLlamadaSentencia(self, ctx:VoltioParser.LlamadaSentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VoltioParser#entradaSalida.
    def visitEntradaSalida(self, ctx:VoltioParser.EntradaSalidaContext):
        return self.visitChildren(ctx)



del VoltioParser