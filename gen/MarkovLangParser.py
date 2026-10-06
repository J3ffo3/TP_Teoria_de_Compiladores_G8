# Generated from C:/Users/jeffo/Downloads/Teoria de Compiladores/TP1/MarkovLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,215,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,5,0,52,8,0,10,
        0,12,0,55,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,74,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        3,7,101,8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,
        5,10,116,8,10,10,10,12,10,119,9,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,5,11,128,8,11,10,11,12,11,131,9,11,1,11,1,11,1,12,1,12,3,12,
        137,8,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,
        5,18,176,8,18,10,18,12,18,179,9,18,1,19,1,19,1,19,1,19,1,19,1,19,
        5,19,187,8,19,10,19,12,19,190,9,19,1,20,1,20,1,20,1,20,1,20,1,20,
        5,20,198,8,20,10,20,12,20,201,9,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,3,21,213,8,21,1,21,0,3,36,38,40,22,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,1,1,0,14,18,
        215,0,47,1,0,0,0,2,58,1,0,0,0,4,60,1,0,0,0,6,73,1,0,0,0,8,75,1,0,
        0,0,10,81,1,0,0,0,12,83,1,0,0,0,14,100,1,0,0,0,16,102,1,0,0,0,18,
        107,1,0,0,0,20,113,1,0,0,0,22,122,1,0,0,0,24,136,1,0,0,0,26,138,
        1,0,0,0,28,142,1,0,0,0,30,151,1,0,0,0,32,161,1,0,0,0,34,167,1,0,
        0,0,36,169,1,0,0,0,38,180,1,0,0,0,40,191,1,0,0,0,42,212,1,0,0,0,
        44,46,3,2,1,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,
        0,0,0,48,53,1,0,0,0,49,47,1,0,0,0,50,52,3,6,3,0,51,50,1,0,0,0,52,
        55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,
        0,56,57,5,0,0,1,57,1,1,0,0,0,58,59,3,4,2,0,59,3,1,0,0,0,60,61,5,
        2,0,0,61,62,5,34,0,0,62,63,5,27,0,0,63,5,1,0,0,0,64,74,3,8,4,0,65,
        74,3,12,6,0,66,74,3,14,7,0,67,74,3,16,8,0,68,74,3,18,9,0,69,74,3,
        22,11,0,70,74,3,30,15,0,71,74,3,32,16,0,72,74,3,20,10,0,73,64,1,
        0,0,0,73,65,1,0,0,0,73,66,1,0,0,0,73,67,1,0,0,0,73,68,1,0,0,0,73,
        69,1,0,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,7,1,0,0,
        0,75,76,5,1,0,0,76,77,5,36,0,0,77,78,5,26,0,0,78,79,3,10,5,0,79,
        80,5,27,0,0,80,9,1,0,0,0,81,82,7,0,0,0,82,11,1,0,0,0,83,84,5,36,
        0,0,84,85,5,24,0,0,85,86,3,34,17,0,86,87,5,27,0,0,87,13,1,0,0,0,
        88,89,5,8,0,0,89,90,3,34,17,0,90,91,5,9,0,0,91,92,3,20,10,0,92,101,
        1,0,0,0,93,94,5,8,0,0,94,95,3,34,17,0,95,96,5,9,0,0,96,97,3,20,10,
        0,97,98,5,10,0,0,98,99,3,20,10,0,99,101,1,0,0,0,100,88,1,0,0,0,100,
        93,1,0,0,0,101,15,1,0,0,0,102,103,5,11,0,0,103,104,3,34,17,0,104,
        105,5,12,0,0,105,106,3,20,10,0,106,17,1,0,0,0,107,108,5,13,0,0,108,
        109,5,29,0,0,109,110,3,34,17,0,110,111,5,30,0,0,111,112,5,27,0,0,
        112,19,1,0,0,0,113,117,5,31,0,0,114,116,3,6,3,0,115,114,1,0,0,0,
        116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,120,1,0,0,0,
        119,117,1,0,0,0,120,121,5,32,0,0,121,21,1,0,0,0,122,123,5,3,0,0,
        123,124,5,36,0,0,124,125,5,12,0,0,125,129,5,31,0,0,126,128,3,24,
        12,0,127,126,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,
        0,0,130,132,1,0,0,0,131,129,1,0,0,0,132,133,5,32,0,0,133,23,1,0,
        0,0,134,137,3,26,13,0,135,137,3,28,14,0,136,134,1,0,0,0,136,135,
        1,0,0,0,137,25,1,0,0,0,138,139,5,4,0,0,139,140,5,36,0,0,140,141,
        5,27,0,0,141,27,1,0,0,0,142,143,5,5,0,0,143,144,5,36,0,0,144,145,
        5,25,0,0,145,146,5,36,0,0,146,147,5,29,0,0,147,148,3,34,17,0,148,
        149,5,30,0,0,149,150,5,27,0,0,150,29,1,0,0,0,151,152,5,6,0,0,152,
        153,5,29,0,0,153,154,5,36,0,0,154,155,5,28,0,0,155,156,5,36,0,0,
        156,157,5,28,0,0,157,158,3,34,17,0,158,159,5,30,0,0,159,160,5,27,
        0,0,160,31,1,0,0,0,161,162,5,7,0,0,162,163,5,29,0,0,163,164,5,36,
        0,0,164,165,5,30,0,0,165,166,5,27,0,0,166,33,1,0,0,0,167,168,3,36,
        18,0,168,35,1,0,0,0,169,170,6,18,-1,0,170,171,3,38,19,0,171,177,
        1,0,0,0,172,173,10,2,0,0,173,174,5,21,0,0,174,176,3,38,19,0,175,
        172,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,
        37,1,0,0,0,179,177,1,0,0,0,180,181,6,19,-1,0,181,182,3,40,20,0,182,
        188,1,0,0,0,183,184,10,2,0,0,184,185,5,22,0,0,185,187,3,40,20,0,
        186,183,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,
        189,39,1,0,0,0,190,188,1,0,0,0,191,192,6,20,-1,0,192,193,3,42,21,
        0,193,199,1,0,0,0,194,195,10,2,0,0,195,196,5,23,0,0,196,198,3,42,
        21,0,197,194,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,
        0,0,200,41,1,0,0,0,201,199,1,0,0,0,202,213,5,34,0,0,203,213,5,33,
        0,0,204,213,5,35,0,0,205,213,5,19,0,0,206,213,5,20,0,0,207,213,5,
        36,0,0,208,209,5,29,0,0,209,210,3,34,17,0,210,211,5,30,0,0,211,213,
        1,0,0,0,212,202,1,0,0,0,212,203,1,0,0,0,212,204,1,0,0,0,212,205,
        1,0,0,0,212,206,1,0,0,0,212,207,1,0,0,0,212,208,1,0,0,0,213,43,1,
        0,0,0,11,47,53,73,100,117,129,136,177,188,199,212
    ]

