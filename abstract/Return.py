from enum import Enum

class Type(Enum):
    NULL = 0
    INT = 1
    FLOAT = 2
    BOOL = 3
    STRING = 4
    LIST = 5
    STRUCT = 6
    UNDEFINED = 7

    RETURN_ST = 8
    BREAK_ST = 9
    CONTINUE_ST = 10

class Return:
    def __init__(self, value, ret_type, is_temp, aux_type=''):
        self.value = value
        self.type = ret_type
        self.is_temp = is_temp
        self.struct_type = aux_type
        self.true_lbl = ''
        self.false_lbl = ''