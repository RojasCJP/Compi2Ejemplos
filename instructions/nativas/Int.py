from abstract.Instruction import *
from abstract.Return import *
from sym.Generator import *

class Int(Instruction):

    def __init__(self, line, column, value):
        Instruction.__init__(self, line, column)
        self.value = value
        
    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        value = self.value.compile(env)
        temp = generator.add_temp()
        temp_aux = generator.add_temp()
        generator.add_expression(temp, value.value, '','')
        generator.add_module(temp_aux, temp, '1')
        generator.add_expression(temp, temp, temp_aux, '-')
        return Return(temp, Type.INT, True)