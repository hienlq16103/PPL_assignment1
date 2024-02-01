# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u00a7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\38\n\3\3\4\3\4\5\4<\n\4\3\5")
        buf.write("\3\5\5\5@\n\5\3\5\3\5\3\5\3\5\5\5F\n\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5N\n\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\na\n\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r")
        buf.write("q\n\r\3\16\3\16\3\16\3\16\3\16\5\16x\n\16\3\17\3\17\3")
        buf.write("\17\3\17\5\17~\n\17\3\20\3\20\3\20\5\20\u0083\n\20\3\21")
        buf.write("\3\21\5\21\u0087\n\21\3\21\5\21\u008a\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u0096\n\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\30\5\30\u00a5\n\30\3\30\2\2\31\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\2\4\3\2\5\7\3\2\b\t")
        buf.write("\2\u009e\2\60\3\2\2\2\4\67\3\2\2\2\6;\3\2\2\2\bM\3\2\2")
        buf.write("\2\nO\3\2\2\2\fQ\3\2\2\2\16S\3\2\2\2\20X\3\2\2\2\22`\3")
        buf.write("\2\2\2\24b\3\2\2\2\26h\3\2\2\2\30p\3\2\2\2\32w\3\2\2\2")
        buf.write("\34y\3\2\2\2\36\u0082\3\2\2\2 \u0089\3\2\2\2\"\u008b\3")
        buf.write("\2\2\2$\u0095\3\2\2\2&\u0097\3\2\2\2(\u0099\3\2\2\2*\u009b")
        buf.write("\3\2\2\2,\u009f\3\2\2\2.\u00a4\3\2\2\2\60\61\5\4\3\2\61")
        buf.write("\62\7\2\2\3\62\3\3\2\2\2\63\64\5\6\4\2\64\65\5\4\3\2\65")
        buf.write("8\3\2\2\2\668\5\6\4\2\67\63\3\2\2\2\67\66\3\2\2\28\5\3")
        buf.write("\2\2\29<\5\b\5\2:<\5\24\13\2;9\3\2\2\2;:\3\2\2\2<\7\3")
        buf.write("\2\2\2=@\5\n\6\2>@\7\t\2\2?=\3\2\2\2?>\3\2\2\2@A\3\2\2")
        buf.write("\2AB\7\61\2\2BN\5.\30\2CF\5\n\6\2DF\5\f\7\2EC\3\2\2\2")
        buf.write("ED\3\2\2\2FG\3\2\2\2GH\7\61\2\2HI\7\35\2\2IJ\5,\27\2J")
        buf.write("K\5.\30\2KN\3\2\2\2LN\5\16\b\2M?\3\2\2\2ME\3\2\2\2ML\3")
        buf.write("\2\2\2N\t\3\2\2\2OP\t\2\2\2P\13\3\2\2\2QR\t\3\2\2R\r\3")
        buf.write("\2\2\2ST\5\n\6\2TU\7\61\2\2UV\5\20\t\2VW\5.\30\2W\17\3")
        buf.write("\2\2\2XY\7)\2\2YZ\5\22\n\2Z[\7*\2\2[\21\3\2\2\2\\]\7-")
        buf.write("\2\2]^\7+\2\2^a\5\22\n\2_a\7-\2\2`\\\3\2\2\2`_\3\2\2\2")
        buf.write("a\23\3\2\2\2bc\7\13\2\2cd\7\61\2\2de\5\26\f\2ef\5\36\20")
        buf.write("\2fg\5 \21\2g\25\3\2\2\2hi\7\'\2\2ij\5\30\r\2jk\7(\2\2")
        buf.write("k\27\3\2\2\2lm\5\34\17\2mn\5\32\16\2nq\3\2\2\2oq\3\2\2")
        buf.write("\2pl\3\2\2\2po\3\2\2\2q\31\3\2\2\2rs\7+\2\2st\5\34\17")
        buf.write("\2tu\5\32\16\2ux\3\2\2\2vx\3\2\2\2wr\3\2\2\2wv\3\2\2\2")
        buf.write("x\33\3\2\2\2yz\5\n\6\2z}\7\61\2\2{~\5\20\t\2|~\3\2\2\2")
        buf.write("}{\3\2\2\2}|\3\2\2\2~\35\3\2\2\2\177\u0080\7,\2\2\u0080")
        buf.write("\u0083\5\36\20\2\u0081\u0083\3\2\2\2\u0082\177\3\2\2\2")
        buf.write("\u0082\u0081\3\2\2\2\u0083\37\3\2\2\2\u0084\u0087\5\"")
        buf.write("\22\2\u0085\u0087\5*\26\2\u0086\u0084\3\2\2\2\u0086\u0085")
        buf.write("\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u008a\3\2\2\2\u0089")
        buf.write("\u0086\3\2\2\2\u0089\u0088\3\2\2\2\u008a!\3\2\2\2\u008b")
        buf.write("\u008c\7\24\2\2\u008c\u008d\5.\30\2\u008d\u008e\5$\23")
        buf.write("\2\u008e\u008f\7\25\2\2\u008f\u0090\5.\30\2\u0090#\3\2")
        buf.write("\2\2\u0091\u0092\5&\24\2\u0092\u0093\5$\23\2\u0093\u0096")
        buf.write("\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0091\3\2\2\2\u0095")
        buf.write("\u0094\3\2\2\2\u0096%\3\2\2\2\u0097\u0098\5\b\5\2\u0098")
        buf.write("\'\3\2\2\2\u0099\u009a\7\3\2\2\u009a)\3\2\2\2\u009b\u009c")
        buf.write("\7\n\2\2\u009c\u009d\5,\27\2\u009d\u009e\5.\30\2\u009e")
        buf.write("+\3\2\2\2\u009f\u00a0\7\4\2\2\u00a0-\3\2\2\2\u00a1\u00a2")
        buf.write("\7,\2\2\u00a2\u00a5\5.\30\2\u00a3\u00a5\7,\2\2\u00a4\u00a1")
        buf.write("\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5/\3\2\2\2\20\67;?EM")
        buf.write("`pw}\u0082\u0086\u0089\u0095\u00a4")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'assign'", "'expr'", "'number'", "'bool'", 
                     "'string'", "'var'", "'dynamic'", "'return'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'='", "'!='", "'<-'", 
                     "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'not'", 
                     "'and'", "'or'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "TYPE_NUMBER", 
                      "TYPE_BOOL", "TYPE_STRING", "VAR", "DYNAMIC", "RETURN", 
                      "FUNCTION", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "PLUS", "MINUS", 
                      "MULTIPLY", "DIVIDE", "MODULO", "EQUAL", "NOT_EQUAL", 
                      "ASSIGNMENT", "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
                      "GREATER_THAN_OR_EQUAL", "STRING_CONCATENATION", "STRING_COMPARISION", 
                      "NOT", "AND", "OR", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "COMMA", 
                      "NEWLINE", "NUMBER", "BOOLEAN", "STRING", "COMMENT", 
                      "IDENTIFIER", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declaration_list = 1
    RULE_declaration = 2
    RULE_variable_declaration = 3
    RULE_primitive_type = 4
    RULE_impicit_type = 5
    RULE_array_declaration = 6
    RULE_array_size = 7
    RULE_array_size_list = 8
    RULE_function_declaration = 9
    RULE_parameter_declaration = 10
    RULE_parameter_list = 11
    RULE_extra_parameter = 12
    RULE_parameter = 13
    RULE_function_seperator = 14
    RULE_function_body = 15
    RULE_block = 16
    RULE_statement_list = 17
    RULE_statement = 18
    RULE_assignment_statement = 19
    RULE_return_statement = 20
    RULE_expression = 21
    RULE_newline_list = 22

    ruleNames =  [ "program", "declaration_list", "declaration", "variable_declaration", 
                   "primitive_type", "impicit_type", "array_declaration", 
                   "array_size", "array_size_list", "function_declaration", 
                   "parameter_declaration", "parameter_list", "extra_parameter", 
                   "parameter", "function_seperator", "function_body", "block", 
                   "statement_list", "statement", "assignment_statement", 
                   "return_statement", "expression", "newline_list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    TYPE_NUMBER=3
    TYPE_BOOL=4
    TYPE_STRING=5
    VAR=6
    DYNAMIC=7
    RETURN=8
    FUNCTION=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    PLUS=20
    MINUS=21
    MULTIPLY=22
    DIVIDE=23
    MODULO=24
    EQUAL=25
    NOT_EQUAL=26
    ASSIGNMENT=27
    LESS_THAN=28
    LESS_THAN_OR_EQUAL=29
    GREATER_THAN=30
    GREATER_THAN_OR_EQUAL=31
    STRING_CONCATENATION=32
    STRING_COMPARISION=33
    NOT=34
    AND=35
    OR=36
    LEFT_PARENTHESIS=37
    RIGHT_PARENTHESIS=38
    LEFT_SQUARE_BRACKET=39
    RIGHT_SQUARE_BRACKET=40
    COMMA=41
    NEWLINE=42
    NUMBER=43
    BOOLEAN=44
    STRING=45
    COMMENT=46
    IDENTIFIER=47
    WS=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.declaration_list()
            self.state = 47
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_list" ):
                return visitor.visitDeclaration_list(self)
            else:
                return visitor.visitChildren(self)




    def declaration_list(self):

        localctx = ZCodeParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration_list)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.declaration()
                self.state = 50
                self.declaration_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.variable_declaration()
                pass
            elif token in [ZCodeParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.function_declaration()
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


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ASSIGNMENT(self):
            return self.getToken(ZCodeParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def impicit_type(self):
            return self.getTypedRuleContext(ZCodeParser.Impicit_typeContext,0)


        def array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = ZCodeParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_declaration)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING]:
                    self.state = 59
                    self.primitive_type()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 60
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 63
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 64
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING]:
                    self.state = 65
                    self.primitive_type()
                    pass
                elif token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                    self.state = 66
                    self.impicit_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 69
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 70
                self.match(ZCodeParser.ASSIGNMENT)
                self.state = 71
                self.expression()
                self.state = 72
                self.newline_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.array_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_NUMBER(self):
            return self.getToken(ZCodeParser.TYPE_NUMBER, 0)

        def TYPE_STRING(self):
            return self.getToken(ZCodeParser.TYPE_STRING, 0)

        def TYPE_BOOL(self):
            return self.getToken(ZCodeParser.TYPE_BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = ZCodeParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE_NUMBER) | (1 << ZCodeParser.TYPE_BOOL) | (1 << ZCodeParser.TYPE_STRING))) != 0)):
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


    class Impicit_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_impicit_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpicit_type" ):
                return visitor.visitImpicit_type(self)
            else:
                return visitor.visitChildren(self)




    def impicit_type(self):

        localctx = ZCodeParser.Impicit_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_impicit_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.VAR or _la==ZCodeParser.DYNAMIC):
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


    class Array_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_size(self):
            return self.getTypedRuleContext(ZCodeParser.Array_sizeContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declaration" ):
                return visitor.visitArray_declaration(self)
            else:
                return visitor.visitChildren(self)




    def array_declaration(self):

        localctx = ZCodeParser.Array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.primitive_type()
            self.state = 82
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 83
            self.array_size()
            self.state = 84
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def array_size_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_size_listContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size" ):
                return visitor.visitArray_size(self)
            else:
                return visitor.visitChildren(self)




    def array_size(self):

        localctx = ZCodeParser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 87
            self.array_size_list()
            self.state = 88
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_size_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_size_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_size_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_size_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size_list" ):
                return visitor.visitArray_size_list(self)
            else:
                return visitor.visitChildren(self)




    def array_size_list(self):

        localctx = ZCodeParser.Array_size_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_size_list)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(ZCodeParser.NUMBER)
                self.state = 91
                self.match(ZCodeParser.COMMA)
                self.state = 92
                self.array_size_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ZCodeParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def parameter_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_declarationContext,0)


        def function_seperator(self):
            return self.getTypedRuleContext(ZCodeParser.Function_seperatorContext,0)


        def function_body(self):
            return self.getTypedRuleContext(ZCodeParser.Function_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = ZCodeParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(ZCodeParser.FUNCTION)
            self.state = 97
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 98
            self.parameter_declaration()
            self.state = 99
            self.function_seperator()
            self.state = 100
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration" ):
                return visitor.visitParameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration(self):

        localctx = ZCodeParser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 103
            self.parameter_list()
            self.state = 104
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def extra_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Extra_parameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter_list)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.parameter()
                self.state = 107
                self.extra_parameter()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

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


    class Extra_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def extra_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Extra_parameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_extra_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtra_parameter" ):
                return visitor.visitExtra_parameter(self)
            else:
                return visitor.visitChildren(self)




    def extra_parameter(self):

        localctx = ZCodeParser.Extra_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_extra_parameter)
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(ZCodeParser.COMMA)
                self.state = 113
                self.parameter()
                self.state = 114
                self.extra_parameter()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

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


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_size(self):
            return self.getTypedRuleContext(ZCodeParser.Array_sizeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.primitive_type()
            self.state = 120
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LEFT_SQUARE_BRACKET]:
                self.state = 121
                self.array_size()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS, ZCodeParser.COMMA]:
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


    class Function_seperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def function_seperator(self):
            return self.getTypedRuleContext(ZCodeParser.Function_seperatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_seperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_seperator" ):
                return visitor.visitFunction_seperator(self)
            else:
                return visitor.visitChildren(self)




    def function_seperator(self):

        localctx = ZCodeParser.Function_seperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function_seperator)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.match(ZCodeParser.NEWLINE)
                self.state = 126
                self.function_seperator()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.RETURN, ZCodeParser.FUNCTION, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)

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


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body" ):
                return visitor.visitFunction_body(self)
            else:
                return visitor.visitChildren(self)




    def function_body(self):

        localctx = ZCodeParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_body)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.BEGIN]:
                    self.state = 130
                    self.block()
                    pass
                elif token in [ZCodeParser.RETURN]:
                    self.state = 131
                    self.return_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)

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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ZCodeParser.BEGIN)
            self.state = 138
            self.newline_list()
            self.state = 139
            self.statement_list()
            self.state = 140
            self.match(ZCodeParser.END)
            self.state = 141
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement_list)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.statement()
                self.state = 144
                self.statement_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.variable_declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ZCodeParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ZCodeParser.RETURN)
            self.state = 154
            self.expression()
            self.state = 155
            self.newline_list()
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ZCodeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_newline_list)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(ZCodeParser.NEWLINE)
                self.state = 160
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





