import ply.lex as lex
import ply.yacc as yacc
import sys

from sym.Environment import *
from abstract.Return import *

from instructions.nativas.Print import *
from instructions.variables.Declaration import *
from instructions.Statement import *
from instructions.functions.Function import *
from instructions.functions.Param import *
from instructions.functions.ReturnST import *
from instructions.loops.While import *
from instructions.loops.Break import *
from instructions.loops.Continue import *

from expressions.Literal import *
from expressions.Logical import *
from expressions.Relational import *
from expressions.Arithmetic import *
from expressions.Access import *
from expressions.CallFunc import *

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
    t[0] = t[1]

def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        | instruccion'''
    if (len(t) != 2):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]



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
                        | expression LINEANUEVA'''
    t[0] = t[1]



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
    if(len(t)==2):
        t[0] = t[1]
    elif (len(t)==3):
        if(t[1] == '-'):
            t[0] = Arithmetic(Literal(0,Type.INT, t.lineno(1), t.lexpos(0)),t[2],ArithmeticOption.MINUS,t.lineno(1), t.lexpos(0))
        else:
            t[0] = Logical(t[2],Literal(True, Type.BOOL, t.lineno(1), t.lexpos(0)),LogicOption.NOT, t.lineno(1), t.lexpos(0))
    else:
        if t[2] == "+":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.PLUS,
                              t.lineno(1), t.lexpos(0))
        elif t[2] == "-":
            t[0] = Arithmetic(
                t[1], t[3], ArithmeticOption.MINUS, t.lineno(1), t.lexpos(0))
        elif t[2] == "*":
            t[0] = Arithmetic(
                t[1], t[3], ArithmeticOption.TIMES, t.lineno(1), t.lexpos(0))
        elif t[2] == "/":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.DIV,
                              t.lineno(1), t.lexpos(0))
        elif t[2] == "^":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.RAISED,
                              t.lineno(1), t.lexpos(0))
        elif t[2] == "%":
            t[0] = Arithmetic(
                t[1], t[3], ArithmeticOption.MODULE, t.lineno(1), t.lexpos(0))
        elif t[2] == "or":
            t[0] = Logical(t[1], t[3], LogicOption.OR,
                           t.lineno(1), t.lexpos(0))
        elif t[2] == "and":
            t[0] = Logical(t[1], t[3], LogicOption.AND,
                           t.lineno(1), t.lexpos(0))
        elif t[2] == "<":
            t[0] = Relational(t[1], t[3], RelationalOption.LESS,
                              t.lineno(1), t.lexpos(0))
        elif t[2] == ">":
            t[0] = Relational(
                t[1], t[3], RelationalOption.GREATER, t.lineno(1), t.lexpos(0))
        elif t[2] == "<=":
            t[0] = Relational(
                t[1], t[3], RelationalOption.LESSEQUAL, t.lineno(1), t.lexpos(0))
        elif t[2] == ">=":
            t[0] = Relational(
                t[1], t[3], RelationalOption.GREATEREQUAL, t.lineno(1), t.lexpos(0))
        elif t[2] == "==":
            t[0] = Relational(t[1], t[3], RelationalOption.EQUAL,
                              t.lineno(1), t.lexpos(0))
        elif t[2] == "!=":
            t[0] = Relational(
                t[1], t[3], RelationalOption.DISTINCT, t.lineno(1), t.lexpos(0))


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
    if len(t) == 2:
        if t.slice[1].type == "ENTERO":
            t[0] = Literal(t[1], Type.INT, t.lineno(1), t.lexpos(0))
        if t.slice[1].type == "DECIMAL":
            t[0] = Literal(t[1], Type.FLOAT, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "FALSE":
            t[0] = Literal(False, Type.BOOL, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "TRUE":
            t[0] = Literal(True, Type.BOOL, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "CADENA":
            t[0] = Literal(str(t[1]), Type.STRING, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == 'ID':
            t[0] = Access(t[1], t.lineno(1), t.lexpos(0))
    else:
        if t.slice[1].type == "PARIZQ":
            t[0] = t[2]
        else:
            t[0] = Literal(t[2], Type.ARRAY, t.lineno(1), t.lexpos(0))

def p_nativas(t):
    '''nativas          : UPPER PARIZQ expression PARDER
                        | LOWER PARIZQ expression PARDER
                        | STR PARIZQ expression PARDER
                        | FLOAT PARIZQ expression PARDER
                        | LEN PARIZQ expression PARDER
                        '''

def p_print_instr(t):
    'print_instr    : PRINT PARIZQ exp_list PARDER'
    t[0] = Print(t[3], t.lineno(1), t.lexpos(0), False)

def p_println_instr(t):
    'println_instr  : PRINTLN PARIZQ exp_list PARDER'
    t[0] = Print(t[3], t.lineno(1), t.lexpos(0), True)

def p_tipo(t):
    '''tipo     : INT
                | FLOAT
                | BOOL
                | STR
                | NONE
    '''

def p_asignacion_instr(t):
    '''asignacion_instr     : ID IGUAL expression'''
    t[0] = Declaration(t[1], t[3], t.lineno(1), t.lexpos(0))

def p_definicion_asignacion_instr(t):
    '''definicion_asignacion_instr  : ID  DOSP tipo IGUAL expression'''
    t[0] = Declaration(t[1], t[5], t.lineno(1), t.lexpos(0))

def p_asignacion_arreglo_instr(t):
    '''asignacion_arreglo_instr     : ID index_list IGUAL expression'''

def p_call_function_instr(t):
    '''call_function    : ID PARIZQ PARDER
                        | ID PARIZQ exp_list PARDER'''
    if len(t) == 4:
        t[0] = CallFunc(t[1], [], t.lineno(1), t.lexpos(0))
    else:
        t[0] = CallFunc(t[1], t[3], t.lineno(1), t.lexpos(0))

def p_exp_list_instr(t):
    '''exp_list         : exp_list COMA expression
                        | expression'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]
    
def p_index_list_instr(t):
    '''index_list       : index_list CORCHETEIZQ expression CORCHETEDER
                        | CORCHETEIZQ expression CORCHETEDER'''

def p_statement(t):
    '''statement        : instrucciones'''
    t[0] = Statement(t[1], t.lineno(1), t.lexpos(0))

def p_declare_function(t):
    '''declare_function     : DEF ID PARIZQ dec_params PARDER DOSP statement END
                            | DEF ID PARIZQ PARDER DOSP statement END'''
    if len(t) == 8:
        t[0] = Function(t[2], [], Type.NULL, t[6], t.lineno(1), t.lexpos(0))
    else:
        t[0] = Function(t[2], t[4], Type.NULL, t[7], t.lineno(1), t.lexpos(0))

def p_dec_params(t):
    '''dec_params :   dec_params COMA ID DOSP tipo
                    | dec_params COMA ID
                    | ID DOSP tipo
                    | ID'''
    if len(t) == 2:
        t[0] = [Param(t[1],Type.LIST,t.lineno(1), t.lexpos(0))]
    elif len(t) == 4:
        if(t.slice[1].type == 'ID'):
            t[0] = [Param(t[1],t[3],t.lineno(1), t.lexpos(0))]
        else:
            t[0] = t[1].append(Param(t[3],Type.LIST,t.lineno(1), t.lexpos(0)))
    else:
        t[0] = t[1].append(Param(t[3],t[5],t.lineno(1), t.lexpos(0)))

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
    t[0] = While(t[2], t[4], t.lineno(1), t.lexpos(0))

def p_for_state(t):
    '''for_state        : FOR ID IN expression DOSP expression DOSP statement END
                        | FOR ID IN expression DOSP statement END'''
                    
def p_break(t):
    '''break_state      : BREAK'''
    t[0] = Break(t.lineno(1), t.lexpos(0))

def p_continue(t):
    '''continue_state      : CONTINUE'''
    t[0] = Continue(t.lineno(1), t.lexpos(0))

def p_return(t):
    '''return_state     : RETURN
                        | RETURN expression'''
    if(len(t) == 2):
        t[0] = ReturnSt(None, t.lineno(1), t.lexpos(0))
    else:
        t[0] = ReturnSt(t[2], t.lineno(1), t.lexpos(0))

parser = yacc.yacc()

def parse(input):
    return parser.parse(input, lexer=lexer)


