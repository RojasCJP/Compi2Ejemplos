from abstract.Instruction import *
from abstract.Return import *
from sym.Generator import *


class Break(Instruction):

    def __init__(self, line, column):
        Instruction.__init__(self,line,column)

    def compile(self, env):
        if env.break_lbl == '':
            print('break fuera de ciclo')
            return
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        generator.add_goto(env.break_lbl)
