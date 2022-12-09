from abstract.Return import *

class Symbol:

    def __init__(self, symbol_id, symbol_type, position, global_var, in_heap, struct_type='', pos_heap=False):
        self.id = symbol_id
        self.type = symbol_type
        self.pos = position
        self.is_global = global_var
        self.in_heap = in_heap
        self.struct_type = struct_type
        self.pos_heap = pos_heap
        self.value = None
