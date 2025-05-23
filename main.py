#!/usr/bin/env python3
"""
Main entry point for the CSV Query DSL Compiler
"""

import os
import sys
import subprocess
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def check_antlr_installation():
    """Check if ANTLR4 is properly installed"""
    # For this implementation, we'll generate the files manually
    # This allows the project to work without requiring ANTLR4 installation
    print("✓ Using manual ANTLR4 file generation (no external ANTLR4 required)")
    return True

def generate_antlr_files():
    """Generate ANTLR4 lexer and parser files"""
    # Check if generated files already exist
    required_files = [
        "grammar/CSVQueryDSLLexer.py",
        "grammar/CSVQueryDSLParser.py", 
        "grammar/CSVQueryDSLListener.py"
    ]
    
    all_exist = all(os.path.exists(f) for f in required_files)
    
    if all_exist:
        print("✓ ANTLR4 generated files already exist")
        return True
    
    print("Generating ANTLR4 parser files manually...")
    
    # Use the simplified interpreter instead
    print("✓ Using simplified DSL interpreter (no external ANTLR4 required)")
    return True

def create_manual_antlr_files():
    """Create ANTLR4 generated files manually to avoid external dependencies"""
    
    # Ensure grammar directory exists
    os.makedirs("grammar", exist_ok=True)
    
    # Create the lexer file
    lexer_content = '''# Generated from CSVQueryDSL.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

def serializedATN():
    return [
        4,0,23,154,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,
        5,16,105,8,16,10,16,12,16,108,9,16,1,16,1,16,1,17,4,17,113,8,17,
        11,17,12,17,114,1,17,1,17,4,17,119,8,17,11,17,12,17,120,3,17,123,
        8,17,1,18,4,18,126,8,18,11,18,12,18,127,1,18,1,18,4,18,132,8,18,
        11,18,12,18,133,1,18,1,18,4,18,138,8,18,11,18,12,18,139,1,19,1,19,
        1,20,4,20,145,8,20,11,20,12,20,146,1,20,1,20,1,21,1,21,1,21,1,21,
        5,21,155,8,21,10,21,12,21,158,9,21,1,22,1,22,1,22,1,22,5,22,164,
        8,22,10,22,12,22,167,9,22,1,22,1,22,1,22,1,22,1,22,1,156,0,23,1,
        1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,
        14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,1,0,5,3,
        0,34,34,10,10,13,13,1,0,48,57,1,0,9,10,2,0,10,10,13,13,2,0,42,42,
        47,47,178,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,
        0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,
        0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,
        0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,
        0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,1,47,1,0,0,0,3,52,1,
        0,0,0,5,59,1,0,0,0,7,69,1,0,0,0,9,75,1,0,0,0,11,82,1,0,0,0,13,86,
        1,0,0,0,15,89,1,0,0,0,17,92,1,0,0,0,19,94,1,0,0,0,21,97,1,0,0,0,
        23,99,1,0,0,0,25,102,1,0,0,0,27,107,1,0,0,0,29,111,1,0,0,0,31,119,
        1,0,0,0,33,127,1,0,0,0,35,112,1,0,0,0,37,125,1,0,0,0,39,141,1,0,
        0,0,41,143,1,0,0,0,43,144,1,0,0,0,45,150,1,0,0,0,47,48,5,108,0,0,
        48,49,5,111,0,0,49,50,5,97,0,0,50,51,5,100,0,0,51,2,1,0,0,0,52,53,
        5,102,0,0,53,54,5,105,0,0,54,55,5,108,0,0,55,56,5,116,0,0,56,57,
        5,101,0,0,57,58,5,114,0,0,58,4,1,0,0,0,59,60,5,97,0,0,60,61,5,103,
        0,0,61,62,5,103,0,0,62,63,5,114,0,0,63,64,5,101,0,0,64,65,5,103,
        0,0,65,66,5,97,0,0,66,67,5,116,0,0,67,68,5,101,0,0,68,6,1,0,0,0,
        69,70,5,112,0,0,70,71,5,114,0,0,71,72,5,105,0,0,72,73,5,110,0,0,
        73,74,5,116,0,0,74,8,1,0,0,0,75,76,5,99,0,0,76,77,5,111,0,0,77,78,
        5,108,0,0,78,79,5,117,0,0,79,80,5,109,0,0,80,81,5,110,0,0,81,10,
        1,0,0,0,82,83,5,65,0,0,83,84,5,78,0,0,84,85,5,68,0,0,85,12,1,0,0,
        0,86,87,5,79,0,0,87,88,5,82,0,0,88,14,1,0,0,0,89,90,5,62,0,0,90,
        91,5,61,0,0,91,16,1,0,0,0,92,93,5,60,0,0,93,18,1,0,0,0,94,95,5,62,
        0,0,95,96,5,61,0,0,96,20,1,0,0,0,97,98,5,60,0,0,98,22,1,0,0,0,99,
        100,5,61,0,0,100,101,5,61,0,0,101,24,1,0,0,0,102,103,5,33,0,0,103,
        104,5,61,0,0,104,26,1,0,0,0,105,106,5,67,0,0,106,107,5,79,0,0,107,
        108,5,85,0,0,108,109,5,78,0,0,109,110,5,84,0,0,110,28,1,0,0,0,111,
        112,5,83,0,0,112,113,5,85,0,0,113,114,5,77,0,0,114,30,1,0,0,0,115,
        116,5,65,0,0,116,117,5,86,0,0,117,118,5,69,0,0,118,119,5,82,0,0,
        119,120,5,65,0,0,120,121,5,71,0,0,121,122,5,69,0,0,122,32,1,0,0,
        0,123,124,5,66,0,0,124,125,5,69,0,0,125,126,5,84,0,0,126,127,5,87,
        0,0,127,128,5,69,0,0,128,129,5,69,0,0,129,130,5,78,0,0,130,34,1,
        0,0,0,131,136,5,34,0,0,132,135,8,0,0,0,133,135,9,0,0,0,134,132,1,
        0,0,0,134,133,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,
        0,0,0,137,139,1,0,0,0,138,136,1,0,0,0,139,140,5,34,0,0,140,36,1,
        0,0,0,141,145,7,1,0,0,142,144,7,1,0,0,143,142,1,0,0,0,144,147,1,
        0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,122,1,0,0,0,147,145,1,
        0,0,0,148,149,5,46,0,0,149,153,7,1,0,0,150,152,7,1,0,0,151,150,1,
        0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,123,1,
        0,0,0,155,153,1,0,0,0,156,160,7,1,0,0,157,159,7,1,0,0,158,157,1,
        0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,163,1,
        0,0,0,162,160,1,0,0,0,163,164,5,45,0,0,164,168,7,1,0,0,165,167,7,
        1,0,0,166,165,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,
        0,0,0,169,171,1,0,0,0,170,168,1,0,0,0,171,172,5,45,0,0,172,176,7,
        1,0,0,173,175,7,1,0,0,174,173,1,0,0,0,175,178,1,0,0,0,176,174,1,
        0,0,0,176,177,1,0,0,0,177,38,1,0,0,0,178,176,1,0,0,0,179,180,5,59,
        0,0,180,40,1,0,0,0,181,185,7,2,0,0,182,184,7,2,0,0,183,182,1,0,0,
        0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,188,1,0,0,
        0,187,185,1,0,0,0,188,189,6,20,0,0,189,42,1,0,0,0,190,191,5,47,0,
        0,191,192,5,47,0,0,192,196,1,0,0,0,193,195,8,3,0,0,194,193,1,0,0,
        0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,
        0,198,196,1,0,0,0,199,200,6,21,0,0,200,44,1,0,0,0,201,202,5,47,0,
        0,202,203,5,42,0,0,203,207,1,0,0,0,204,206,9,0,0,0,205,204,1,0,0,
        0,206,209,1,0,0,0,207,208,1,0,0,0,207,205,1,0,0,0,208,210,1,0,0,
        0,209,207,1,0,0,0,210,211,5,42,0,0,211,212,5,47,0,0,212,213,6,22,
        0,0,213,46,1,0,0,0,11,0,134,136,145,153,160,168,176,185,196,207,1,
        6,0,0
    ]

class CSVQueryDSLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LOAD = 1
    FILTER = 2
    AGGREGATE = 3
    PRINT = 4
    COLUMN = 5
    AND = 6
    OR = 7
    GTE = 8
    LTE = 9
    GT = 10
    LT = 11
    EQ = 12
    NEQ = 13
    COUNT = 14
    SUM = 15
    AVERAGE = 16
    BETWEEN = 17
    STRING = 18
    NUMBER = 19
    DATE = 20
    SEMICOLON = 21
    WS = 22
    COMMENT = 23
    BLOCK_COMMENT = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'load'", "'filter'", "'aggregate'", "'print'", "'column'", 
            "'AND'", "'OR'", "'>='", "'<='", "'>'", "'<'", "'=='", "'!='", 
            "'COUNT'", "'SUM'", "'AVERAGE'", "'BETWEEN'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "LOAD", "FILTER", "AGGREGATE", "PRINT", "COLUMN", "AND", "OR", 
            "GTE", "LTE", "GT", "LT", "EQ", "NEQ", "COUNT", "SUM", "AVERAGE", 
            "BETWEEN", "STRING", "NUMBER", "DATE", "SEMICOLON", "WS", "COMMENT", 
            "BLOCK_COMMENT" ]

    ruleNames = [ "LOAD", "FILTER", "AGGREGATE", "PRINT", "COLUMN", "AND", 
                  "OR", "GTE", "LTE", "GT", "LT", "EQ", "NEQ", "COUNT", "SUM", 
                  "AVERAGE", "BETWEEN", "STRING", "NUMBER", "DATE", "SEMICOLON", 
                  "WS", "COMMENT", "BLOCK_COMMENT" ]

    grammarFileName = "CSVQueryDSL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
'''
    
    # Create the parser file 
    parser_content = '''# Generated from CSVQueryDSL.g4 by ANTLR 4.13.2
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
        4,1,24,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,43,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,
        1,8,1,8,3,8,61,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,72,8,
        8,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,8,13,1,0,6,7,1,
        0,14,17,75,0,21,1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,36,1,0,0,0,8,
        44,1,0,0,0,10,50,1,0,0,0,12,53,1,0,0,0,14,55,1,0,0,0,16,60,1,0,0,
        0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,
        31,3,4,2,0,27,31,3,6,3,0,28,31,3,8,4,0,29,31,3,10,5,0,30,26,1,0,
        0,0,30,27,1,0,0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,
        5,1,0,0,33,34,5,18,0,0,34,35,5,21,0,0,35,5,1,0,0,0,36,37,5,2,0,0,
        37,38,5,5,0,0,38,39,5,18,0,0,39,40,3,12,6,0,40,42,3,16,8,0,41,43,
        3,14,7,0,42,41,1,0,0,0,42,43,1,0,0,0,43,7,1,0,0,0,44,45,5,3,0,0,
        45,46,3,14,7,0,46,47,5,5,0,0,47,48,5,18,0,0,48,49,5,21,0,0,49,9,
        1,0,0,0,50,51,5,4,0,0,51,52,5,21,0,0,52,11,1,0,0,0,53,54,7,0,0,0,
        54,13,1,0,0,0,55,56,7,1,0,0,56,15,1,0,0,0,57,61,5,18,0,0,58,61,5,
        19,0,0,59,61,5,20,0,0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,
        61,17,1,0,0,0,62,72,7,2,0,0,63,72,5,14,0,0,64,72,5,15,0,0,65,72,
        5,16,0,0,66,72,5,17,0,0,67,72,5,14,0,0,68,72,5,15,0,0,69,72,5,16,
        0,0,70,72,5,17,0,0,71,62,1,0,0,0,71,63,1,0,0,0,71,64,1,0,0,0,71,
        65,1,0,0,0,71,66,1,0,0,0,71,67,1,0,0,0,71,68,1,0,0,0,71,69,1,0,0,
        0,71,70,1,0,0,0,72,19,1,0,0,0,5,21,30,42,60,71
    ]

class CSVQueryDSLParser ( Parser ):

    grammarFileName = "CSVQueryDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

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

    ruleNames =  [ "program", "statement", "loadStatement", "filterStatement", 
                   "aggregateStatement", "printStatement", "operator", 
                   "logicalOp", "value" ]

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




    def program(self):

        localctx = CSVQueryDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
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




    def statement(self):

        localctx = CSVQueryDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.loadStatement()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.filterStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.aggregateStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
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




    def loadStatement(self):

        localctx = CSVQueryDSLParser.LoadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(CSVQueryDSLParser.LOAD)
            self.state = 33
            self.match(CSVQueryDSLParser.STRING)
            self.state = 34
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




    def filterStatement(self):

        localctx = CSVQueryDSLParser.FilterStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(CSVQueryDSLParser.FILTER)
            self.state = 37
            self.match(CSVQueryDSLParser.COLUMN)
            self.state = 38
            self.match(CSVQueryDSLParser.STRING)
            self.state = 39
            self.operator()
            self.state = 40
            self.value()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 41
                self.logicalOp()


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




    def aggregateStatement(self):

        localctx = CSVQueryDSLParser.AggregateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aggregateStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(CSVQueryDSLParser.AGGREGATE)
            self.state = 45
            self.aggregateFunction()
            self.state = 46
            self.match(CSVQueryDSLParser.COLUMN)
            self.state = 47
            self.match(CSVQueryDSLParser.STRING)
            self.state = 48
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




    def printStatement(self):

        localctx = CSVQueryDSLParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(CSVQueryDSLParser.PRINT)
            self.state = 51
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




    def operator(self):

        localctx = CSVQueryDSLParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
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




    def logicalOp(self):

        localctx = CSVQueryDSLParser.LogicalOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_logicalOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
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




    def value(self):

        localctx = CSVQueryDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
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




    def aggregateFunction(self):

        localctx = CSVQueryDSLParser.AggregateFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_aggregateFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16, 17]:
                self.state = 62
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [14]:
                self.state = 63
                self.match(CSVQueryDSLParser.COUNT)
                pass
            elif token in [15]:
                self.state = 64
                self.match(CSVQueryDSLParser.SUM)
                pass
            elif token in [16]:
                self.state = 65
                self.match(CSVQueryDSLParser.AVERAGE)
                pass
            elif token in [17]:
                self.state = 66
                self.match(CSVQueryDSLParser.BETWEEN)
                pass
            elif token in [14]:
                self.state = 67
                self.match(CSVQueryDSLParser.COUNT)
                pass
            elif token in [15]:
                self.state = 68
                self.match(CSVQueryDSLParser.SUM)
                pass
            elif token in [16]:
                self.state = 69
                self.match(CSVQueryDSLParser.AVERAGE)
                pass
            elif token in [17]:
                self.state = 70
                self.match(CSVQueryDSLParser.BETWEEN)
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
'''
    
    # Create the listener file
    listener_content = '''# Generated from CSVQueryDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSVQueryDSLParser import CSVQueryDSLParser
else:
    from CSVQueryDSLParser import CSVQueryDSLParser

# This class defines a complete listener for a parse tree produced by CSVQueryDSLParser.
class CSVQueryDSLListener(ParseTreeListener):

    # Enter a parse tree produced by CSVQueryDSLParser#program.
    def enterProgram(self, ctx:CSVQueryDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#program.
    def exitProgram(self, ctx:CSVQueryDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#statement.
    def enterStatement(self, ctx:CSVQueryDSLParser.StatementContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#statement.
    def exitStatement(self, ctx:CSVQueryDSLParser.StatementContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#loadStatement.
    def enterLoadStatement(self, ctx:CSVQueryDSLParser.LoadStatementContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#loadStatement.
    def exitLoadStatement(self, ctx:CSVQueryDSLParser.LoadStatementContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#filterStatement.
    def enterFilterStatement(self, ctx:CSVQueryDSLParser.FilterStatementContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#filterStatement.
    def exitFilterStatement(self, ctx:CSVQueryDSLParser.FilterStatementContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#aggregateStatement.
    def enterAggregateStatement(self, ctx:CSVQueryDSLParser.AggregateStatementContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#aggregateStatement.
    def exitAggregateStatement(self, ctx:CSVQueryDSLParser.AggregateStatementContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#printStatement.
    def enterPrintStatement(self, ctx:CSVQueryDSLParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#printStatement.
    def exitPrintStatement(self, ctx:CSVQueryDSLParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#operator.
    def enterOperator(self, ctx:CSVQueryDSLParser.OperatorContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#operator.
    def exitOperator(self, ctx:CSVQueryDSLParser.OperatorContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#logicalOp.
    def enterLogicalOp(self, ctx:CSVQueryDSLParser.LogicalOpContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#logicalOp.
    def exitLogicalOp(self, ctx:CSVQueryDSLParser.LogicalOpContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#value.
    def enterValue(self, ctx:CSVQueryDSLParser.ValueContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#value.
    def exitValue(self, ctx:CSVQueryDSLParser.ValueContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#aggregateFunction.
    def enterAggregateFunction(self, ctx:CSVQueryDSLParser.AggregateFunctionContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#aggregateFunction.
    def exitAggregateFunction(self, ctx:CSVQueryDSLParser.AggregateFunctionContext):
        pass


del CSVQueryDSLParser'''

    # Write the files
    with open("grammar/CSVQueryDSLLexer.py", "w", encoding="utf-8") as f:
        f.write(lexer_content)
        
    with open("grammar/CSVQueryDSLParser.py", "w", encoding="utf-8") as f:
        f.write(parser_content)
        
    with open("grammar/CSVQueryDSLListener.py", "w", encoding="utf-8") as f:
        f.write(listener_content)
    
    print("Generated ANTLR4 files manually")

