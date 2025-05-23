grammar CSVQueryDSL;

// Parser Rules
program: statement* EOF;

statement: loadStatement
         | filterStatement  
         | aggregateStatement
         | printStatement
         ;

loadStatement: 'load' STRING ';';

filterStatement: 'filter' 'column' STRING operator value logicalOp?;

aggregateStatement: 'aggregate' aggregateFunction 'column' STRING ';';

printStatement: 'print' ';';

operator: '>=' | '<=' | '>' | '<' | '==' | '!=';

logicalOp: 'AND' | 'OR';

aggregateFunction: 'COUNT' | 'SUM' | 'AVERAGE' | 'BETWEEN';

value: STRING | NUMBER | DATE;

// Lexer Rules
LOAD: 'load';
FILTER: 'filter';
AGGREGATE: 'aggregate';
PRINT: 'print';
COLUMN: 'column';
AND: 'AND';
OR: 'OR';

// Operators
GTE: '>=';
LTE: '<=';
GT: '>';
LT: '<';
EQ: '==';
NEQ: '!=';

// Aggregate Functions
COUNT: 'COUNT';
SUM: 'SUM';
AVERAGE: 'AVERAGE';
BETWEEN: 'BETWEEN';

// Literals
STRING: '"' (~["\r\n])* '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;
DATE: [0-9]{4} '-' [0-9]{2} '-' [0-9]{2};

// Symbols
SEMICOLON: ';';

// Whitespace and Comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
