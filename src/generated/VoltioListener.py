# Generated from grammar/Voltio.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .VoltioParser import VoltioParser
else:
    from VoltioParser import VoltioParser

# This class defines a complete listener for a parse tree produced by VoltioParser.
class VoltioListener(ParseTreeListener):

    # Enter a parse tree produced by VoltioParser#programa.
    def enterPrograma(self, ctx:VoltioParser.ProgramaContext):
        pass

    # Exit a parse tree produced by VoltioParser#programa.
    def exitPrograma(self, ctx:VoltioParser.ProgramaContext):
        pass


    # Enter a parse tree produced by VoltioParser#listaSentencias.
    def enterListaSentencias(self, ctx:VoltioParser.ListaSentenciasContext):
        pass

    # Exit a parse tree produced by VoltioParser#listaSentencias.
    def exitListaSentencias(self, ctx:VoltioParser.ListaSentenciasContext):
        pass


    # Enter a parse tree produced by VoltioParser#sentencia.
    def enterSentencia(self, ctx:VoltioParser.SentenciaContext):
        pass

    # Exit a parse tree produced by VoltioParser#sentencia.
    def exitSentencia(self, ctx:VoltioParser.SentenciaContext):
        pass


    # Enter a parse tree produced by VoltioParser#bloque.
    def enterBloque(self, ctx:VoltioParser.BloqueContext):
        pass

    # Exit a parse tree produced by VoltioParser#bloque.
    def exitBloque(self, ctx:VoltioParser.BloqueContext):
        pass


    # Enter a parse tree produced by VoltioParser#declaracion.
    def enterDeclaracion(self, ctx:VoltioParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by VoltioParser#declaracion.
    def exitDeclaracion(self, ctx:VoltioParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by VoltioParser#inicializacion.
    def enterInicializacion(self, ctx:VoltioParser.InicializacionContext):
        pass

    # Exit a parse tree produced by VoltioParser#inicializacion.
    def exitInicializacion(self, ctx:VoltioParser.InicializacionContext):
        pass


    # Enter a parse tree produced by VoltioParser#tipo.
    def enterTipo(self, ctx:VoltioParser.TipoContext):
        pass

    # Exit a parse tree produced by VoltioParser#tipo.
    def exitTipo(self, ctx:VoltioParser.TipoContext):
        pass


    # Enter a parse tree produced by VoltioParser#asignacion.
    def enterAsignacion(self, ctx:VoltioParser.AsignacionContext):
        pass

    # Exit a parse tree produced by VoltioParser#asignacion.
    def exitAsignacion(self, ctx:VoltioParser.AsignacionContext):
        pass


    # Enter a parse tree produced by VoltioParser#opAsignacion.
    def enterOpAsignacion(self, ctx:VoltioParser.OpAsignacionContext):
        pass

    # Exit a parse tree produced by VoltioParser#opAsignacion.
    def exitOpAsignacion(self, ctx:VoltioParser.OpAsignacionContext):
        pass


    # Enter a parse tree produced by VoltioParser#expresion.
    def enterExpresion(self, ctx:VoltioParser.ExpresionContext):
        pass

    # Exit a parse tree produced by VoltioParser#expresion.
    def exitExpresion(self, ctx:VoltioParser.ExpresionContext):
        pass


    # Enter a parse tree produced by VoltioParser#conjuncion.
    def enterConjuncion(self, ctx:VoltioParser.ConjuncionContext):
        pass

    # Exit a parse tree produced by VoltioParser#conjuncion.
    def exitConjuncion(self, ctx:VoltioParser.ConjuncionContext):
        pass


    # Enter a parse tree produced by VoltioParser#negacion.
    def enterNegacion(self, ctx:VoltioParser.NegacionContext):
        pass

    # Exit a parse tree produced by VoltioParser#negacion.
    def exitNegacion(self, ctx:VoltioParser.NegacionContext):
        pass


    # Enter a parse tree produced by VoltioParser#igualdad.
    def enterIgualdad(self, ctx:VoltioParser.IgualdadContext):
        pass

    # Exit a parse tree produced by VoltioParser#igualdad.
    def exitIgualdad(self, ctx:VoltioParser.IgualdadContext):
        pass


    # Enter a parse tree produced by VoltioParser#relacional.
    def enterRelacional(self, ctx:VoltioParser.RelacionalContext):
        pass

    # Exit a parse tree produced by VoltioParser#relacional.
    def exitRelacional(self, ctx:VoltioParser.RelacionalContext):
        pass


    # Enter a parse tree produced by VoltioParser#aritmetica.
    def enterAritmetica(self, ctx:VoltioParser.AritmeticaContext):
        pass

    # Exit a parse tree produced by VoltioParser#aritmetica.
    def exitAritmetica(self, ctx:VoltioParser.AritmeticaContext):
        pass


    # Enter a parse tree produced by VoltioParser#termino.
    def enterTermino(self, ctx:VoltioParser.TerminoContext):
        pass

    # Exit a parse tree produced by VoltioParser#termino.
    def exitTermino(self, ctx:VoltioParser.TerminoContext):
        pass


    # Enter a parse tree produced by VoltioParser#unario.
    def enterUnario(self, ctx:VoltioParser.UnarioContext):
        pass

    # Exit a parse tree produced by VoltioParser#unario.
    def exitUnario(self, ctx:VoltioParser.UnarioContext):
        pass


    # Enter a parse tree produced by VoltioParser#primario.
    def enterPrimario(self, ctx:VoltioParser.PrimarioContext):
        pass

    # Exit a parse tree produced by VoltioParser#primario.
    def exitPrimario(self, ctx:VoltioParser.PrimarioContext):
        pass


    # Enter a parse tree produced by VoltioParser#literal.
    def enterLiteral(self, ctx:VoltioParser.LiteralContext):
        pass

    # Exit a parse tree produced by VoltioParser#literal.
    def exitLiteral(self, ctx:VoltioParser.LiteralContext):
        pass


    # Enter a parse tree produced by VoltioParser#numero.
    def enterNumero(self, ctx:VoltioParser.NumeroContext):
        pass

    # Exit a parse tree produced by VoltioParser#numero.
    def exitNumero(self, ctx:VoltioParser.NumeroContext):
        pass


    # Enter a parse tree produced by VoltioParser#llamada.
    def enterLlamada(self, ctx:VoltioParser.LlamadaContext):
        pass

    # Exit a parse tree produced by VoltioParser#llamada.
    def exitLlamada(self, ctx:VoltioParser.LlamadaContext):
        pass


    # Enter a parse tree produced by VoltioParser#argumentos.
    def enterArgumentos(self, ctx:VoltioParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by VoltioParser#argumentos.
    def exitArgumentos(self, ctx:VoltioParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by VoltioParser#argumentosCola.
    def enterArgumentosCola(self, ctx:VoltioParser.ArgumentosColaContext):
        pass

    # Exit a parse tree produced by VoltioParser#argumentosCola.
    def exitArgumentosCola(self, ctx:VoltioParser.ArgumentosColaContext):
        pass


    # Enter a parse tree produced by VoltioParser#seleccion.
    def enterSeleccion(self, ctx:VoltioParser.SeleccionContext):
        pass

    # Exit a parse tree produced by VoltioParser#seleccion.
    def exitSeleccion(self, ctx:VoltioParser.SeleccionContext):
        pass


    # Enter a parse tree produced by VoltioParser#parteSino.
    def enterParteSino(self, ctx:VoltioParser.ParteSinoContext):
        pass

    # Exit a parse tree produced by VoltioParser#parteSino.
    def exitParteSino(self, ctx:VoltioParser.ParteSinoContext):
        pass


    # Enter a parse tree produced by VoltioParser#colaSino.
    def enterColaSino(self, ctx:VoltioParser.ColaSinoContext):
        pass

    # Exit a parse tree produced by VoltioParser#colaSino.
    def exitColaSino(self, ctx:VoltioParser.ColaSinoContext):
        pass


    # Enter a parse tree produced by VoltioParser#iteracion.
    def enterIteracion(self, ctx:VoltioParser.IteracionContext):
        pass

    # Exit a parse tree produced by VoltioParser#iteracion.
    def exitIteracion(self, ctx:VoltioParser.IteracionContext):
        pass


    # Enter a parse tree produced by VoltioParser#pasoOpcional.
    def enterPasoOpcional(self, ctx:VoltioParser.PasoOpcionalContext):
        pass

    # Exit a parse tree produced by VoltioParser#pasoOpcional.
    def exitPasoOpcional(self, ctx:VoltioParser.PasoOpcionalContext):
        pass


    # Enter a parse tree produced by VoltioParser#regla.
    def enterRegla(self, ctx:VoltioParser.ReglaContext):
        pass

    # Exit a parse tree produced by VoltioParser#regla.
    def exitRegla(self, ctx:VoltioParser.ReglaContext):
        pass


    # Enter a parse tree produced by VoltioParser#parametros.
    def enterParametros(self, ctx:VoltioParser.ParametrosContext):
        pass

    # Exit a parse tree produced by VoltioParser#parametros.
    def exitParametros(self, ctx:VoltioParser.ParametrosContext):
        pass


    # Enter a parse tree produced by VoltioParser#parametrosCola.
    def enterParametrosCola(self, ctx:VoltioParser.ParametrosColaContext):
        pass

    # Exit a parse tree produced by VoltioParser#parametrosCola.
    def exitParametrosCola(self, ctx:VoltioParser.ParametrosColaContext):
        pass


    # Enter a parse tree produced by VoltioParser#parametro.
    def enterParametro(self, ctx:VoltioParser.ParametroContext):
        pass

    # Exit a parse tree produced by VoltioParser#parametro.
    def exitParametro(self, ctx:VoltioParser.ParametroContext):
        pass


    # Enter a parse tree produced by VoltioParser#tipoRetorno.
    def enterTipoRetorno(self, ctx:VoltioParser.TipoRetornoContext):
        pass

    # Exit a parse tree produced by VoltioParser#tipoRetorno.
    def exitTipoRetorno(self, ctx:VoltioParser.TipoRetornoContext):
        pass


    # Enter a parse tree produced by VoltioParser#retorno.
    def enterRetorno(self, ctx:VoltioParser.RetornoContext):
        pass

    # Exit a parse tree produced by VoltioParser#retorno.
    def exitRetorno(self, ctx:VoltioParser.RetornoContext):
        pass


    # Enter a parse tree produced by VoltioParser#valorRetorno.
    def enterValorRetorno(self, ctx:VoltioParser.ValorRetornoContext):
        pass

    # Exit a parse tree produced by VoltioParser#valorRetorno.
    def exitValorRetorno(self, ctx:VoltioParser.ValorRetornoContext):
        pass


    # Enter a parse tree produced by VoltioParser#llamadaSentencia.
    def enterLlamadaSentencia(self, ctx:VoltioParser.LlamadaSentenciaContext):
        pass

    # Exit a parse tree produced by VoltioParser#llamadaSentencia.
    def exitLlamadaSentencia(self, ctx:VoltioParser.LlamadaSentenciaContext):
        pass


    # Enter a parse tree produced by VoltioParser#entradaSalida.
    def enterEntradaSalida(self, ctx:VoltioParser.EntradaSalidaContext):
        pass

    # Exit a parse tree produced by VoltioParser#entradaSalida.
    def exitEntradaSalida(self, ctx:VoltioParser.EntradaSalidaContext):
        pass



del VoltioParser