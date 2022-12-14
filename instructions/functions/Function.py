from abstract.Instruction import *
from sym.Generator import *

class Function(Instruction):

    def __init__(self, id, params, type, instructions, line, column):
        Instruction.__init__(self, line, column)
        self.id = id 
        self.params = params
        self.type = type
        self.instructions = instructions

    def compile(self, env):
        env.save_func(self.id, self)
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        new_env = Environment(env)
        return_lbl = generator.new_label()
        new_env.return_lbl = return_lbl
        new_env.size = 1
        for param in self.params:
            new_env.save_var(param.id+"#", param.type, (param.type == Type.STRING or param.type == Type.STRUCT), param.struct_type)
        generator.add_begin_func(self.id) 
        try:
            self.instructions.compile(new_env)
        except Exception as e:
            print("error al compilar las instrucciones de una funcion", e)
        if self.type != Type.NULL:
            generator.put_label(return_lbl)
        generator.add_end_func()