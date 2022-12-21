import ast
import ply.lex as lex
import ply.yacc as yacc
import decimal

tokens = (
    'DEF',
    'IF',
    'NAME',
    'NUMBER',
    'STRING',
    'LPAR',
    'RPAR',
    'COLON',
    'EQ',
    'ASSIGN',
    'LT',
    'GT',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'RETURN',
    'WS',
    'NEWLINE',
    'COMMA',
    'SEMICOLON',
    'INDENT',
    'DEDENT',
    'ENDMARKER'
)

def t_NUMBER(t):
    r"""(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?"""
    t.value = decimal.Decimal(t.value)
    if t.value == int(t.value):
        t.value = int(t.value)
    else:
        t.value = float(t.value)
    return t

def t_STRING(t):
    r"'([^\\']+|\\'|\\\\)*'"  # I think this is right ...
    t.value = t.value[1:-1].encode().decode("unicode_escape")  # .swapcase() # for fun
    return t

t_COLON = r':'
t_EQ = r'=='
t_ASSIGN = r'='
t_LT = r'<'
t_GT = r'>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_COMMA = r','
t_SEMICOLON = r';'

RESERVED = {
    "def": "DEF",
    "if": "IF",
    "return": "RETURN",
}

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = RESERVED.get(t.value, "NAME")
    return t

def t_comment(t):
    r"[ ]*\043[^\n]*"  # \043 is '#'
    pass

def t_WS(t):
    r'[ ]+'
    if t.lexer.at_line_start and t.lexer.paren_count == 0:
        return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = "NEWLINE"
    if t.lexer.paren_count == 0:
        return t

def t_LPAR(t):
    r'\('
    t.lexer.paren_count += 1
    return t


def t_RPAR(t):
    r'\)'
    # check for underflow?  should be the job of the parser
    t.lexer.paren_count -= 1
    return t


def t_error(t):
    raise SyntaxError("Unknown symbol %r" % (t.value[0],))
    print("Skipping", repr(t.value[0]))
    t.lexer.skip(1)

NO_INDENT = 0
MAY_INDENT = 1
MUST_INDENT = 2

def track_tokens_filter(lexer, tokens):
    lexer.at_line_start = at_line_start = True
    indent = NO_INDENT
    saw_colon = False
    for token in tokens:
        token.at_line_start = at_line_start

        if token.type == "COLON":
            at_line_start = False
            indent = MAY_INDENT
            token.must_indent = False

        elif token.type == "NEWLINE":
            at_line_start = True
            if indent == MAY_INDENT:
                indent = MUST_INDENT
            token.must_indent = False

        elif token.type == "WS":
            assert token.at_line_start == True
            at_line_start = True
            token.must_indent = False

        else:
            # A real token; only indent after COLON NEWLINE
            if indent == MUST_INDENT:
                token.must_indent = True
            else:
                token.must_indent = False
            at_line_start = False
            indent = NO_INDENT

        yield token
        lexer.at_line_start = at_line_start

def _new_token(type, lineno):
    tok = lex.LexToken()
    tok.type = type
    tok.value = None
    tok.lineno = lineno
    tok.lexpos = 0
    return tok

def DEDENT(lineno):
    return _new_token("DEDENT", lineno)

def INDENT(lineno):
    return _new_token("INDENT", lineno)

