# Generated from C:/Users/jeffo/Downloads/Teoria de Compiladores/TP1/MarkovLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MarkovLangParser import MarkovLangParser
else:
    from MarkovLangParser import MarkovLangParser

# This class defines a complete listener for a parse tree produced by MarkovLangParser.
class MarkovLangListener(ParseTreeListener):

    # Enter a parse tree produced by MarkovLangParser#program.
    def enterProgram(self, ctx:MarkovLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#program.
    def exitProgram(self, ctx:MarkovLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#globalConfig.
    def enterGlobalConfig(self, ctx:MarkovLangParser.GlobalConfigContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#globalConfig.
    def exitGlobalConfig(self, ctx:MarkovLangParser.GlobalConfigContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#seedStmt.
    def enterSeedStmt(self, ctx:MarkovLangParser.SeedStmtContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#seedStmt.
    def exitSeedStmt(self, ctx:MarkovLangParser.SeedStmtContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#statement.
    def enterStatement(self, ctx:MarkovLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#statement.
    def exitStatement(self, ctx:MarkovLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#varDecl.
    def enterVarDecl(self, ctx:MarkovLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#varDecl.
    def exitVarDecl(self, ctx:MarkovLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#typeSpec.
    def enterTypeSpec(self, ctx:MarkovLangParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#typeSpec.
    def exitTypeSpec(self, ctx:MarkovLangParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#assignment.
    def enterAssignment(self, ctx:MarkovLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#assignment.
    def exitAssignment(self, ctx:MarkovLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#ifStmt.
    def enterIfStmt(self, ctx:MarkovLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#ifStmt.
    def exitIfStmt(self, ctx:MarkovLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#whileStmt.
    def enterWhileStmt(self, ctx:MarkovLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#whileStmt.
    def exitWhileStmt(self, ctx:MarkovLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#printStmt.
    def enterPrintStmt(self, ctx:MarkovLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#printStmt.
    def exitPrintStmt(self, ctx:MarkovLangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#block.
    def enterBlock(self, ctx:MarkovLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#block.
    def exitBlock(self, ctx:MarkovLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#chainDecl.
    def enterChainDecl(self, ctx:MarkovLangParser.ChainDeclContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#chainDecl.
    def exitChainDecl(self, ctx:MarkovLangParser.ChainDeclContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#chainBody.
    def enterChainBody(self, ctx:MarkovLangParser.ChainBodyContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#chainBody.
    def exitChainBody(self, ctx:MarkovLangParser.ChainBodyContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#stateDecl.
    def enterStateDecl(self, ctx:MarkovLangParser.StateDeclContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#stateDecl.
    def exitStateDecl(self, ctx:MarkovLangParser.StateDeclContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#transitionStmt.
    def enterTransitionStmt(self, ctx:MarkovLangParser.TransitionStmtContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#transitionStmt.
    def exitTransitionStmt(self, ctx:MarkovLangParser.TransitionStmtContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#simulateStmt.
    def enterSimulateStmt(self, ctx:MarkovLangParser.SimulateStmtContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#simulateStmt.
    def exitSimulateStmt(self, ctx:MarkovLangParser.SimulateStmtContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#stationaryStmt.
    def enterStationaryStmt(self, ctx:MarkovLangParser.StationaryStmtContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#stationaryStmt.
    def exitStationaryStmt(self, ctx:MarkovLangParser.StationaryStmtContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#expression.
    def enterExpression(self, ctx:MarkovLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#expression.
    def exitExpression(self, ctx:MarkovLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#relationalExpr.
    def enterRelationalExpr(self, ctx:MarkovLangParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#relationalExpr.
    def exitRelationalExpr(self, ctx:MarkovLangParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:MarkovLangParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:MarkovLangParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:MarkovLangParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:MarkovLangParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by MarkovLangParser#factor.
    def enterFactor(self, ctx:MarkovLangParser.FactorContext):
        pass

    # Exit a parse tree produced by MarkovLangParser#factor.
    def exitFactor(self, ctx:MarkovLangParser.FactorContext):
        pass



del MarkovLangParser