grammar Simple;

prog: classDef+ ;

classDef
    : 'class' ID '{' member+ '}' 
    ;

member
    : 'int' ID ';'
    | 'int' ID '(' paramList? ')' '{' stat* '}' 
    ;

paramList
    : ID (',' ID)*
    ;

stat
    : expr ';'
    | ID '=' expr ';'
    ;

expr
    : expr op=('*'|'/') expr       # MulDiv
    | expr op=('+'|'-') expr       # AddSub
    | INT                          # Int
    | ID                           # Id
    | ID '(' INT ')'               # Call
    | '(' expr ')'                 # Parens
    ;

INT : [0-9]+ ;
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
WS  : [ \t\r\n]+ -> skip ;
