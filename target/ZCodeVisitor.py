# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration_list.
    def visitDeclaration_list(self, ctx:ZCodeParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration.
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_declaration.
    def visitVariable_declaration(self, ctx:ZCodeParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_type.
    def visitPrimitive_type(self, ctx:ZCodeParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#impicit_type.
    def visitImpicit_type(self, ctx:ZCodeParser.Impicit_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_declaration.
    def visitArray_declaration(self, ctx:ZCodeParser.Array_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_size.
    def visitArray_size(self, ctx:ZCodeParser.Array_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_size_list.
    def visitArray_size_list(self, ctx:ZCodeParser.Array_size_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_declaration.
    def visitFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:ZCodeParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_list.
    def visitParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#extra_parameter.
    def visitExtra_parameter(self, ctx:ZCodeParser.Extra_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_seperator.
    def visitFunction_seperator(self, ctx:ZCodeParser.Function_seperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_body.
    def visitFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block.
    def visitBlock(self, ctx:ZCodeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement_list.
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)



del ZCodeParser