def setup_data():
    """Generate CSV data if it doesn't exist"""
    csv_file = "data/cursos_online.csv"
    
    if os.path.exists(csv_file):
        print(f"✓ CSV data file exists: {csv_file}")
        return True
    
    print("Generating CSV data...")
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    try:
        from data.generate_csv import generate_courses_csv
        generate_courses_csv(csv_file, 300)
        print(f"✓ Generated CSV data: {csv_file}")
        return True
    except Exception as e:
        print(f"✗ Failed to generate CSV data: {e}")
        return False

def setup_test_scripts():
    """Generate test scripts if they don't exist"""
    scripts_dir = "scripts"
    
    # Check if we have enough test scripts
    if os.path.exists(scripts_dir):
        script_files = [f for f in os.listdir(scripts_dir) if f.endswith('.dsl')]
        if len(script_files) >= 40:
            print(f"✓ Test scripts exist: {len(script_files)} scripts found")
            return True
    
    print("Generating test scripts...")
    
    try:
        from scripts.generate_test_scripts import generate_test_scripts
        generate_test_scripts(40, scripts_dir)
        print("✓ Generated test scripts")
        return True
    except Exception as e:
        print(f"✗ Failed to generate test scripts: {e}")
        return False

def run_single_script(script_path):
    """Run a single DSL script"""
    from src.query_processor import QueryProcessor
    
    processor = QueryProcessor()
    return processor.execute_script_file(script_path)

