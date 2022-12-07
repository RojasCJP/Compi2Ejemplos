import ply.lex as lex
import ply.yacc as yacc
import sys

reservadas = {
    "println" : "PRINTLN",
    "print": "PRINT",
    "while": "WHILE",
    "for": "FOR",
    "if": "IF",
    "in": "IN",
    "elif": "ELIF",
    "else": "ELSE",
    "None": "NONE",
    "or" : "OR",
    "and" : "AND",
    "not" : "NOT",
    "int": "INT",
    "float": "FLOAT",
    "bool": "BOOL",
    "str": "STR",
    "upper": "UPPER",
    "lower": "LOWER",
    "len": "LEN",
    "def": "DEF",
    "break": "BREAK",
    "continue": "CONTINUE",
    "return": "RETURN",
    "end": "END",
    "True": "TRUE",
    "False": "FALSE"
}

tokens = [
    "LINEANUEVA",
    "DOSP",
    "PUNTO",
    "COMA",
    "LLAVIZQ",
    "LLAVDER",
    "CORCHETEIZQ",
    "CORCHETEDER",
    "PARIZQ",
    "PARDER",
    "IGUAL",
    "MAS",
    "MENOS",
    "POR",
    "DIVIDIDO",
    "POTENCIA",
    "MODULO",
    "MENQUE",
    "MENIGUALQUE",
    "MAYQUE",
    "MAYIGUALQUE",
    "IGUALQUE",
    "NIGUALQUE",
    "DECIMAL",
    "ENTERO",
    "CADENA",
    "ID"
] + list(reservadas.values())

# Tokens
t_LINEANUEVA = r'\n'
t_DOSP = r':'
t_PUNTO = r'\.'
t_COMA = r','
t_LLAVIZQ = r'{'
t_LLAVDER = r'}'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r']'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_POTENCIA = r'\^'
t_MODULO = r'%'
t_MENQUE = r'<'
t_MENIGUALQUE = r'<='
t_MAYQUE = r'>'
t_MAYIGUALQUE = r'>='
t_IGUALQUE = r'=='
t_NIGUALQUE = r'!='
t_IGUAL = r'='

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reservadas.get(t.value, 'ID')
    return t


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t

# Comentario de múltiples líneas #= .. =#


def t_COMENTARIO_MULTILINEA(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple # ...


def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"

def t_error(t):
    print("Error!!!!!")
    t.lexer.skip(1)

lexer = lex.lex()

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUALQUE', 'NIGUALQUE'),
    ('left', 'MAYQUE', 'MENQUE', 'MAYIGUALQUE', 'MENIGUALQUE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MODULO'),
    ('left', 'POTENCIA'),
    ('right', 'UMENOS')
)



def p_init(t):
    '''init            : instrucciones'''

def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        | instruccion'''

def p_instruccion(t):
    '''instruccion      : print_instr LINEANUEVA
                        | println_instr LINEANUEVA
                        | asignacion_instr LINEANUEVA
                        | asignacion_arreglo_instr LINEANUEVA
                        | definicion_asignacion_instr LINEANUEVA
                        | call_function LINEANUEVA
                        | declare_function LINEANUEVA
                        | return_state LINEANUEVA
                        | break_state LINEANUEVA
                        | continue_state LINEANUEVA
                        | if_state LINEANUEVA
                        | while_state LINEANUEVA
                        | for_state LINEANUEVA
                        | nativas LINEANUEVA
'''


def p_expression(t):
    '''expression       : MENOS expression %prec UMENOS
                        | NOT expression %prec UMENOS
                        | expression MAS expression
                        | expression MENOS expression
                        | expression POR expression
                        | expression DIVIDIDO expression
                        | expression POTENCIA expression
                        | expression MODULO expression
                        | expression MAYQUE expression
                        | expression MENQUE expression
                        | expression MENIGUALQUE expression
                        | expression MAYIGUALQUE expression
                        | expression IGUALQUE expression
                        | expression NIGUALQUE expression
                        | expression OR expression
                        | expression AND expression
                        | final_expression'''

def p_final_expression(t):
    '''final_expression     : PARIZQ expression PARDER
                            | CORCHETEIZQ exp_list CORCHETEDER
                            | DECIMAL
                            | ENTERO
                            | CADENA
                            | ID
                            | ID index_list  
                            | TRUE
                            | FALSE
                            | call_function
                            | nativas'''

def p_nativas(t):
    '''nativas          : UPPER PARIZQ expression PARDER
                        | LOWER PARIZQ expression PARDER
                        | STR PARIZQ expression PARDER
                        | FLOAT PARIZQ expression PARDER
                        | LEN PARIZQ expression PARDER
                        '''

def p_print_instr(t):
    'print_instr    : PRINT PARIZQ exp_list PARDER'

def p_println_instr(t):
    'println_instr  : PRINTLN PARIZQ exp_list PARDER'

def p_tipo(t):
    '''tipo     : INT
                | FLOAT
                | BOOL
                | STR
                | NONE
    '''

def p_asignacion_instr(t):
    '''asignacion_instr     : ID IGUAL expression'''

def p_definicion_asignacion_instr(t):
    '''definicion_asignacion_instr  : ID  DOSP tipo IGUAL expression'''

def p_asignacion_arreglo_instr(t):
    '''asignacion_arreglo_instr     : ID index_list IGUAL expression'''

def p_call_function_instr(t):
    '''call_function    : ID PARIZQ PARDER
                        | ID PARIZQ exp_list PARDER'''

def p_exp_list_instr(t):
    '''exp_list         : exp_list COMA expression
                        | expression'''

def p_index_list_instr(t):
    '''index_list       : index_list CORCHETEIZQ expression CORCHETEDER
                        | CORCHETEIZQ expression CORCHETEDER'''

def p_statement(t):
    '''statement        : instrucciones'''

def p_declare_function(t):
    '''declare_function     : DEF ID PARIZQ dec_params PARDER DOSP statement END
                            | DEF ID PARIZQ PARDER DOSP statement END'''

def p_dec_params(t):
    '''dec_params :   dec_params COMA ID DOSP tipo
                    | dec_params COMA ID
                    | ID DOSP tipo
                    | ID'''

def p_if_state(t):
    '''if_state     : IF expression DOSP statement END
                    | IF expression DOSP statement ELSE DOSP statement END
                    | IF expression DOSP statement else_if_list END'''
    

def p_else_if_list(t):
    '''else_if_list     : ELIF expression DOSP statement
                        | ELIF expression DOSP statement ELSE statement
                        | ELIF expression DOSP statement else_if_list'''

def p_while_state(t):
    '''while_state      : WHILE expression DOSP statement END'''

def p_for_state(t):
    '''for_state        : FOR ID IN expression DOSP expression DOSP statement END
                        | FOR ID IN expression DOSP statement END'''
                    
def p_break(t):
    '''break_state      : BREAK'''

def p_continue(t):
    '''continue_state      : CONTINUE'''

def p_return(t):
    '''return_state     : RETURN
                        | RETURN expression'''

parser = yacc.yacc()
s = ''
with open('tabulaciones.txt', 'r') as f:
    contenido = f.readlines()
    for element in contenido:
        s += element
parser.parse(s)


