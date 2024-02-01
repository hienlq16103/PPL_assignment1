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
	: (single_dimension_number | single_dimension_string | single_dimension_bool)
	| LEFT_SQUARE_BRACKET (multi_dimension_number | multi_dimension_string | multi_dimension_bool)  RIGHT_SQUARE_BRACKET
	;

multi_dimension_number
	: single_dimension_number extra_dimension_number
	|
	;
extra_dimension_number
	: COMMA single_dimension_number extra_dimension_number
	|
	;
multi_dimension_string
	: single_dimension_string extra_dimension_string
	|
	;
extra_dimension_string
	: COMMA single_dimension_string extra_dimension_string
	|
	;
multi_dimension_bool
	: single_dimension_bool extra_dimension_bool
	|
	;
extra_dimension_bool
	: COMMA single_dimension_bool extra_dimension_bool
	|
	;

single_dimension_number : LEFT_SQUARE_BRACKET array_number RIGHT_SQUARE_BRACKET;
single_dimension_string: LEFT_SQUARE_BRACKET array_string RIGHT_SQUARE_BRACKET;
single_dimension_bool: LEFT_SQUARE_BRACKET array_bool RIGHT_SQUARE_BRACKET;
array_number
	: NUMBER extra_array_number
	|
	;
extra_array_number
	: COMMA NUMBER extra_array_number
	|
	;
array_string
	: STRING extra_array_string
	|
	;
extra_array_string
	: COMMA STRING extra_array_string
	|
	;
array_bool
	: BOOLEAN extra_array_bool
	|
	;
extra_array_bool
	: COMMA BOOLEAN extra_array_bool
	|
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
statement
	: variable_declaration
	| assignment_statement
	| condition_statement
	| for_statement
	| break_statement
	| continue_statement
	| return_statement
	| function_call_statement
	| block
	;

assignment_statement: ASSIGNMENT;
condition_statement: if_statement elif_list (else_statement | );

elif_list
	: elif_statement elif_list
	|
	;
if_statement: IF expression nullable_newline_list statement;
elif_statement: ELIF expression nullable_newline_list statement;
else_statement: ELSE expression nullable_newline_list statement;

for_statement: FOR expression UNTIL expression BY expression nullable_newline_list statement;

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
expression: 'expr';


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