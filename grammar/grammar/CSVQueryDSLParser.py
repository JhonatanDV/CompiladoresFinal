# Generated from grammar/CSVQueryDSL.g4 by ANTLR 4.13.1
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
        4,1,24,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,45,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,
        6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,
        4,1,0,8,13,1,0,6,7,1,0,14,17,1,0,18,20,60,0,23,1,0,0,0,2,32,1,0,
        0,0,4,34,1,0,0,0,6,38,1,0,0,0,8,48,1,0,0,0,10,54,1,0,0,0,12,57,1,
        0,0,0,14,59,1,0,0,0,16,61,1,0,0,0,18,63,1,0,0,0,20,22,3,2,1,0,21,
        20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,
        0,25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,33,3,4,2,0,29,33,3,
        6,3,0,30,33,3,8,4,0,31,33,3,10,5,0,32,28,1,0,0,0,32,29,1,0,0,0,32,
        30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,35,5,1,0,0,35,36,5,18,0,
        0,36,37,5,21,0,0,37,5,1,0,0,0,38,39,5,2,0,0,39,40,5,5,0,0,40,41,
        5,18,0,0,41,42,3,12,6,0,42,44,3,18,9,0,43,45,3,14,7,0,44,43,1,0,
        0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,5,21,0,0,47,7,1,0,0,0,48,49,
        5,3,0,0,49,50,3,16,8,0,50,51,5,5,0,0,51,52,5,18,0,0,52,53,5,21,0,
        0,53,9,1,0,0,0,54,55,5,4,0,0,55,56,5,21,0,0,56,11,1,0,0,0,57,58,
        7,0,0,0,58,13,1,0,0,0,59,60,7,1,0,0,60,15,1,0,0,0,61,62,7,2,0,0,
        62,17,1,0,0,0,63,64,7,3,0,0,64,19,1,0,0,0,3,23,32,44
    ]

