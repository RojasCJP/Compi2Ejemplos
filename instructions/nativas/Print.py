import uuid
from abstract.Instruction import *
from abstract.Return import *
from sym.Generator import *


class Print(Instruction):
    printlist = ''

    def __init__(self, value, line, column, new_line=False):
        Instruction.__init__(self, line, column)
        self.value = value
        self.new_line = new_line

    def compile(self, env):
        # val = self.value.compile(env)
        gen_aux = Generator()
        generator = gen_aux.get_instance()

        for values in self.value:
            valuee = values.compile(env)
            if valuee.type == Type.INT:
                generator.add_print("d", valuee.value)
            elif valuee.type == Type.FLOAT:
                generator.print_float("f", valuee.value)
            elif valuee.type == Type.CHAR:
                generator.add_print('c', valuee.value)
            elif valuee.type == Type.BOOL:
                temp_lbl = generator.new_label()
                generator.put_label(valuee.true_lbl)
                generator.print_true()
                generator.add_goto(temp_lbl)
                generator.put_label(valuee.false_lbl)
                generator.print_false()
                generator.put_label(temp_lbl)
            elif valuee.type == Type.STRING:
                generator.fprint_string()
                param_temp = generator.add_temp()
                generator.add_expression(param_temp, 'P', env.size, '+')
                generator.add_expression(param_temp, param_temp, '1', '+')
                generator.set_stack(param_temp, valuee.value)
                generator.new_env(env.size)
                generator.call_fun('print_string')
                temp = generator.add_temp()
                generator.get_stack(temp, 'P')
                generator.ret_env(env.size)
            elif valuee.type == Type.ARRAY:
                generator.add_expression('P', 'P', env.size, '+')
                generator.fprint_array()
                generator.add_expression('P', 'P', env.size, '-')
                param_temp = generator.add_temp()
                generator.add_expression(param_temp, 'P', env.size, '+')
                generator.add_expression(param_temp, param_temp, '1', '+')
                generator.set_stack(param_temp, valuee.value)
                generator.new_env(env.size)
                generator.call_fun('print_array')
                temp = generator.add_temp()
                generator.get_stack(temp, 'P')
                generator.ret_env(env.size)
            else:
                print("falta")
            generator.add_print("c", 32)
        if self.new_line:
            generator.add_print("c", 10)