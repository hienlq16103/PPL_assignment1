grammar ZCode;

@lexer::header {
from lexererr import *
2113376
}
options {
	language=Python3;
}
//======================= PARSER =======================
program: declaration_list EOF;

declaration_list
	: declaration declaration_list
	| declaration
	;
declaration: variable_declaration | function_declaration;

variable_declaration
	: (primitive_type | DYNAMIC) IDENTIFIER newline_list
	| (primitive_type | impicit_type) IDENTIFIER ASSIGNMENT expression newline_list
	| array_declaration
	;

primitive_type: TYPE_NUMBER | TYPE_STRING | TYPE_BOOL;
impicit_type: VAR | DYNAMIC;

array_declaration: primitive_type IDENTIFIER array_size (ASSIGNMENT array_value | ) newline_list;
array_size: LEFT_SQUARE_BRACKET array_size_list RIGHT_SQUARE_BRACKET;
array_size_list
	: NUMBER COMMA array_size_list
	| NUMBER
	;
array_value
	: single_dimension_value
	| LEFT_SQUARE_BRACKET multi_dimension_value RIGHT_SQUARE_BRACKET
	;
multi_dimension_value
	: single_dimension_value COMMA multi_dimension_value
	| single_dimension_value
	;
single_dimension_value: LEFT_SQUARE_BRACKET array_element_list RIGHT_SQUARE_BRACKET;
array_element_list
	: expression COMMA array_element_list
	| expression
	;

function_declaration
	: FUNCTION IDENTIFIER parameter_declaration nullable_newline_list function_body
	;

parameter_declaration: LEFT_PARENTHESIS parameter_list RIGHT_PARENTHESIS;
parameter_list
	: parameter extra_parameter 
	|
	;
extra_parameter
	: COMMA parameter extra_parameter
	|
	;
parameter: primitive_type IDENTIFIER (array_size | );

function_body
	: (block | return_statement)
	| newline_list
	;

block: BEGIN newline_list statement_list END newline_list;

statement_list
	: statement statement_list
	|
	;
statement: simple_statement | condition_statement;
simple_statement
	: variable_declaration
	| assignment_statement
	| break_statement
	| continue_statement
	| return_statement
	| function_call_statement
	| block
	| for_statement
	;

condition_statement: open_statement | close_statement;

open_statement
	: open_if open_elif_list
	| close_if close_elif_list open_else
	;
close_statement
	: simple_statement
	| close_if close_elif_list close_else
	;

open_if
	: IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS nullable_newline_list (simple_statement | open_statement );
close_if: IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS nullable_newline_list close_statement ;

open_else: ELSE nullable_newline_list open_statement;
close_else: ELSE nullable_newline_list close_statement;

open_elif_list
	: open_elif open_elif_list
	|
	;
close_elif_list
	: close_elif close_elif_list
	|
	;

open_elif
	: ELIF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS nullable_newline_list (simple_statement | open_statement);
close_elif: ELIF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS nullable_newline_list close_statement;


for_statement: FOR IDENTIFIER UNTIL expression BY expression nullable_newline_list statement;

assignment_statement: ASSIGNMENT newline_list;
return_statement: RETURN expression newline_list;
break_statement: BREAK newline_list;
continue_statement: CONTINUE newline_list;

function_call_statement: function_call newline_list;
function_call: IDENTIFIER LEFT_PARENTHESIS argument_list RIGHT_PARENTHESIS;
argument_list
	: expression extra_argument_list
	| 
	;
extra_argument_list
	: COMMA expression extra_argument_list
	|
	;
expression
	: expression1 STRING_CONCATENATION expression1
	| expression1
	;
expression1
	: expression2 relational_operator expression2
	| expression2
	;
relational_operator
	: EQUAL | STRING_COMPARISION | NOT_EQUAL 
	| LESS_THAN | GREATER_THAN 
	| LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL
	;

expression2
	: expression2 (AND | OR) expression3
	| expression3
	;
expression3
	: expression3 (PLUS | MINUS) expression4
	| expression4
	;
expression4
	: expression4 (MULTIPLY | DIVIDE | MODULO) expression5
	| expression5
	;
expression5
	: NOT expression5
	| expression6
	;
expression6:;

array_extract_expression: (IDENTIFIER | function_call) LEFT_SQUARE_BRACKET index_operators RIGHT_SQUARE_BRACKET;
index_operators
	: expression COMMA index_operators
	| expression
	;
newline_list
	: NEWLINE newline_list
	| NEWLINE
	;
nullable_newline_list
	: NEWLINE newline_list
	|
	;
//======================= TOKENS =======================
//----------------------- Keywords ----------------------

TYPE_NUMBER: 'number';
TYPE_BOOL: 'bool';
TYPE_STRING: 'string';
VAR: 'var';
DYNAMIC: 'dynamic';

RETURN: 'return';

FUNCTION: 'func';

FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';

IF: 'if';
ELSE: 'else';
ELIF: 'elif';

BEGIN: 'begin';
END: 'end';

//----------------------- Operators ----------------------

PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';
EQUAL: '=';
NOT_EQUAL: '!=';
ASSIGNMENT: '<-';
LESS_THAN: '<';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_THAN_OR_EQUAL: '>=';

STRING_CONCATENATION: '...';
STRING_COMPARISION: '==';

NOT: 'not';
AND: 'and';
OR: 'or';

//----------------------- Seperators ----------------------

LEFT_PARENTHESIS: '(';
RIGHT_PARENTHESIS: ')';

LEFT_SQUARE_BRACKET: '[';
RIGHT_SQUARE_BRACKET: ']';

COMMA: ',';
NEWLINE: '\r'? '\n';
//----------------------- Literals ----------------------

NUMBER: INTEGER DECIMAL? EXPONENT?;
BOOLEAN: 'true' | 'false';
STRING: '"' (ESCAPE_SEQUENCE | ~["\r\n\\])* '"' {self.text = self.text[1:-1]};

//----------------------- Miscellaneous ----------------------

COMMENT: '##' .*? ('\r'? '\n' | EOF) -> skip;

IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;
WS : [ \t\b\f]+ -> skip ; // skip spaces, tabs, newlines
ILLEGAL_ESCAPE: '"' (ESCAPE_SEQUENCE | ~["\r\n\\])* '\\' ~[bfrnt'\\] {raise IllegalEscape(self.text[1:])};
UNCLOSE_STRING: '"' (ESCAPE_SEQUENCE | ~["\r\n\\])* {raise UncloseString(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};

//======================= FRAGMENTS =======================
//----------------------- Literals ----------------------

fragment INTEGER: [0-9]+;
fragment DECIMAL: . [0-9]*;
fragment EXPONENT: [eE] [+-]? [0-9]+;
fragment ESCAPE_SEQUENCE: '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\' | '\'"';