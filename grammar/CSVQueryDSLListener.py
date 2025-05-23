# Generated from CSVQueryDSL.g4 by ANTLR 4.13.2
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

del CSVQueryDSLParser