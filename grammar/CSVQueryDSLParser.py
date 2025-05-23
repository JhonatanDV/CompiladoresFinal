# Generated from CSVQueryDSL.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

class CSVQueryDSLParser(Parser):

    grammarFileName = "CSVQueryDSL.g4"
    atn = None
    decisionsToDFA = []
    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "'filter'", "'aggregate'", 
                     "'print'", "'column'", "'AND'", "'OR'", "'>='", "'<='", 
                     "'>'", "'<'", "'=='", "'!='", "'COUNT'", "'SUM'", 
                     "'AVERAGE'", "'BETWEEN'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "LOAD", "FILTER", "AGGREGATE", "PRINT", 
                      "COLUMN", "AND", "OR", "GTE", "LTE", "GT", "LT", "EQ", 
                      "NEQ", "COUNT", "SUM", "AVERAGE", "BETWEEN", "STRING", 
                      "NUMBER", "DATE", "SEMICOLON", "WS", "COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_loadStatement = 2
    RULE_filterStatement = 3
    RULE_aggregateStatement = 4
    RULE_printStatement = 5
    RULE_operator = 6
    RULE_logicalOp = 7
    RULE_value = 8
    RULE_aggregateFunction = 9

    ruleNames =  [ "program", "statement", "loadStatement", "filterStatement", 
                   "aggregateStatement", "printStatement", "operator", 
                   "logicalOp", "value", "aggregateFunction" ]

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
        self.checkVersion("4.13.2")
        self._interp = None
        self._predicates = None

    class ProgramContext(ParserRuleContext):
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

    class StatementContext(ParserRuleContext):
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

    class LoadStatementContext(ParserRuleContext):
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

    class FilterStatementContext(ParserRuleContext):
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

    class AggregateStatementContext(ParserRuleContext):
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

    class PrintStatementContext(ParserRuleContext):
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

    class OperatorContext(ParserRuleContext):
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

    class LogicalOpContext(ParserRuleContext):
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

    class ValueContext(ParserRuleContext):
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

    class AggregateFunctionContext(ParserRuleContext):
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

    def program(self):
        return self.ProgramContext(self, self._ctx, self.state)

    def statement(self):
        return self.StatementContext(self, self._ctx, self.state)

    def loadStatement(self):
        return self.LoadStatementContext(self, self._ctx, self.state)

    def filterStatement(self):
        return self.FilterStatementContext(self, self._ctx, self.state)

    def aggregateStatement(self):
        return self.AggregateStatementContext(self, self._ctx, self.state)

    def printStatement(self):
        return self.PrintStatementContext(self, self._ctx, self.state)

    def operator(self):
        return self.OperatorContext(self, self._ctx, self.state)

    def logicalOp(self):
        return self.LogicalOpContext(self, self._ctx, self.state)

    def value(self):
        return self.ValueContext(self, self._ctx, self.state)

    def aggregateFunction(self):
        return self.AggregateFunctionContext(self, self._ctx, self.state)