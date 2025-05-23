# Generated from CSVQueryDSL.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

class CSVQueryDSLLexer(Lexer):

    atn = None
    decisionsToDFA = []

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
        self._interp = None
        self._actions = None
        self._predicates = None