# Track the indentation level and emit the right INDENT / DEDENT events.
def indentation_filter(tokens):
    # A stack of indentation levels; will never pop item 0
    levels = [0]
    token = None
    depth = 0
    prev_was_ws = False
    for token in tokens:
        # if 1:
        # print "Process", token,
        # if token.at_line_start:
        # print "at_line_start",
        # if token.must_indent:
        # print "must_indent",
        # print

        # WS only occurs at the start of the line
        # There may be WS followed by NEWLINE so
        # only track the depth here.  Don't indent/dedent
        # until there's something real.
        if token.type == "WS":
            assert depth == 0
            depth = len(token.value)
            prev_was_ws = True
            # WS tokens are never passed to the parser
            continue

        if token.type == "NEWLINE":
            depth = 0
            if prev_was_ws or token.at_line_start:
                # ignore blank lines
                continue
            # pass the other cases on through
            yield token
            continue

        # then it must be a real token (not WS, not NEWLINE)
        # which can affect the indentation level

        prev_was_ws = False
        if token.must_indent:
            # The current depth must be larger than the previous level
            if not (depth > levels[-1]):
                raise IndentationError("expected an indented block")

            levels.append(depth)
            yield INDENT(token.lineno)

        elif token.at_line_start:
            # Must be on the same level or one of the previous levels
            if depth == levels[-1]:
                # At the same level
                pass
            elif depth > levels[-1]:
                raise IndentationError(
                    "indentation increase but not in new block")
            else:
                # Back up; but only if it matches a previous level
                try:
                    i = levels.index(depth)
                except ValueError:
                    raise IndentationError("inconsistent indentation")
                for _ in range(i + 1, len(levels)):
                    yield DEDENT(token.lineno)
                    levels.pop()

        yield token
         ### Finished processing ###

    # Must dedent any remaining levels
    if len(levels) > 1:
        assert token is not None
        for _ in range(1, len(levels)):
            yield DEDENT(token.lineno)


def filter(lexer, add_endmarker=True):
    token = None
    tokens = iter(lexer.token, None)
    tokens = track_tokens_filter(lexer, tokens)
    for token in indentation_filter(tokens):
        yield token

    if add_endmarker:
        lineno = 1
        if token is not None:
            lineno = token.lineno
        yield _new_token("ENDMARKER", lineno)

class IndentLexer(object):

    def __init__(self, debug=0, reflags=0):
        self.lexer = lex.lex(debug=debug, reflags=reflags)
        self.token_stream = None

    def input(self, s, add_endmarker=True):
        self.lexer.paren_count = 0
        self.lexer.input(s)
        self.token_stream = filter(self.lexer, add_endmarker)

    def token(self):
        try:
            return next(self.token_stream)
        except StopIteration:
            return None




def Assign(left, right):
    names = []
    if isinstance(left, ast.Name):
        # Single assignment on left
        return ast.Assign([ast.Name(left.id, ctx=ast.Store())], right)
    elif isinstance(left, ast.Tuple):
        # List of things - make sure they are Name nodes
        names = []
        for child in left.elts:
            if not isinstance(child, ast.Name):
                raise SyntaxError("that assignment not supported")
            names.append(child.id)
        ass_list = [ast.Name(name, ctx=ast.Store()) for name in names]
        return ast.Assign([ast.Tuple(ass_list, ctx=ast.Store())], right)
    else:
        raise SyntaxError("Can't do that yet")


def p_file_input_end(p):
    """file_input_end : file_input ENDMARKER"""
    p[0] = p[1]

def p_file_input(p):
    """file_input : file_input NEWLINE
                  | file_input stmt
                  | NEWLINE
                  | stmt"""
    if isinstance(p[len(p) - 1], str):
        if len(p) == 3:
            p[0] = p[1]
        else:
            p[0] = []  # p == 2 --> only a blank line
    else:
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

def p_funcdef(p):
    "funcdef : DEF NAME parameters COLON suite"
    p[0] = ast.FunctionDef(p[2], args=ast.arguments([ast.arg(x, None) for x in p[3]], None, [], [], None, []), body=p[5], decorator_list=[], returns=None)

def p_parameters(p):
    """parameters : LPAR RPAR
                  | LPAR varargslist RPAR"""
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]

def p_varargslist(p):
    """varargslist : varargslist COMMA NAME
                   | NAME"""
    if len(p) == 4:
        p[0] = p[1] + p[3]
    else:
        p[0] = [p[1]]

def p_stmt_simple(p):
    """stmt : simple_stmt"""
    # simple_stmt is a list
    p[0] = p[1]

def p_stmt_compound(p):
    """stmt : compound_stmt"""
    p[0] = [p[1]]

def p_simple_stmt(p):
    """simple_stmt : small_stmts NEWLINE
                   | small_stmts SEMICOLON NEWLINE"""
    p[0] = p[1]

