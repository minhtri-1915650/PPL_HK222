//1915650
// Ho Minh Tri

grammar MT22;

@lexer::header {
from lexererr import *

}

options{
	language=Python3;
}
/*------------------------Parser-----------------------*/
program: decls EOF;

decls: decl decls | decl;
decl: vardecl | fundecl;

vardecl: shortform | initial;

shortform: idlist CL vartype SEMI;
idlist: ID CM idlist | ID;
vartype: atomictype | arraytype | AUTO;

initial: ID initialbody expr SEMI;
initialbody: CM ID initialbody expr CM | CL vartype ASSIGN;

fundecl: ID CL FUNCTION funtype LB paramlist RB isinherit body;
funtype: vartype | VOID;
paramlist: params |; 
params: param CM params | param; 
param: INHERIT? OUT? ID CL vartype;
isinherit: INHERIT ID |;

body: blockstmt;
blockstmt: LCP blockbody RCP;
blockbody: stmtlist blockbody | ;
stmtlist: stmt | vardecl;
stmt: assignstmt | ifstmt | forstmt | whilestmt | dowhilestmt 
	| breakstmt | continuestmt | returnstmt | callstmt | blockstmt;

assignstmt: lhs ASSIGN expr SEMI;
lhs: ID | indexop;

ifstmt: matchstmt | unmatchstmt;
matchstmt: IF LB expr RB matchstmt ELSE matchstmt | other;
unmatchstmt: IF LB expr RB ifstmt | IF LB expr RB matchstmt ELSE unmatchstmt;
other: assignstmt | forstmt | whilestmt | dowhilestmt 
	| breakstmt | continuestmt | returnstmt | callstmt | blockstmt;

forstmt: FOR LB lhs ASSIGN expr CM expr CM expr RB stmt;

whilestmt: WHILE LB expr RB stmt;
dowhilestmt: DO blockstmt WHILE LB expr RB SEMI;
breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
returnstmt: RETURN expr? SEMI;
callstmt: funcall SEMI;

atomictype: BOOLEAN | INTEGER | FLOAT | STRING;
arraytype: ARRAY LSP dimensions RSP OF atomictype;
dimensions: INTLIT CM dimensions | INTLIT;

expr: expr1 CONC expr1 | expr1;
expr1: expr2 EQUAL expr2 | expr2 NEQUAL expr2 
	| expr2 SMALL expr2 | expr2 LARGE expr2
	| expr2 SMALLEQ expr2 | expr2 LARGEEQ expr2 | expr2;
expr2: expr2 AND expr3 | expr2 OR expr3 | expr3;
expr3: expr3 ADDOP expr4 | expr3 SUBOP expr4 | expr4;
expr4: expr4 MULOP expr5 | expr4 DIVOP expr5 | expr4 MODOP expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUBOP expr6 | expr7;
expr7: ID | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT 
	| indexop | funcall | arraylit
	| LB expr RB;

indexop: ID LSP exprs RSP;
funcall: ID LB exprlist RB;

exprlist: exprs |;
exprs: expr CM exprs | expr;
arraylit: LCP exprlist RCP;

/*---------------------------Lexer-------------------------------*/
//Seperators
LB: '('; RB: ')'; LSP: '['; RSP: ']'; 
DOT: '.'; CM: ','; SEMI: ';' ; CL: ':';
LCP: '{'; RCP: '}'; ASSIGN: '=';

//Operators
ADDOP: '+'; SUBOP: '-'; MULOP: '*'; DIVOP: '/'; MODOP: '%';
NOT: '!'; AND: '&&'; OR: '||'; EQUAL: '==';
NEQUAL: '!='; SMALL: '<'; SMALLEQ: '<='; LARGE: '>'; LARGEEQ: '>=';
CONC: '::';  

//Keywords
AUTO: 'auto'; BREAK: 'break'; BOOLEAN: 'boolean'; DO: 'do'; ELSE: 'else';
FLOAT: 'float'; FOR: 'for'; FUNCTION: 'function'; IF: 'if';
INTEGER: 'integer'; RETURN: 'return'; STRING: 'string'; WHILE: 'while';
VOID: 'void'; OUT: 'out'; CONTINUE: 'continue'; OF: 'of'; INHERIT: 'inherit';
ARRAY: 'array';
fragment TRUE: 'true'; fragment FALSE: 'false';

//Literals
INTLIT: '0' | [1-9] ('_' [0-9] | [0-9])* {self.text = self.text.replace("_", "")};
FLOATLIT: INTLIT DECPART EXPONENT? {self.text = self.text.replace("_", "")}
		| INTLIT EXPONENT {self.text = self.text.replace("_", "")}
		| DECPART EXPONENT; 
fragment DECPART: DOT [0-9]*;
fragment EXPONENT: [eE] [+-]? [0-9]+;
BOOLLIT: TRUE | FALSE; 
STRINGLIT: '"' (~["\\\r\n] | '\\' [tbfrn\\'"])* '"' {self.text = self.text[1:-1]};

//Identifiers
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

//Comments
CCOMMENT: '/*' .*? '*/' -> skip; //C-style comment 
CPPCOMMENT: '//' ~[\r\n]* -> skip; //C++ style comment

WS : [ \t\b\f\r\n]+ -> skip ;
// skip spaces, tabs, backspace, form feed, carriage return, newlines 

UNCLOSE_STRING: '"' (~["\\\r\n] | '\\' [tbfrn\\'"])* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' (~["\\\r\n] | '\\' [tbfrn\\'"])* '\\' ~[tbfrn\\'"] {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};