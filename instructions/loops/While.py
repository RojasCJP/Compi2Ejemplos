from abstract.Instruction import *
from abstract.Return import *
from sym.Generator import *

class While(Instruction):

    def __init__(self, condition, instructions,line, column):
        Instruction.__init__(self, line, column)
        self.condition = condition
        self.instructions = instructions

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()

        continue_lbl = generator.new_label() # L1
        generator.put_label(continue_lbl) # ponemos el L1
        condition = self.condition.compile(env) # Retorna etiqueta V o F
        new_env = Environment(env) # nuevo entorno
        new_env.break_lbl = condition.false_lbl # L2 
        new_env.continue_lbl = continue_lbl # L1
        generator.put_label(condition.true_lbl) # L3
        self.instructions.compile(new_env) # bloque de codigo
        generator.add_goto(continue_lbl) # goto L1
        generator.put_label(condition.false_lbl) #  L2