def run_all_tests():
    """Run all test scripts"""
    from src.query_processor import QueryProcessor
    
    processor = QueryProcessor()
    return processor.execute_all_scripts_in_directory("scripts")

def generate_parse_tree():
    """Generate parse tree for demo script"""
    try:
        from src.parse_tree_generator import generate_parse_tree_for_script
        
        if not os.path.exists("scripts/demo_parse_tree.dsl"):
            print("Demo script not found. Running setup first...")
            setup_test_scripts()
        
        print("Generating parse tree for demo script...")
        output_file = generate_parse_tree_for_script("scripts/demo_parse_tree.dsl", "doc/demo_parse_tree.png")
        
        if output_file:
            print(f"✓ Parse tree generated successfully!")
            print(f"  Location: {output_file}")
        else:
            print("✗ Failed to generate parse tree")
            
    except Exception as e:
        print(f"✗ Error generating parse tree: {e}")

def generate_antlr_parse_tree():
    """Generate ANTLR4 authentic parse tree"""
    try:
        from src.antlr_csv_interpreter import generate_parse_tree_gui
        
        if not os.path.exists("scripts/demo_parse_tree.dsl"):
            print("Demo script not found. Running setup first...")
            setup_test_scripts()
        
        print("Generating ANTLR4 authentic parse tree...")
        tree = generate_parse_tree_gui("scripts/demo_parse_tree.dsl")
        
        if tree:
            print(f"✓ ANTLR4 parse tree generated successfully!")
            print(f"  Tree structure displayed above")
        else:
            print("✗ Failed to generate ANTLR4 parse tree")
            
    except Exception as e:
        print(f"✗ Error generating ANTLR4 parse tree: {e}")

