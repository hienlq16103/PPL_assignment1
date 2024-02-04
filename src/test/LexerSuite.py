import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):      
    # def test_simple_string(self):
    #     """test simple string"""
    #     self.assertTrue(TestLexer.test("'Yanxi Palace - 2018'","'Yanxi Palace - 2018',<EOF>",101))
    
    #======== KEYWORD TEST ============
    def test_keyword_0(self):
        input = "number"
        expect = "number,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,100))
    def test_keyword_1(self):
        input = "bool"
        expect = "bool,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))
    def test_keyword_2(self):
        input = "string"
        expect = "string,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,102))
    def test_keyword_3(self):
        input = "var"
        expect = "var,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,103))
    def test_keyword_4(self):
        input = "dynamic"
        expect = "dynamic,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,104))
    def test_keyword_5(self):
        input = "return"
        expect = "return,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,105))
    def test_keyword_6(self):
        input = "func"
        expect = "func,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,106))
    def test_keyword_7(self):
        input = "for"
        expect = "for,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,107))
    def test_keyword_8(self):
        input = "until"
        expect = "until,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,108))
    def test_keyword_9(self):
        input = "by"
        expect = "by,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,109))
    def test_keyword_10(self):
        input = "break"
        expect = "break,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,110))
    def test_keyword_11(self):
        input = "continue"
        expect = "continue,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,111))
    def test_keyword_12(self):
        input = "if"
        expect = "if,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))
    def test_keyword_13(self):
        input = "else"
        expect = "else,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,113))
    def test_keyword_14(self):
        input = "elif"
        expect = "elif,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))
    def test_keyword_15(self):
        input = "begin"
        expect = "begin,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,115))
    def test_keyword_16(self):
        input = "end"
        expect = "end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,116))
    
    #======== OPERATOR TEST ============
    def test_operator_0(self):
        input = "+"
        expect = "+,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,117))
    def test_operator_1(self):
        input = "-"
        expect = "-,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,118))
    def test_operator_2(self):
        input = "*"
        expect = "*,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,119))
    def test_operator_3(self):
        input = "/"
        expect = "/,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,120))
    def test_operator_4(self):
        input = "%"
        expect = "%,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,121))
    def test_operator_5(self):
        input = "="
        expect = "=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,122))
    def test_operator_6(self):
        input = "!="
        expect = "!=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,123))
    def test_operator_7(self):
        input = "<-"
        expect = "<-,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,124))
    def test_operator_8(self):
        input = "<"
        expect = "<,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,125))
    def test_operator_8(self):
        input = "<="
        expect = "<=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,126))
    def test_operator_9(self):
        input = ">"
        expect = ">,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,127))
    def test_operator_10(self):
        input = ">="
        expect = ">=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,128))
    def test_operator_11(self):
        input = "..."
        expect = "...,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,129))
    def test_operator_12(self):
        input = "=="
        expect = "==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,130))
    def test_operator_13(self):
        input = "not"
        expect = "not,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,131))
    def test_operator_14(self):
        input = "and"
        expect = "and,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,132))
    def test_operator_15(self):
        input = "or"
        expect = "or,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,133))
    def test_operator_incorrect_case_0(self):
        input = "!"
        expect = "Error Token !"
        self.assertTrue(TestLexer.test(input,expect,134))
    def test_operator_incorrect_case_1(self):
        input = "^"
        expect = "Error Token ^"
        self.assertTrue(TestLexer.test(input,expect,135))
    def test_operator_incorrect_case_2(self):
        input = "&&"
        expect = "Error Token &"
        self.assertTrue(TestLexer.test(input,expect,136))
    def test_operator_incorrect_case_3(self):
        input = "||"
        expect = "Error Token |"
        self.assertTrue(TestLexer.test(input,expect,137))
        
    #======== SEPERATOR TEST ============
    def test_seperator_0(self):
        input = "("
        expect = "(,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,138))
    def test_seperator_1(self):
        input = ")"
        expect = "),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,139))
    def test_seperator_2(self):
        input = "["
        expect = "[,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,140))
    def test_seperator_4(self):
        input = "]"
        expect = "],<EOF>"
        self.assertTrue(TestLexer.test(input,expect,141))
    def test_seperator_5(self):
        input = ","
        expect = ",,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,142))
    def test_seperator_6(self):
        input = '''
        '''
        expect = '''\n\n,<EOF>'''
        self.assertTrue(TestLexer.test(input,expect,143))
    def test_seperator_incorrect_case_0(self):
        input = "{"
        expect = "Error Token {"
        self.assertTrue(TestLexer.test(input,expect,144))
    def test_seperator_incorrect_case_1(self):
        input = "}"
        expect = "Error Token }"
        self.assertTrue(TestLexer.test(input,expect,145))
    def test_seperator_incorrect_case_2(self):
        input = ";"
        expect = "Error Token ;"
        self.assertTrue(TestLexer.test(input,expect,146))
        
    #======== LITERAL TEST ============
    #-------- number test -------------
    def test_number_0(self):
        input = "0"
        expect = "0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,147))
    def test_number_1(self):
        input = "199"
        expect = "199,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,148))
    def test_number_2(self):
        input = "12."
        expect = "12.,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,149))
    def test_number_3(self):
        input = "12.3"
        expect = "12.3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,150))
    def test_number_4(self):
        input = "12.3e3"
        expect = "12.3e3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,151))
    def test_number_5(self):
        input = "12.3e-30"
        expect = "12.3e-30,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,152))
    def test_number_6(self):
        input = "0.0"
        expect = "0.0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,153))
    def test_number_7(self):
        input = "0.0"
        expect = "0.0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,154))
    def test_number_8(self):
        input = "1.2E53"
        expect = "1.2E53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,155))
    def test_number_9(self):
        input = "1.2E-53"
        expect = "1.2E-53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,156))
    def test_number_10(self):
        input = "1.2E+53"
        expect = "1.2E+53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,157))
    def test_number_11(self):
        input = "111.223e+53"
        expect = "111.223e+53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,158))
    def test_number_12(self):
        input = "111.e+53"
        expect = "111.e+53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,159))
    def test_number_13(self):
        input = "16e+53"
        expect = "16e+53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,160))
    def test_number_14(self):
        input = "16e-53"
        expect = "16e-53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,161))
    def test_number_15(self):
        input = "16e53"
        expect = "16e53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,162))
    def test_number_16(self):
        input = "16E53"
        expect = "16E53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,163))
    def test_number_17(self):
        input = "16E+53"
        expect = "16E+53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,164))
    def test_number_18(self):
        input = "16E-53"
        expect = "16E-53,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,165))
    def test_number_19(self):
        input = ".2e13"
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input,expect,166))
    def test_number_20(self):
        input = ".e13"
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input,expect,167))
    def test_number_21(self):
        input = "5.2e"
        expect = "5.2,e,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,168))
    def test_number_22(self):
        input = "5.2e+"
        expect = "5.2,e,+,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,169))
    def test_number_23(self):
        input = "e3"
        expect = "e3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,170))
    #-------- boolean test -------------
    def test_boolean_0(self):
        input = "false"
        expect = "false,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,171))
    def test_boolean_1(self):
        input = "true"
        expect = "true,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,172))
    #-------- string test -------------
    def test_string_0(self):
        input = '''"Hello world"'''
        expect = "Hello world,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,173))
    def test_string_1(self):
        input = '''"Hello \b world"'''
        expect = "Hello \b world,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,174))
    def test_string_2(self):
        input = '''"\fHello \b world"'''
        expect = "\fHello \b world,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,175))
    def test_string_3(self):
        input = '''"Hello world\\r"'''
        expect = "Hello world\\r,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,176))
    def test_string_4(self):
        input = '''"Hello\\n \\t world\\r"'''
        expect = "Hello\\n \\t world\\r,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,177))
    def test_string_5(self):
        input = '''"Hello\\n \\t world\\r,\\\'!@#$%^&*()_+-=[]\\\\"'''
        expect = "Hello\\n \\t world\\r,\\\'!@#$%^&*()_+-=[]\\\\,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,178))
    def test_string_6(self):
        input = '''"Hello world \'""'''
        expect = "Hello world \'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,179))
    def test_string_7(self):
        input = '''"Hello world \\a'''
        expect = "Illegal Escape In String: Hello world \\a"
        self.assertTrue(TestLexer.test(input,expect,180))
    def test_string_8(self):
        input = '''"Hello\\n world \\aabc\\n"'''
        expect = "Illegal Escape In String: Hello\\n world \\a"
        self.assertTrue(TestLexer.test(input,expect,181))
    def test_string_9(self):
        input = '''"Hello\\n 'world \\"'''
        expect = "Illegal Escape In String: Hello\\n 'world \\\""
        self.assertTrue(TestLexer.test(input,expect,182))
    def test_string_10(self):
        input = '''"Me\\n at\\t the\\ zoo"'''
        expect = "Illegal Escape In String: Me\\n at\\t the\\ "
        self.assertTrue(TestLexer.test(input,expect,183))
    def test_string_11(self):
        input = '''"Me at" the zoo"'''
        expect = "Me at,the,zoo,Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,184))
    def test_string_12(self):
        input = '''"Me at the zoo'''
        expect = "Unclosed String: Me at the zoo"
        self.assertTrue(TestLexer.test(input,expect,185))
    def test_string_13(self):
        input = '''"Me at\n the zoo"'''
        expect = "Unclosed String: Me at"
        self.assertTrue(TestLexer.test(input,expect,186))
    def test_string_14(self):
        input = '''"Me at the zoo""'''
        expect = "Me at the zoo,Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,187))
    def test_string_15(self):
        input = '''"Me at the zoo'"'''
        expect = "Unclosed String: Me at the zoo'\""
        self.assertTrue(TestLexer.test(input,expect,188))
    def test_string_16(self):
        input = '''"Me' at\' the zoo"'''
        expect = "Me' at\' the zoo,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,189))
    def test_string_17(self):
        input = '''"Me' at\ the zoo"'''
        expect = "Illegal Escape In String: Me' at\ "
        self.assertTrue(TestLexer.test(input,expect,190))
    def test_string_18(self):
        input = '''"Me' a\t t\he zoo"'''
        expect = "Illegal Escape In String: Me' a	 t\h"
        self.assertTrue(TestLexer.test(input,expect,191))
    def test_string_19(self):
        input = '''"Me at\r the zoo"'''
        expect = "Unclosed String: Me at"
        self.assertTrue(TestLexer.test(input,expect,192))
        
    #======== COMMENT TEST ============
    def test_comment_0(self):
        input = '''## This is a comment'''
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,193))
    def test_comment_1(self):
        input = '''abc## This is a comment'''
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,194))
    def test_comment_2(self):
        input = '''pi <- 3.14 ## This is a pi'''
        expect = "pi,<-,3.14,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,195))
    def test_comment_3(self):
        input = '''## program
        6.28'''
        expect = "6.28,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,196))
    def test_comment_4(self):
        input = '''## nameless\n program'''
        expect = "program,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,197))
    def test_comment_5(self):
        input = '''## nameless\\n
        program'''
        expect = "program,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,198))
    def test_comment_6(self):
        input = '''# this is a comment'''
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input,expect,199))   
    #======== IDENTIFIER TEST ============
    def test_identifier_0(self):
        input = '''variableDeclaration09'''
        expect = "variableDeclaration09,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,200))
    def test_identifier_1(self):
        input = '''ClassDeclaration_02'''
        expect = "ClassDeclaration_02,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,201))   
    def test_identifier_2(self):
        input = '''_ClassDeclaration_02'''
        expect = "_ClassDeclaration_02,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,201))  
    def test_identifier_3(self):
        input = '''22abc'''
        expect = "22,abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,202))  