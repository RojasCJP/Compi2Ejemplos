import uuid
from abstract.Instruction import *
from abstract.Return import *
from sym.Generator import *

class ToLower(Instruction):

    def __init__(self, value, line, column):
        Instruction.__init__(self, line, column)
        self.value = value

    def compile(self, env):
        val = self.value.compile(env)
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        generator.f_to_lower()
        param_temp = generator.add_temp()
        generator.add_expression(param_temp, 'P', env.size, '+')
        generator.add_expression(param_temp, param_temp, '1', '+')
        generator.set_stack(param_temp, val.value)
        generator.new_env(env.size)
        generator.call_fun("to_lower")
        temp1 = generator.add_temp()
        temp2 = generator.add_temp()
        generator.add_expression(temp2, 'P', 1, '+')
        generator.get_stack(temp1, temp2)
        return Return(temp1, Type.STRING, True)