def p_small_stmts(p):
    """small_stmts : small_stmts SEMICOLON small_stmt
                   | small_stmt"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_small_stmt(p):
    """small_stmt : flow_stmt
                  | expr_stmt"""
    p[0] = p[1]

def p_expr_stmt(p):
    """expr_stmt : testlist ASSIGN testlist
                 | testlist """
    if len(p) == 2:
        # a list of expressions
        p[0] = ast.Expr(p[1])
    else:
        p[0] = Assign(p[1], p[3])

def p_flow_stmt(p):
    "flow_stmt : return_stmt"
    p[0] = p[1]

def p_return_stmt(p):
    "return_stmt : RETURN testlist"
    p[0] = ast.Return(p[2])

def p_compound_stmt(p):
    """compound_stmt : if_stmt
                     | funcdef"""
    p[0] = p[1]

def p_if_stmt(p):
    'if_stmt : IF test COLON suite'
    p[0] = ast.If(p[2], p[4], [])

def p_suite(p):
    """suite : simple_stmt
             | NEWLINE INDENT stmts DEDENT"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[3]

def p_stmts(p):
    """stmts : stmts stmt
             | stmt"""
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

binary_ops = {
    "+": ast.Add,
    "-": ast.Sub,
    "*": ast.Mult,
    "/": ast.Div,
}
compare_ops = {
    "<": ast.Lt,
    ">": ast.Gt,
    "==": ast.Eq,
}
unary_ops = {
    "+": ast.UAdd,
    "-": ast.USub,
}
precedence = (
    ("left", "EQ", "GT", "LT"),
    ("left", "PLUS", "MINUS"),
    ("left", "MULT", "DIV"),
)


def p_comparison(p):
    """comparison : comparison PLUS comparison
                  | comparison MINUS comparison
                  | comparison MULT comparison
                  | comparison DIV comparison
                  | comparison LT comparison
                  | comparison EQ comparison
                  | comparison GT comparison
                  | PLUS comparison
                  | MINUS comparison
                  | power"""
    if len(p) == 4:
        if p[2] in binary_ops:
            p[0] = ast.BinOp(p[1], binary_ops[p[2]](), p[3])
        else:
            p[0] = ast.Compare(p[1], [compare_ops[p[2]]()], [p[3]])
    elif len(p) == 3:
        p[0] = ast.UnaryOp(unary_ops[p[1]](), p[2])
    else:
        p[0] = p[1]

def p_power(p):
    """power : atom
             | atom trailer"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2][0] == "CALL":
            p[0] = ast.Call(p[1], p[2][1], [])
        else:
            raise AssertionError("not implemented")


def p_atom_name(p):
    """atom : NAME"""
    p[0] = ast.Name(p[1],ctx=ast.Load())


def p_atom_number(p):
    """atom : NUMBER"""
    p[0] = ast.Num(p[1])

def p_atom_string(p):
    """atom : STRING"""
    p[0] = ast.Str(p[1])

def p_atom_tuple(p):
    """atom : LPAR testlist RPAR"""
    p[0] = p[2]

def p_trailer(p):
    "trailer : LPAR arglist RPAR"
    p[0] = ("CALL", p[2])

def p_testlist(p):
    """testlist : testlist_multi COMMA
                | testlist_multi """
    if len(p) == 2:
        p[0] = p[1]
    else:
        # May need to promote singleton to tuple
        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]
    # Convert into a tuple?
    if isinstance(p[0], list):
        p[0] = ast.Tuple(p[0], ctx=ast.Load())


def p_testlist_multi(p):
    """testlist_multi : testlist_multi COMMA test
                      | test"""
    if len(p) == 2:
        # singleton
        p[0] = p[1]
    else:
        if isinstance(p[1], list):
            p[0] = p[1] + [p[3]]
        else:
            # singleton -> tuple
            p[0] = [p[1], p[3]]

def p_test(p):
    "test : comparison"
    p[0] = p[1]

def p_arglist(p):
    """arglist : arglist COMMA argument
               | argument"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_argument(p):
    "argument : test"
    p[0] = p[1]


def p_error(p):
    # print "Error!", repr(p)
    raise SyntaxError(p)



lexer = IndentLexer()
parser = yacc.yacc()

def parse(input):
    return parser.parse(input, lexer=lexer)


s = ''
with open('tabulaciones.txt', 'r') as f:
    contenido = f.readlines()
    for element in contenido:
        s += element
arbol = parse(s)
print(arbol)

from platform import python_version
print(python_version())
