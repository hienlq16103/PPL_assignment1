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


    # Visit a parse tree produced by ZCodeParser#array_value.
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multi_dimension_value.
    def visitMulti_dimension_value(self, ctx:ZCodeParser.Multi_dimension_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#extra_dimension_value.
    def visitExtra_dimension_value(self, ctx:ZCodeParser.Extra_dimension_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#single_dimension_value.
    def visitSingle_dimension_value(self, ctx:ZCodeParser.Single_dimension_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_element_list.
    def visitArray_element_list(self, ctx:ZCodeParser.Array_element_listContext):
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


    # Visit a parse tree produced by ZCodeParser#simple_statement.
    def visitSimple_statement(self, ctx:ZCodeParser.Simple_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#conditional_statement.
    def visitConditional_statement(self, ctx:ZCodeParser.Conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#open_statement.
    def visitOpen_statement(self, ctx:ZCodeParser.Open_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#close_statement.
    def visitClose_statement(self, ctx:ZCodeParser.Close_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#open_if.
    def visitOpen_if(self, ctx:ZCodeParser.Open_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#close_if.
    def visitClose_if(self, ctx:ZCodeParser.Close_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#open_else.
    def visitOpen_else(self, ctx:ZCodeParser.Open_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#close_else.
    def visitClose_else(self, ctx:ZCodeParser.Close_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#open_elif_list.
    def visitOpen_elif_list(self, ctx:ZCodeParser.Open_elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#close_elif_list.
    def visitClose_elif_list(self, ctx:ZCodeParser.Close_elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#open_elif.
    def visitOpen_elif(self, ctx:ZCodeParser.Open_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#close_elif.
    def visitClose_elif(self, ctx:ZCodeParser.Close_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:ZCodeParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call.
    def visitFunction_call(self, ctx:ZCodeParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argument_list.
    def visitArgument_list(self, ctx:ZCodeParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#extra_argument_list.
    def visitExtra_argument_list(self, ctx:ZCodeParser.Extra_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression1.
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression2.
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression3.
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression4.
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression5.
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression6.
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression7.
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sub_expression.
    def visitSub_expression(self, ctx:ZCodeParser.Sub_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_operator.
    def visitRelational_operator(self, ctx:ZCodeParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#element_extract_expression.
    def visitElement_extract_expression(self, ctx:ZCodeParser.Element_extract_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_extract_expression.
    def visitFunction_extract_expression(self, ctx:ZCodeParser.Function_extract_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_extract_expression.
    def visitArray_extract_expression(self, ctx:ZCodeParser.Array_extract_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operators.
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullable_newline_list.
    def visitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        return self.visitChildren(ctx)



del ZCodeParser