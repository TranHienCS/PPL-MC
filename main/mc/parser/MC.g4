//1611097 - Tran Van Hien
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}
program: decl+ EOF;

decl: var_decl|func_decl;

var_decl: primitive_type list_id SM;

primitive_type: INT|FLOAT|STRING|BOOLEAN;

list_id: variable (CM variable)*;

variable: ID (LSB INTLIT RSB)?;

func_decl: (VOID|primitive_type|out_pointer) ID LB param_list? RB block_stmt;

param_list: param (CM param)*;

param: primitive_type ID (LSB RSB)? ;

block_stmt: LP (var_decl|stmt)* RP;

out_pointer: primitive_type LSB RSB;

stmt: if_stmt|while_stmt|for_stmt|break_stmt|continue_stmt|return_stmt|expr_stmt|block_stmt;

if_stmt: IF LB expr RB stmt (ELSE stmt)?;

while_stmt: DO stmt+ WHILE expr SM;

for_stmt: FOR LB expr SM expr SM expr RB stmt;

break_stmt: BREAK SM;

continue_stmt: CONTINUE SM;

return_stmt: RETURN expr? SM;

expr_stmt: expr SM;

func_call: ID LB (expr (CM expr)*)? RB;

expr: expr1 ASSIGN expr
    |expr1;
expr1: expr1 OR expr2
    |expr2;
expr2: expr2 AND expr3
    |expr3;
expr3: expr4 (EQUAL|NOT_EQUAL)expr4
    |expr4;
expr4: expr5 (LESS_THAN|LESS_EQUAL|GREATER_EQUAL|GREATER_THAN) expr5
    |expr5;
expr5: expr5 (ADD|SUB) expr6
    |expr6;
expr6: expr6 (DIV|MUL|MOD) expr7
    |expr7;
expr7: (SUB|NOT) expr7
    |expr8;
expr8: term LSB expr RSB|term;
term: BOOLLIT
    |FLOATLIT
    |INTLIT
    |STRINGLIT
    |ID
    |func_call
    |LB expr RB;

//boolean literal
BOOLLIT: TRUE|FALSE;
/*-----------------------KEYWORD------------------------*/
BOOLEAN: 'boolean';

BREAK: 'break';

CONTINUE: 'continue';

ELSE: 'else';

FOR: 'for';

FLOAT: 'float';

IF: 'if';

INT: 'int';

RETURN: 'return';

VOID: 'void';

DO: 'do';

WHILE: 'while';

TRUE: 'true';

FALSE: 'false';

STRING: 'string';

//integer literal
INTLIT: [0-9]+;

// floating-point literal
fragment EXPONENT: [eE]'-'?Number+;
FLOATLIT: Number*'.'Number+ EXPONENT?
    | Number+'.'?
    | Number+ EXPONENT;

//string literal
fragment ESC_LIT: '\\'[bfrnt'"\\];
STRINGLIT: '"'(~["\\]|ESC_LIT)*'"'{
        self.text = self.text[1:-1]};

/*---------------------------OPERATOR-----------------------------*/
ADD: '+';

MUL: '*';

NOT: '!';

OR: '||';

NOT_EQUAL: '!=';

LESS_THAN: '<';

LESS_EQUAL: '<=';

ASSIGN: '=';

SUB: '-';

DIV: '/';

MOD: '%';

AND: '&&';

EQUAL: '==';

GREATER_THAN: '>';

GREATER_EQUAL: '>=';

/*------------------------SEPARATORS------------------*/
LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SM: ';' ;

CM: ',';

LSB: '[';

RSB: ']';

fragment Letter: [a-zA-Z] ;

fragment Number: [0-9] ;

ID: (Letter|'_')(Letter|Number|'_')* ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
BLOCK_COMMENT: '/*'.*?'*/' -> skip;
LINE_COMMENT: '//' ~[\n]* -> skip;

ERROR_CHAR: . { raise ErrorToken(self.text)};
UNCLOSE_STRING: '"'(~["\\]|ESC_LIT)*{
    raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"'(~["\\]|ESC_LIT)*'\\'~[bfrnt'"\\]?{
    raise IllegalEscape(self.text[1:])
};