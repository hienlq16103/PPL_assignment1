# Generated from e:/PPL/assignment1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
        4,1,50,299,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,86,8,1,1,2,1,2,3,2,90,8,2,1,3,1,3,3,3,94,8,
        3,1,3,1,3,1,3,1,3,3,3,100,8,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,108,8,
        3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,120,8,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,132,8,8,1,9,1,9,1,9,1,9,1,9,3,
        9,139,8,9,1,10,1,10,1,10,1,10,1,10,3,10,146,8,10,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,3,12,157,8,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,173,8,15,
        1,16,1,16,1,16,1,16,1,16,3,16,180,8,16,1,17,1,17,1,17,1,17,3,17,
        186,8,17,1,18,1,18,3,18,190,8,18,1,18,3,18,193,8,18,1,19,1,19,1,
        19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,3,20,205,8,20,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,216,8,21,1,22,1,22,1,23,1,
        23,1,23,1,23,3,23,224,8,23,1,24,1,24,1,24,1,24,3,24,230,8,24,1,25,
        1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,
        1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,
        1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,33,
        1,33,1,33,1,34,1,34,1,34,1,34,3,34,278,8,34,1,35,1,35,1,35,1,35,
        1,35,3,35,285,8,35,1,36,1,36,1,37,1,37,1,37,3,37,292,8,37,1,38,1,
        38,1,38,3,38,297,8,38,1,38,0,0,39,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,72,74,76,0,2,1,0,2,4,1,0,5,6,290,0,78,1,0,0,0,2,85,1,0,0,0,
        4,89,1,0,0,0,6,107,1,0,0,0,8,109,1,0,0,0,10,111,1,0,0,0,12,113,1,
        0,0,0,14,123,1,0,0,0,16,131,1,0,0,0,18,138,1,0,0,0,20,145,1,0,0,
        0,22,147,1,0,0,0,24,156,1,0,0,0,26,158,1,0,0,0,28,164,1,0,0,0,30,
        172,1,0,0,0,32,179,1,0,0,0,34,181,1,0,0,0,36,192,1,0,0,0,38,194,
        1,0,0,0,40,204,1,0,0,0,42,215,1,0,0,0,44,217,1,0,0,0,46,219,1,0,
        0,0,48,229,1,0,0,0,50,231,1,0,0,0,52,236,1,0,0,0,54,241,1,0,0,0,
        56,246,1,0,0,0,58,255,1,0,0,0,60,259,1,0,0,0,62,262,1,0,0,0,64,265,
        1,0,0,0,66,268,1,0,0,0,68,277,1,0,0,0,70,284,1,0,0,0,72,286,1,0,
        0,0,74,291,1,0,0,0,76,296,1,0,0,0,78,79,3,2,1,0,79,80,5,0,0,1,80,
        1,1,0,0,0,81,82,3,4,2,0,82,83,3,2,1,0,83,86,1,0,0,0,84,86,3,4,2,
        0,85,81,1,0,0,0,85,84,1,0,0,0,86,3,1,0,0,0,87,90,3,6,3,0,88,90,3,
        26,13,0,89,87,1,0,0,0,89,88,1,0,0,0,90,5,1,0,0,0,91,94,3,8,4,0,92,
        94,5,6,0,0,93,91,1,0,0,0,93,92,1,0,0,0,94,95,1,0,0,0,95,96,5,46,
        0,0,96,108,3,74,37,0,97,100,3,8,4,0,98,100,3,10,5,0,99,97,1,0,0,
        0,99,98,1,0,0,0,100,101,1,0,0,0,101,102,5,46,0,0,102,103,5,26,0,
        0,103,104,3,72,36,0,104,105,3,74,37,0,105,108,1,0,0,0,106,108,3,
        12,6,0,107,93,1,0,0,0,107,99,1,0,0,0,107,106,1,0,0,0,108,7,1,0,0,
        0,109,110,7,0,0,0,110,9,1,0,0,0,111,112,7,1,0,0,112,11,1,0,0,0,113,
        114,3,8,4,0,114,115,5,46,0,0,115,119,3,14,7,0,116,117,5,26,0,0,117,
        120,3,18,9,0,118,120,1,0,0,0,119,116,1,0,0,0,119,118,1,0,0,0,120,
        121,1,0,0,0,121,122,3,74,37,0,122,13,1,0,0,0,123,124,5,38,0,0,124,
        125,3,16,8,0,125,126,5,39,0,0,126,15,1,0,0,0,127,128,5,42,0,0,128,
        129,5,40,0,0,129,132,3,16,8,0,130,132,5,42,0,0,131,127,1,0,0,0,131,
        130,1,0,0,0,132,17,1,0,0,0,133,139,3,22,11,0,134,135,5,38,0,0,135,
        136,3,20,10,0,136,137,5,39,0,0,137,139,1,0,0,0,138,133,1,0,0,0,138,
        134,1,0,0,0,139,19,1,0,0,0,140,141,3,22,11,0,141,142,5,40,0,0,142,
        143,3,20,10,0,143,146,1,0,0,0,144,146,3,22,11,0,145,140,1,0,0,0,
        145,144,1,0,0,0,146,21,1,0,0,0,147,148,5,38,0,0,148,149,3,24,12,
        0,149,150,5,39,0,0,150,23,1,0,0,0,151,152,3,72,36,0,152,153,5,40,
        0,0,153,154,3,24,12,0,154,157,1,0,0,0,155,157,3,72,36,0,156,151,
        1,0,0,0,156,155,1,0,0,0,157,25,1,0,0,0,158,159,5,8,0,0,159,160,5,
        46,0,0,160,161,3,28,14,0,161,162,3,76,38,0,162,163,3,36,18,0,163,
        27,1,0,0,0,164,165,5,36,0,0,165,166,3,30,15,0,166,167,5,37,0,0,167,
        29,1,0,0,0,168,169,3,34,17,0,169,170,3,32,16,0,170,173,1,0,0,0,171,
        173,1,0,0,0,172,168,1,0,0,0,172,171,1,0,0,0,173,31,1,0,0,0,174,175,
        5,40,0,0,175,176,3,34,17,0,176,177,3,32,16,0,177,180,1,0,0,0,178,
        180,1,0,0,0,179,174,1,0,0,0,179,178,1,0,0,0,180,33,1,0,0,0,181,182,
        3,8,4,0,182,185,5,46,0,0,183,186,3,14,7,0,184,186,1,0,0,0,185,183,
        1,0,0,0,185,184,1,0,0,0,186,35,1,0,0,0,187,190,3,38,19,0,188,190,
        3,58,29,0,189,187,1,0,0,0,189,188,1,0,0,0,190,193,1,0,0,0,191,193,
        3,74,37,0,192,189,1,0,0,0,192,191,1,0,0,0,193,37,1,0,0,0,194,195,
        5,17,0,0,195,196,3,74,37,0,196,197,3,40,20,0,197,198,5,18,0,0,198,
        199,3,74,37,0,199,39,1,0,0,0,200,201,3,42,21,0,201,202,3,40,20,0,
        202,205,1,0,0,0,203,205,1,0,0,0,204,200,1,0,0,0,204,203,1,0,0,0,
        205,41,1,0,0,0,206,216,3,6,3,0,207,216,3,44,22,0,208,216,3,46,23,
        0,209,216,3,56,28,0,210,216,3,60,30,0,211,216,3,62,31,0,212,216,
        3,58,29,0,213,216,3,64,32,0,214,216,3,38,19,0,215,206,1,0,0,0,215,
        207,1,0,0,0,215,208,1,0,0,0,215,209,1,0,0,0,215,210,1,0,0,0,215,
        211,1,0,0,0,215,212,1,0,0,0,215,213,1,0,0,0,215,214,1,0,0,0,216,
        43,1,0,0,0,217,218,5,26,0,0,218,45,1,0,0,0,219,220,3,50,25,0,220,
        223,3,48,24,0,221,224,3,54,27,0,222,224,1,0,0,0,223,221,1,0,0,0,
        223,222,1,0,0,0,224,47,1,0,0,0,225,226,3,52,26,0,226,227,3,48,24,
        0,227,230,1,0,0,0,228,230,1,0,0,0,229,225,1,0,0,0,229,228,1,0,0,
        0,230,49,1,0,0,0,231,232,5,14,0,0,232,233,3,72,36,0,233,234,3,76,
        38,0,234,235,3,42,21,0,235,51,1,0,0,0,236,237,5,16,0,0,237,238,3,
        72,36,0,238,239,3,76,38,0,239,240,3,42,21,0,240,53,1,0,0,0,241,242,
        5,15,0,0,242,243,3,72,36,0,243,244,3,76,38,0,244,245,3,42,21,0,245,
        55,1,0,0,0,246,247,5,9,0,0,247,248,3,72,36,0,248,249,5,10,0,0,249,
        250,3,72,36,0,250,251,5,11,0,0,251,252,3,72,36,0,252,253,3,76,38,
        0,253,254,3,42,21,0,254,57,1,0,0,0,255,256,5,7,0,0,256,257,3,72,
        36,0,257,258,3,74,37,0,258,59,1,0,0,0,259,260,5,12,0,0,260,261,3,
        74,37,0,261,61,1,0,0,0,262,263,5,13,0,0,263,264,3,74,37,0,264,63,
        1,0,0,0,265,266,3,66,33,0,266,267,3,74,37,0,267,65,1,0,0,0,268,269,
        5,46,0,0,269,270,5,36,0,0,270,271,3,68,34,0,271,272,5,37,0,0,272,
        67,1,0,0,0,273,274,3,72,36,0,274,275,3,70,35,0,275,278,1,0,0,0,276,
        278,1,0,0,0,277,273,1,0,0,0,277,276,1,0,0,0,278,69,1,0,0,0,279,280,
        5,40,0,0,280,281,3,72,36,0,281,282,3,70,35,0,282,285,1,0,0,0,283,
        285,1,0,0,0,284,279,1,0,0,0,284,283,1,0,0,0,285,71,1,0,0,0,286,287,
        5,1,0,0,287,73,1,0,0,0,288,289,5,41,0,0,289,292,3,74,37,0,290,292,
        5,41,0,0,291,288,1,0,0,0,291,290,1,0,0,0,292,75,1,0,0,0,293,294,
        5,41,0,0,294,297,3,74,37,0,295,297,1,0,0,0,296,293,1,0,0,0,296,295,
        1,0,0,0,297,77,1,0,0,0,23,85,89,93,99,107,119,131,138,145,156,172,
        179,185,189,192,204,215,223,229,277,284,291,296
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'expr'", "'number'", "'bool'", "'string'", 
                     "'var'", "'dynamic'", "'return'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'='", "'!='", "'<-'", "'<'", 
                     "'<='", "'>'", "'>='", "'...'", "'=='", "'not'", "'and'", 
                     "'or'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TYPE_NUMBER", "TYPE_BOOL", 
                      "TYPE_STRING", "VAR", "DYNAMIC", "RETURN", "FUNCTION", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MODULO", "EQUAL", "NOT_EQUAL", "ASSIGNMENT", 
                      "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
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
    RULE_array_value = 9
    RULE_multi_dimension_value = 10
    RULE_single_dimension_value = 11
    RULE_array_element_list = 12
    RULE_function_declaration = 13
    RULE_parameter_declaration = 14
    RULE_parameter_list = 15
    RULE_extra_parameter = 16
    RULE_parameter = 17
    RULE_function_body = 18
    RULE_block = 19
    RULE_statement_list = 20
    RULE_statement = 21
    RULE_assignment_statement = 22
    RULE_condition_statement = 23
    RULE_elif_list = 24
    RULE_if_statement = 25
    RULE_elif_statement = 26
    RULE_else_statement = 27
    RULE_for_statement = 28
    RULE_return_statement = 29
    RULE_break_statement = 30
    RULE_continue_statement = 31
    RULE_function_call_statement = 32
    RULE_function_call = 33
    RULE_argument_list = 34
    RULE_extra_argument_list = 35
    RULE_expression = 36
    RULE_newline_list = 37
    RULE_nullable_newline_list = 38

    ruleNames =  [ "program", "declaration_list", "declaration", "variable_declaration", 
                   "primitive_type", "impicit_type", "array_declaration", 
                   "array_size", "array_size_list", "array_value", "multi_dimension_value", 
                   "single_dimension_value", "array_element_list", "function_declaration", 
                   "parameter_declaration", "parameter_list", "extra_parameter", 
                   "parameter", "function_body", "block", "statement_list", 
                   "statement", "assignment_statement", "condition_statement", 
                   "elif_list", "if_statement", "elif_statement", "else_statement", 
                   "for_statement", "return_statement", "break_statement", 
                   "continue_statement", "function_call_statement", "function_call", 
                   "argument_list", "extra_argument_list", "expression", 
                   "newline_list", "nullable_newline_list" ]

    EOF = Token.EOF
    T__0=1
    TYPE_NUMBER=2
    TYPE_BOOL=3
    TYPE_STRING=4
    VAR=5
    DYNAMIC=6
    RETURN=7
    FUNCTION=8
    FOR=9
    UNTIL=10
    BY=11
    BREAK=12
    CONTINUE=13
    IF=14
    ELSE=15
    ELIF=16
    BEGIN=17
    END=18
    PLUS=19
    MINUS=20
    MULTIPLY=21
    DIVIDE=22
    MODULO=23
    EQUAL=24
    NOT_EQUAL=25
    ASSIGNMENT=26
    LESS_THAN=27
    LESS_THAN_OR_EQUAL=28
    GREATER_THAN=29
    GREATER_THAN_OR_EQUAL=30
    STRING_CONCATENATION=31
    STRING_COMPARISION=32
    NOT=33
    AND=34
    OR=35
    LEFT_PARENTHESIS=36
    RIGHT_PARENTHESIS=37
    LEFT_SQUARE_BRACKET=38
    RIGHT_SQUARE_BRACKET=39
    COMMA=40
    NEWLINE=41
    NUMBER=42
    BOOLEAN=43
    STRING=44
    COMMENT=45
    IDENTIFIER=46
    WS=47
    ILLEGAL_ESCAPE=48
    UNCLOSE_STRING=49
    ERROR_CHAR=50

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

        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.declaration_list()
            self.state = 79
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




    def declaration_list(self):

        localctx = ZCodeParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration_list)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.declaration()
                self.state = 82
                self.declaration_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
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




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.variable_declaration()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
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




    def variable_declaration(self):

        localctx = ZCodeParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_declaration)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 3, 4]:
                    self.state = 91
                    self.primitive_type()
                    pass
                elif token in [6]:
                    self.state = 92
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 95
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 96
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 3, 4]:
                    self.state = 97
                    self.primitive_type()
                    pass
                elif token in [5, 6]:
                    self.state = 98
                    self.impicit_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 101
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 102
                self.match(ZCodeParser.ASSIGNMENT)
                self.state = 103
                self.expression()
                self.state = 104
                self.newline_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
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




    def primitive_type(self):

        localctx = ZCodeParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
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




    def impicit_type(self):

        localctx = ZCodeParser.Impicit_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_impicit_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
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


        def ASSIGNMENT(self):
            return self.getToken(ZCodeParser.ASSIGNMENT, 0)

        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declaration




    def array_declaration(self):

        localctx = ZCodeParser.Array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.primitive_type()
            self.state = 114
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 115
            self.array_size()
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 116
                self.match(ZCodeParser.ASSIGNMENT)
                self.state = 117
                self.array_value()
                pass
            elif token in [41]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 121
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




    def array_size(self):

        localctx = ZCodeParser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 124
            self.array_size_list()
            self.state = 125
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




    def array_size_list(self):

        localctx = ZCodeParser.Array_size_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_size_list)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(ZCodeParser.NUMBER)
                self.state = 128
                self.match(ZCodeParser.COMMA)
                self.state = 129
                self.array_size_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_dimension_value(self):
            return self.getTypedRuleContext(ZCodeParser.Single_dimension_valueContext,0)


        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def multi_dimension_value(self):
            return self.getTypedRuleContext(ZCodeParser.Multi_dimension_valueContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value




    def array_value(self):

        localctx = ZCodeParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_value)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.single_dimension_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
                self.state = 135
                self.multi_dimension_value()
                self.state = 136
                self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_dimension_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_dimension_value(self):
            return self.getTypedRuleContext(ZCodeParser.Single_dimension_valueContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def multi_dimension_value(self):
            return self.getTypedRuleContext(ZCodeParser.Multi_dimension_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_multi_dimension_value




    def multi_dimension_value(self):

        localctx = ZCodeParser.Multi_dimension_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_multi_dimension_value)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.single_dimension_value()
                self.state = 141
                self.match(ZCodeParser.COMMA)
                self.state = 142
                self.multi_dimension_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.single_dimension_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_dimension_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def array_element_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_element_listContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_single_dimension_value




    def single_dimension_value(self):

        localctx = ZCodeParser.Single_dimension_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_single_dimension_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 148
            self.array_element_list()
            self.state = 149
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_element_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_element_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_element_list




    def array_element_list(self):

        localctx = ZCodeParser.Array_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_element_list)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.expression()
                self.state = 152
                self.match(ZCodeParser.COMMA)
                self.state = 153
                self.array_element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.expression()
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


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def function_body(self):
            return self.getTypedRuleContext(ZCodeParser.Function_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration




    def function_declaration(self):

        localctx = ZCodeParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ZCodeParser.FUNCTION)
            self.state = 159
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 160
            self.parameter_declaration()
            self.state = 161
            self.nullable_newline_list()
            self.state = 162
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




    def parameter_declaration(self):

        localctx = ZCodeParser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 165
            self.parameter_list()
            self.state = 166
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




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameter_list)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.parameter()
                self.state = 169
                self.extra_parameter()
                pass
            elif token in [37]:
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




    def extra_parameter(self):

        localctx = ZCodeParser.Extra_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_extra_parameter)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(ZCodeParser.COMMA)
                self.state = 175
                self.parameter()
                self.state = 176
                self.extra_parameter()
                pass
            elif token in [37]:
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




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.primitive_type()
            self.state = 182
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.state = 183
                self.array_size()
                pass
            elif token in [37, 40]:
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


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_body




    def function_body(self):

        localctx = ZCodeParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function_body)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17]:
                    self.state = 187
                    self.block()
                    pass
                elif token in [7]:
                    self.state = 188
                    self.return_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.newline_list()
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




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ZCodeParser.BEGIN)
            self.state = 195
            self.newline_list()
            self.state = 196
            self.statement_list()
            self.state = 197
            self.match(ZCodeParser.END)
            self.state = 198
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




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement_list)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6, 7, 9, 12, 13, 14, 17, 26, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.statement()
                self.state = 201
                self.statement_list()
                pass
            elif token in [18]:
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


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def condition_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Condition_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_statementContext,0)


        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.variable_declaration()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.assignment_statement()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.condition_statement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.for_statement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.break_statement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 211
                self.continue_statement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 212
                self.return_statement()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 8)
                self.state = 213
                self.function_call_statement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 9)
                self.state = 214
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


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT(self):
            return self.getToken(ZCodeParser.ASSIGNMENT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ZCodeParser.ASSIGNMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_condition_statement




    def condition_statement(self):

        localctx = ZCodeParser.Condition_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_condition_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.if_statement()
            self.state = 220
            self.elif_list()
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 221
                self.else_statement()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elif_list)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.elif_statement()
                self.state = 226
                self.elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(ZCodeParser.IF)
            self.state = 232
            self.expression()
            self.state = 233
            self.nullable_newline_list()
            self.state = 234
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(ZCodeParser.ELIF)
            self.state = 237
            self.expression()
            self.state = 238
            self.nullable_newline_list()
            self.state = 239
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ZCodeParser.ELSE)
            self.state = 242
            self.expression()
            self.state = 243
            self.nullable_newline_list()
            self.state = 244
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(ZCodeParser.FOR)
            self.state = 247
            self.expression()
            self.state = 248
            self.match(ZCodeParser.UNTIL)
            self.state = 249
            self.expression()
            self.state = 250
            self.match(ZCodeParser.BY)
            self.state = 251
            self.expression()
            self.state = 252
            self.nullable_newline_list()
            self.state = 253
            self.statement()
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




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(ZCodeParser.RETURN)
            self.state = 256
            self.expression()
            self.state = 257
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(ZCodeParser.BREAK)
            self.state = 260
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(ZCodeParser.CONTINUE)
            self.state = 263
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call_statement




    def function_call_statement(self):

        localctx = ZCodeParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_function_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.function_call()
            self.state = 266
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_listContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call




    def function_call(self):

        localctx = ZCodeParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 269
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 270
            self.argument_list()
            self.state = 271
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def extra_argument_list(self):
            return self.getTypedRuleContext(ZCodeParser.Extra_argument_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument_list




    def argument_list(self):

        localctx = ZCodeParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_argument_list)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.expression()
                self.state = 274
                self.extra_argument_list()
                pass
            elif token in [37]:
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


    class Extra_argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def extra_argument_list(self):
            return self.getTypedRuleContext(ZCodeParser.Extra_argument_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_extra_argument_list




    def extra_argument_list(self):

        localctx = ZCodeParser.Extra_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_extra_argument_list)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(ZCodeParser.COMMA)
                self.state = 280
                self.expression()
                self.state = 281
                self.extra_argument_list()
                pass
            elif token in [37]:
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(ZCodeParser.T__0)
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




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_newline_list)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(ZCodeParser.NEWLINE)
                self.state = 289
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_newline_list




    def nullable_newline_list(self):

        localctx = ZCodeParser.Nullable_newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_nullable_newline_list)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(ZCodeParser.NEWLINE)
                self.state = 294
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





