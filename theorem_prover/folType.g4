grammar folType;

/*------------------------------------------------------------------
 * PARSER RULES
 *------------------------------------------------------------------*/

init
: declaration (NL declaration?)* EOF
;

declaration
: PREPOSITION ':' predicateType
;

predicateType
: (sort ('x' sort)* '->')? BOOL
;

PREPOSITION
: ('A' .. 'Z') CHARACTER*
;

sort
: INT
| BOOL
| TYPE
;

INT
: '_INT'
;

BOOL
: '_Bool'
;

TYPE
: '_' CHARACTER*
;

SEP
: ','
;

fragment CHARACTER
: ('0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '_')
;

NL
: ('\r'? '\n')
;

WS
: (' ' | '\t') + -> skip
;
