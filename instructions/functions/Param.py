from abstract.Instruction import *

class Param(Instruction):

    def __init__(self, id, type, line, column, struct_type = ''):
        Instruction.__init__(self, line, column)
        self.id = id 
        self.type = type
        self.struct_type = struct_type


    def compile(self, env):
        return self