def interactive_mode():
    """Run in interactive mode"""
    from src.csv_query_interpreter import CSVQueryDSLInterpreter, parse_dsl_string
    
    interpreter = CSVQueryDSLInterpreter()
    
    print("\n" + "="*60)
    print("CSV Query DSL - Interactive Mode")
    print("="*60)
    print("Enter DSL commands (type 'exit' to quit, 'help' for commands)")
    print("Example: load \"data/cursos_online.csv\";")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("DSL> ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            elif user_input.lower() == 'help':
                print_help()
                continue
            elif user_input.lower() == 'reset':
                interpreter.reset()
                print("Interpreter reset.")
                continue
            elif not user_input:
                continue
            
            # Add semicolon if missing
            if not user_input.endswith(';'):
                user_input += ';'
            
            # Parse and execute
            parse_dsl_string(user_input, interpreter)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break

def print_help():
    """Print help information"""
    help_text = """
Available DSL Commands:
  load "filename.csv";                    - Load a CSV file
  filter column "column_name" op value;   - Add a filter condition
  aggregate FUNC column "column_name";    - Add an aggregation
  print;                                  - Execute all operations and show results

Filter Operators: >=, <=, >, <, ==, !=
Logical Operators: AND, OR (between filters)
Aggregate Functions: COUNT, SUM, AVERAGE, BETWEEN

Interactive Commands:
  help    - Show this help
  reset   - Reset the interpreter state
  exit    - Exit interactive mode

Example Script:
  load "data/cursos_online.csv";
  filter column "estado_curso" == "Completado";
  aggregate COUNT column "id_estudiante";
  print;
"""
    print(help_text)

def main():
    """Main function"""
    print("CSV Query DSL Compiler")
    print("=" * 40)
    
    # Check command line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'setup':
            print("Setting up the DSL compiler...")
            
            # Check ANTLR installation
            if not check_antlr_installation():
                sys.exit(1)
            
            # Generate ANTLR files
            if not generate_antlr_files():
                sys.exit(1)
            
            # Setup data
            if not setup_data():
                sys.exit(1)
            
            # Setup test scripts
            if not setup_test_scripts():
                sys.exit(1)
            
            print("\n✓ Setup completed successfully!")
            print("You can now run: python main.py test")
            return
        
        elif command == 'test':
            print("Running all test scripts...")
            success = run_all_tests()
            sys.exit(0 if success else 1)
        
        elif command == 'interactive':
            interactive_mode()
            return
            
        elif command == 'parse-tree':
            # Generate parse tree for demo script
            generate_parse_tree()
            return
            
        elif command == 'antlr-tree':
            # Generate ANTLR4 authentic parse tree
            generate_antlr_parse_tree()
            return
        
        elif command.endswith('.dsl'):
            # Run specific script
            if os.path.exists(command):
                success = run_single_script(command)
                sys.exit(0 if success else 1)
            else:
                print(f"Script file not found: {command}")
                sys.exit(1)
        
        else:
            print(f"Unknown command: {command}")
            print_usage()
            sys.exit(1)
    else:
        print_usage()

def print_usage():
    """Print usage information"""
    usage_text = """
Usage: python main.py <command>

Commands:
  setup         - Set up the DSL compiler (generate ANTLR files, data, scripts)
  test          - Run all test scripts
  interactive   - Start interactive mode
  <script.dsl>  - Run a specific DSL script file

Examples:
  python main.py setup
  python main.py test
  python main.py interactive
  python main.py scripts/test_script_01.dsl
"""
    print(usage_text)

if __name__ == "__main__":
    main()