class CSVQueryDSLParser ( Parser ):

    grammarFileName = "CSVQueryDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "'filter'", "'aggregate'", "'print'", 
                     "'column'", "'AND'", "'OR'", "'>='", "'<='", "'>'", 
                     "'<'", "'=='", "'!='", "'COUNT'", "'SUM'", "'AVERAGE'", 
                     "'BETWEEN'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "LOAD", "FILTER", "AGGREGATE", "PRINT", 
                      "COLUMN", "AND", "OR", "GTE", "LTE", "GT", "LT", "EQ", 
                      "NEQ", "COUNT", "SUM", "AVERAGE", "BETWEEN", "STRING", 
                      "NUMBER", "DATE", "SEMICOLON", "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_loadStatement = 2
    RULE_filterStatement = 3
    RULE_aggregateStatement = 4
    RULE_printStatement = 5
    RULE_operator = 6
    RULE_logicalOp = 7
    RULE_aggregateFunction = 8
    RULE_value = 9

    ruleNames =  [ "program", "statement", "loadStatement", "filterStatement", 
                   "aggregateStatement", "printStatement", "operator", "logicalOp", 
                   "aggregateFunction", "value" ]

    EOF = Token.EOF
    LOAD=1
    FILTER=2
    AGGREGATE=3
    PRINT=4
    COLUMN=5
    AND=6
    OR=7
    GTE=8
    LTE=9
    GT=10
    LT=11
    EQ=12
    NEQ=13
    COUNT=14
    SUM=15
    AVERAGE=16
    BETWEEN=17
    STRING=18
    NUMBER=19
    DATE=20
    SEMICOLON=21
    WS=22
    COMMENT=23
    BLOCK_COMMENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSVQueryDSLParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVQueryDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSVQueryDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_program

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

        localctx = CSVQueryDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(CSVQueryDSLParser.EOF)
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

        def loadStatement(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.LoadStatementContext,0)


        def filterStatement(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.FilterStatementContext,0)


        def aggregateStatement(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.AggregateStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.PrintStatementContext,0)


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_statement

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

        localctx = CSVQueryDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.loadStatement()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.filterStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.aggregateStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.printStatement()
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


    class LoadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(CSVQueryDSLParser.LOAD, 0)

        def STRING(self):
            return self.getToken(CSVQueryDSLParser.STRING, 0)

        def SEMICOLON(self):
            return self.getToken(CSVQueryDSLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_loadStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStatement" ):
                listener.enterLoadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStatement" ):
                listener.exitLoadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStatement" ):
                return visitor.visitLoadStatement(self)
            else:
                return visitor.visitChildren(self)




    def loadStatement(self):

        localctx = CSVQueryDSLParser.LoadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(CSVQueryDSLParser.LOAD)
            self.state = 35
            self.match(CSVQueryDSLParser.STRING)
            self.state = 36
            self.match(CSVQueryDSLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(CSVQueryDSLParser.FILTER, 0)

        def COLUMN(self):
            return self.getToken(CSVQueryDSLParser.COLUMN, 0)

        def STRING(self):
            return self.getToken(CSVQueryDSLParser.STRING, 0)

        def operator(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.ValueContext,0)


        def SEMICOLON(self):
            return self.getToken(CSVQueryDSLParser.SEMICOLON, 0)

        def logicalOp(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.LogicalOpContext,0)


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_filterStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStatement" ):
                listener.enterFilterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStatement" ):
                listener.exitFilterStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStatement" ):
                return visitor.visitFilterStatement(self)
            else:
                return visitor.visitChildren(self)




    def filterStatement(self):

        localctx = CSVQueryDSLParser.FilterStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(CSVQueryDSLParser.FILTER)
            self.state = 39
            self.match(CSVQueryDSLParser.COLUMN)
            self.state = 40
            self.match(CSVQueryDSLParser.STRING)
            self.state = 41
            self.operator()
            self.state = 42
            self.value()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 43
                self.logicalOp()


            self.state = 46
            self.match(CSVQueryDSLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGREGATE(self):
            return self.getToken(CSVQueryDSLParser.AGGREGATE, 0)

        def aggregateFunction(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.AggregateFunctionContext,0)


        def COLUMN(self):
            return self.getToken(CSVQueryDSLParser.COLUMN, 0)

        def STRING(self):
            return self.getToken(CSVQueryDSLParser.STRING, 0)

        def SEMICOLON(self):
            return self.getToken(CSVQueryDSLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_aggregateStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateStatement" ):
                listener.enterAggregateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateStatement" ):
                listener.exitAggregateStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateStatement" ):
                return visitor.visitAggregateStatement(self)
            else:
                return visitor.visitChildren(self)




    def aggregateStatement(self):

        localctx = CSVQueryDSLParser.AggregateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aggregateStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(CSVQueryDSLParser.AGGREGATE)
            self.state = 49
            self.aggregateFunction()
            self.state = 50
            self.match(CSVQueryDSLParser.COLUMN)
            self.state = 51
            self.match(CSVQueryDSLParser.STRING)
            self.state = 52
            self.match(CSVQueryDSLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(CSVQueryDSLParser.PRINT, 0)

        def SEMICOLON(self):
            return self.getToken(CSVQueryDSLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = CSVQueryDSLParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(CSVQueryDSLParser.PRINT)
            self.state = 55
            self.match(CSVQueryDSLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GTE(self):
            return self.getToken(CSVQueryDSLParser.GTE, 0)

        def LTE(self):
            return self.getToken(CSVQueryDSLParser.LTE, 0)

        def GT(self):
            return self.getToken(CSVQueryDSLParser.GT, 0)

        def LT(self):
            return self.getToken(CSVQueryDSLParser.LT, 0)

        def EQ(self):
            return self.getToken(CSVQueryDSLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(CSVQueryDSLParser.NEQ, 0)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = CSVQueryDSLParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
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


    class LogicalOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(CSVQueryDSLParser.AND, 0)

        def OR(self):
            return self.getToken(CSVQueryDSLParser.OR, 0)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_logicalOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOp" ):
                listener.enterLogicalOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOp" ):
                listener.exitLogicalOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOp" ):
                return visitor.visitLogicalOp(self)
            else:
                return visitor.visitChildren(self)




    def logicalOp(self):

        localctx = CSVQueryDSLParser.LogicalOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_logicalOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
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


    class AggregateFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COUNT(self):
            return self.getToken(CSVQueryDSLParser.COUNT, 0)

        def SUM(self):
            return self.getToken(CSVQueryDSLParser.SUM, 0)

        def AVERAGE(self):
            return self.getToken(CSVQueryDSLParser.AVERAGE, 0)

        def BETWEEN(self):
            return self.getToken(CSVQueryDSLParser.BETWEEN, 0)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_aggregateFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateFunction" ):
                listener.enterAggregateFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateFunction" ):
                listener.exitAggregateFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateFunction" ):
                return visitor.visitAggregateFunction(self)
            else:
                return visitor.visitChildren(self)




    def aggregateFunction(self):

        localctx = CSVQueryDSLParser.AggregateFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_aggregateFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVQueryDSLParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(CSVQueryDSLParser.NUMBER, 0)

        def DATE(self):
            return self.getToken(CSVQueryDSLParser.DATE, 0)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = CSVQueryDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
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





