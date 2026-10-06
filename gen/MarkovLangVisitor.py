# Generated from C:/Users/jeffo/Downloads/Teoria de Compiladores/TP1/MarkovLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MarkovLangParser import MarkovLangParser
else:
    from MarkovLangParser import MarkovLangParser

# This class defines a complete generic visitor for a parse tree produced by MarkovLangParser.

class MarkovLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MarkovLangParser#program.
    def visitProgram(self, ctx:MarkovLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#globalConfig.
    def visitGlobalConfig(self, ctx:MarkovLangParser.GlobalConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#seedStmt.
    def visitSeedStmt(self, ctx:MarkovLangParser.SeedStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#statement.
    def visitStatement(self, ctx:MarkovLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#varDecl.
    def visitVarDecl(self, ctx:MarkovLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#typeSpec.
    def visitTypeSpec(self, ctx:MarkovLangParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#assignment.
    def visitAssignment(self, ctx:MarkovLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#ifStmt.
    def visitIfStmt(self, ctx:MarkovLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#whileStmt.
    def visitWhileStmt(self, ctx:MarkovLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#printStmt.
    def visitPrintStmt(self, ctx:MarkovLangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#block.
    def visitBlock(self, ctx:MarkovLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#chainDecl.
    def visitChainDecl(self, ctx:MarkovLangParser.ChainDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#chainBody.
    def visitChainBody(self, ctx:MarkovLangParser.ChainBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#stateDecl.
    def visitStateDecl(self, ctx:MarkovLangParser.StateDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#transitionStmt.
    def visitTransitionStmt(self, ctx:MarkovLangParser.TransitionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#simulateStmt.
    def visitSimulateStmt(self, ctx:MarkovLangParser.SimulateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#stationaryStmt.
    def visitStationaryStmt(self, ctx:MarkovLangParser.StationaryStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#expression.
    def visitExpression(self, ctx:MarkovLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#relationalExpr.
    def visitRelationalExpr(self, ctx:MarkovLangParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:MarkovLangParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MarkovLangParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkovLangParser#factor.
    def visitFactor(self, ctx:MarkovLangParser.FactorContext):
        return self.visitChildren(ctx)



del MarkovLangParser