class MarkovLangParser ( Parser ):

    grammarFileName = "MarkovLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'seed'", "'chain'", "<INVALID>", 
                     "'transition'", "'simulate'", "'stationary'", "'if'", 
                     "'then'", "'else'", "'while'", "'do'", "'print'", "'int'", 
                     "'float'", "'bool'", "'string'", "<INVALID>", "'true'", 
                     "'false'", "<INVALID>", "<INVALID>", "<INVALID>", "':='", 
                     "'->'", "':'", "';'", "','", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "VAR", "SEED", "CHAIN", "STATE", "TRANSITION", 
                      "SIMULATE", "STATIONARY", "IF", "THEN", "ELSE", "WHILE", 
                      "DO", "PRINT", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
                      "STRING_TYPE", "STATE_TYPE", "TRUE", "FALSE", "RELOP", 
                      "ADDOP", "MULOP", "ASSIGN", "ARROW", "COLON", "SEMI", 
                      "COMMA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "FLOAT_LIT", 
                      "INT_LIT", "STRING_LIT", "ID", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_globalConfig = 1
    RULE_seedStmt = 2
    RULE_statement = 3
    RULE_varDecl = 4
    RULE_typeSpec = 5
    RULE_assignment = 6
    RULE_ifStmt = 7
    RULE_whileStmt = 8
    RULE_printStmt = 9
    RULE_block = 10
    RULE_chainDecl = 11
    RULE_chainBody = 12
    RULE_stateDecl = 13
    RULE_transitionStmt = 14
    RULE_simulateStmt = 15
    RULE_stationaryStmt = 16
    RULE_expression = 17
    RULE_relationalExpr = 18
    RULE_additiveExpr = 19
    RULE_multiplicativeExpr = 20
    RULE_factor = 21

    ruleNames =  [ "program", "globalConfig", "seedStmt", "statement", "varDecl", 
                   "typeSpec", "assignment", "ifStmt", "whileStmt", "printStmt", 
                   "block", "chainDecl", "chainBody", "stateDecl", "transitionStmt", 
                   "simulateStmt", "stationaryStmt", "expression", "relationalExpr", 
                   "additiveExpr", "multiplicativeExpr", "factor" ]

    EOF = Token.EOF
    VAR=1
    SEED=2
    CHAIN=3
    STATE=4
    TRANSITION=5
    SIMULATE=6
    STATIONARY=7
    IF=8
    THEN=9
    ELSE=10
    WHILE=11
    DO=12
    PRINT=13
    INT_TYPE=14
    FLOAT_TYPE=15
    BOOL_TYPE=16
    STRING_TYPE=17
    STATE_TYPE=18
    TRUE=19
    FALSE=20
    RELOP=21
    ADDOP=22
    MULOP=23
    ASSIGN=24
    ARROW=25
    COLON=26
    SEMI=27
    COMMA=28
    LPAREN=29
    RPAREN=30
    LBRACE=31
    RBRACE=32
    FLOAT_LIT=33
    INT_LIT=34
    STRING_LIT=35
    ID=36
    WS=37
    LINE_COMMENT=38
    BLOCK_COMMENT=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MarkovLangParser.EOF, 0)

        def globalConfig(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkovLangParser.GlobalConfigContext)
            else:
                return self.getTypedRuleContext(MarkovLangParser.GlobalConfigContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkovLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MarkovLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MarkovLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MarkovLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 44
                self.globalConfig()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70866971082) != 0):
                self.state = 50
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(MarkovLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalConfigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seedStmt(self):
            return self.getTypedRuleContext(MarkovLangParser.SeedStmtContext,0)


        def getRuleIndex(self):
            return MarkovLangParser.RULE_globalConfig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalConfig" ):
                listener.enterGlobalConfig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalConfig" ):
                listener.exitGlobalConfig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalConfig" ):
                return visitor.visitGlobalConfig(self)
            else:
                return visitor.visitChildren(self)




    def globalConfig(self):

        localctx = MarkovLangParser.GlobalConfigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_globalConfig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.seedStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeedStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEED(self):
            return self.getToken(MarkovLangParser.SEED, 0)

        def INT_LIT(self):
            return self.getToken(MarkovLangParser.INT_LIT, 0)

        def SEMI(self):
            return self.getToken(MarkovLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_seedStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeedStmt" ):
                listener.enterSeedStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeedStmt" ):
                listener.exitSeedStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeedStmt" ):
                return visitor.visitSeedStmt(self)
            else:
                return visitor.visitChildren(self)




    def seedStmt(self):

        localctx = MarkovLangParser.SeedStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_seedStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(MarkovLangParser.SEED)
            self.state = 61
            self.match(MarkovLangParser.INT_LIT)
            self.state = 62
            self.match(MarkovLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MarkovLangParser.VarDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MarkovLangParser.AssignmentContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MarkovLangParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MarkovLangParser.WhileStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(MarkovLangParser.PrintStmtContext,0)


        def chainDecl(self):
            return self.getTypedRuleContext(MarkovLangParser.ChainDeclContext,0)


        def simulateStmt(self):
            return self.getTypedRuleContext(MarkovLangParser.SimulateStmtContext,0)


        def stationaryStmt(self):
            return self.getTypedRuleContext(MarkovLangParser.StationaryStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(MarkovLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MarkovLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MarkovLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.varDecl()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.assignment()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.ifStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.whileStmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.printStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.chainDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 70
                self.simulateStmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.stationaryStmt()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 9)
                self.state = 72
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MarkovLangParser.VAR, 0)

        def ID(self):
            return self.getToken(MarkovLangParser.ID, 0)

        def COLON(self):
            return self.getToken(MarkovLangParser.COLON, 0)

        def typeSpec(self):
            return self.getTypedRuleContext(MarkovLangParser.TypeSpecContext,0)


        def SEMI(self):
            return self.getToken(MarkovLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = MarkovLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(MarkovLangParser.VAR)
            self.state = 76
            self.match(MarkovLangParser.ID)
            self.state = 77
            self.match(MarkovLangParser.COLON)
            self.state = 78
            self.typeSpec()
            self.state = 79
            self.match(MarkovLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(MarkovLangParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(MarkovLangParser.FLOAT_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(MarkovLangParser.BOOL_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(MarkovLangParser.STRING_TYPE, 0)

        def STATE_TYPE(self):
            return self.getToken(MarkovLangParser.STATE_TYPE, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_typeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpec" ):
                listener.enterTypeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpec" ):
                listener.exitTypeSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpec" ):
                return visitor.visitTypeSpec(self)
            else:
                return visitor.visitChildren(self)




    def typeSpec(self):

        localctx = MarkovLangParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 507904) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MarkovLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MarkovLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MarkovLangParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MarkovLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MarkovLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(MarkovLangParser.ID)
            self.state = 84
            self.match(MarkovLangParser.ASSIGN)
            self.state = 85
            self.expression()
            self.state = 86
            self.match(MarkovLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MarkovLangParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(MarkovLangParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(MarkovLangParser.THEN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkovLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(MarkovLangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MarkovLangParser.ELSE, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MarkovLangParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStmt)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(MarkovLangParser.IF)
                self.state = 89
                self.expression()
                self.state = 90
                self.match(MarkovLangParser.THEN)
                self.state = 91
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(MarkovLangParser.IF)
                self.state = 94
                self.expression()
                self.state = 95
                self.match(MarkovLangParser.THEN)
                self.state = 96
                self.block()
                self.state = 97
                self.match(MarkovLangParser.ELSE)
                self.state = 98
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MarkovLangParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(MarkovLangParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(MarkovLangParser.DO, 0)

        def block(self):
            return self.getTypedRuleContext(MarkovLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MarkovLangParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = MarkovLangParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MarkovLangParser.WHILE)
            self.state = 103
            self.expression()
            self.state = 104
            self.match(MarkovLangParser.DO)
            self.state = 105
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MarkovLangParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(MarkovLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MarkovLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MarkovLangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MarkovLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = MarkovLangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(MarkovLangParser.PRINT)
            self.state = 108
            self.match(MarkovLangParser.LPAREN)
            self.state = 109
            self.expression()
            self.state = 110
            self.match(MarkovLangParser.RPAREN)
            self.state = 111
            self.match(MarkovLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MarkovLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MarkovLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkovLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MarkovLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MarkovLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MarkovLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(MarkovLangParser.LBRACE)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70866971082) != 0):
                self.state = 114
                self.statement()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(MarkovLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChainDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAIN(self):
            return self.getToken(MarkovLangParser.CHAIN, 0)

        def ID(self):
            return self.getToken(MarkovLangParser.ID, 0)

        def DO(self):
            return self.getToken(MarkovLangParser.DO, 0)

        def LBRACE(self):
            return self.getToken(MarkovLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MarkovLangParser.RBRACE, 0)

        def chainBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkovLangParser.ChainBodyContext)
            else:
                return self.getTypedRuleContext(MarkovLangParser.ChainBodyContext,i)


        def getRuleIndex(self):
            return MarkovLangParser.RULE_chainDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChainDecl" ):
                listener.enterChainDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChainDecl" ):
                listener.exitChainDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChainDecl" ):
                return visitor.visitChainDecl(self)
            else:
                return visitor.visitChildren(self)




    def chainDecl(self):

        localctx = MarkovLangParser.ChainDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_chainDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(MarkovLangParser.CHAIN)
            self.state = 123
            self.match(MarkovLangParser.ID)
            self.state = 124
            self.match(MarkovLangParser.DO)
            self.state = 125
            self.match(MarkovLangParser.LBRACE)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 126
                self.chainBody()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.match(MarkovLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChainBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stateDecl(self):
            return self.getTypedRuleContext(MarkovLangParser.StateDeclContext,0)


        def transitionStmt(self):
            return self.getTypedRuleContext(MarkovLangParser.TransitionStmtContext,0)


        def getRuleIndex(self):
            return MarkovLangParser.RULE_chainBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChainBody" ):
                listener.enterChainBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChainBody" ):
                listener.exitChainBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChainBody" ):
                return visitor.visitChainBody(self)
            else:
                return visitor.visitChildren(self)




    def chainBody(self):

        localctx = MarkovLangParser.ChainBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_chainBody)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.stateDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.transitionStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATE(self):
            return self.getToken(MarkovLangParser.STATE, 0)

        def ID(self):
            return self.getToken(MarkovLangParser.ID, 0)

        def SEMI(self):
            return self.getToken(MarkovLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_stateDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateDecl" ):
                listener.enterStateDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateDecl" ):
                listener.exitStateDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateDecl" ):
                return visitor.visitStateDecl(self)
            else:
                return visitor.visitChildren(self)




    def stateDecl(self):

        localctx = MarkovLangParser.StateDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stateDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(MarkovLangParser.STATE)
            self.state = 139
            self.match(MarkovLangParser.ID)
            self.state = 140
            self.match(MarkovLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransitionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRANSITION(self):
            return self.getToken(MarkovLangParser.TRANSITION, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MarkovLangParser.ID)
            else:
                return self.getToken(MarkovLangParser.ID, i)

        def ARROW(self):
            return self.getToken(MarkovLangParser.ARROW, 0)

        def LPAREN(self):
            return self.getToken(MarkovLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MarkovLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MarkovLangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MarkovLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_transitionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransitionStmt" ):
                listener.enterTransitionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransitionStmt" ):
                listener.exitTransitionStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransitionStmt" ):
                return visitor.visitTransitionStmt(self)
            else:
                return visitor.visitChildren(self)




    def transitionStmt(self):

        localctx = MarkovLangParser.TransitionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_transitionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(MarkovLangParser.TRANSITION)
            self.state = 143
            self.match(MarkovLangParser.ID)
            self.state = 144
            self.match(MarkovLangParser.ARROW)
            self.state = 145
            self.match(MarkovLangParser.ID)
            self.state = 146
            self.match(MarkovLangParser.LPAREN)
            self.state = 147
            self.expression()
            self.state = 148
            self.match(MarkovLangParser.RPAREN)
            self.state = 149
            self.match(MarkovLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimulateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIMULATE(self):
            return self.getToken(MarkovLangParser.SIMULATE, 0)

        def LPAREN(self):
            return self.getToken(MarkovLangParser.LPAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MarkovLangParser.ID)
            else:
                return self.getToken(MarkovLangParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MarkovLangParser.COMMA)
            else:
                return self.getToken(MarkovLangParser.COMMA, i)

        def expression(self):
            return self.getTypedRuleContext(MarkovLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MarkovLangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MarkovLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_simulateStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimulateStmt" ):
                listener.enterSimulateStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimulateStmt" ):
                listener.exitSimulateStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimulateStmt" ):
                return visitor.visitSimulateStmt(self)
            else:
                return visitor.visitChildren(self)




    def simulateStmt(self):

        localctx = MarkovLangParser.SimulateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_simulateStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MarkovLangParser.SIMULATE)
            self.state = 152
            self.match(MarkovLangParser.LPAREN)
            self.state = 153
            self.match(MarkovLangParser.ID)
            self.state = 154
            self.match(MarkovLangParser.COMMA)
            self.state = 155
            self.match(MarkovLangParser.ID)
            self.state = 156
            self.match(MarkovLangParser.COMMA)
            self.state = 157
            self.expression()
            self.state = 158
            self.match(MarkovLangParser.RPAREN)
            self.state = 159
            self.match(MarkovLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StationaryStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIONARY(self):
            return self.getToken(MarkovLangParser.STATIONARY, 0)

        def LPAREN(self):
            return self.getToken(MarkovLangParser.LPAREN, 0)

        def ID(self):
            return self.getToken(MarkovLangParser.ID, 0)

        def RPAREN(self):
            return self.getToken(MarkovLangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MarkovLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_stationaryStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStationaryStmt" ):
                listener.enterStationaryStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStationaryStmt" ):
                listener.exitStationaryStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStationaryStmt" ):
                return visitor.visitStationaryStmt(self)
            else:
                return visitor.visitChildren(self)




    def stationaryStmt(self):

        localctx = MarkovLangParser.StationaryStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stationaryStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MarkovLangParser.STATIONARY)
            self.state = 162
            self.match(MarkovLangParser.LPAREN)
            self.state = 163
            self.match(MarkovLangParser.ID)
            self.state = 164
            self.match(MarkovLangParser.RPAREN)
            self.state = 165
            self.match(MarkovLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self):
            return self.getTypedRuleContext(MarkovLangParser.RelationalExprContext,0)


        def getRuleIndex(self):
            return MarkovLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MarkovLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.relationalExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self):
            return self.getTypedRuleContext(MarkovLangParser.AdditiveExprContext,0)


        def relationalExpr(self):
            return self.getTypedRuleContext(MarkovLangParser.RelationalExprContext,0)


        def RELOP(self):
            return self.getToken(MarkovLangParser.RELOP, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_relationalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)



    def relationalExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MarkovLangParser.RelationalExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_relationalExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.additiveExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MarkovLangParser.RelationalExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpr)
                    self.state = 172
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 173
                    self.match(MarkovLangParser.RELOP)
                    self.state = 174
                    self.additiveExpr(0) 
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self):
            return self.getTypedRuleContext(MarkovLangParser.MultiplicativeExprContext,0)


        def additiveExpr(self):
            return self.getTypedRuleContext(MarkovLangParser.AdditiveExprContext,0)


        def ADDOP(self):
            return self.getToken(MarkovLangParser.ADDOP, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)



    def additiveExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MarkovLangParser.AdditiveExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_additiveExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.multiplicativeExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MarkovLangParser.AdditiveExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpr)
                    self.state = 183
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 184
                    self.match(MarkovLangParser.ADDOP)
                    self.state = 185
                    self.multiplicativeExpr(0) 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(MarkovLangParser.FactorContext,0)


        def multiplicativeExpr(self):
            return self.getTypedRuleContext(MarkovLangParser.MultiplicativeExprContext,0)


        def MULOP(self):
            return self.getToken(MarkovLangParser.MULOP, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)



    def multiplicativeExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MarkovLangParser.MultiplicativeExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_multiplicativeExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MarkovLangParser.MultiplicativeExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpr)
                    self.state = 194
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 195
                    self.match(MarkovLangParser.MULOP)
                    self.state = 196
                    self.factor() 
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MarkovLangParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MarkovLangParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MarkovLangParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MarkovLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MarkovLangParser.FALSE, 0)

        def ID(self):
            return self.getToken(MarkovLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MarkovLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MarkovLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MarkovLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return MarkovLangParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MarkovLangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factor)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(MarkovLangParser.INT_LIT)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(MarkovLangParser.FLOAT_LIT)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.match(MarkovLangParser.STRING_LIT)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.match(MarkovLangParser.TRUE)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 206
                self.match(MarkovLangParser.FALSE)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.match(MarkovLangParser.ID)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 7)
                self.state = 208
                self.match(MarkovLangParser.LPAREN)
                self.state = 209
                self.expression()
                self.state = 210
                self.match(MarkovLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.relationalExpr_sempred
        self._predicates[19] = self.additiveExpr_sempred
        self._predicates[20] = self.multiplicativeExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def relationalExpr_sempred(self, localctx:RelationalExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def additiveExpr_sempred(self, localctx:AdditiveExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplicativeExpr_sempred(self, localctx:MultiplicativeExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




