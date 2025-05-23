# Generated from grammar/CSVQueryDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSVQueryDSLParser import CSVQueryDSLParser
else:
    from CSVQueryDSLParser import CSVQueryDSLParser

# This class defines a complete generic visitor for a parse tree produced by CSVQueryDSLParser.

class CSVQueryDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSVQueryDSLParser#program.
    def visitProgram(self, ctx:CSVQueryDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#statement.
    def visitStatement(self, ctx:CSVQueryDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#loadStatement.
    def visitLoadStatement(self, ctx:CSVQueryDSLParser.LoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#filterStatement.
    def visitFilterStatement(self, ctx:CSVQueryDSLParser.FilterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#aggregateStatement.
    def visitAggregateStatement(self, ctx:CSVQueryDSLParser.AggregateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#printStatement.
    def visitPrintStatement(self, ctx:CSVQueryDSLParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#operator.
    def visitOperator(self, ctx:CSVQueryDSLParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#logicalOp.
    def visitLogicalOp(self, ctx:CSVQueryDSLParser.LogicalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#aggregateFunction.
    def visitAggregateFunction(self, ctx:CSVQueryDSLParser.AggregateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#value.
    def visitValue(self, ctx:CSVQueryDSLParser.ValueContext):
        return self.visitChildren(ctx)



del CSVQueryDSLParser