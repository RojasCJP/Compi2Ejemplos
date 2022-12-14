from abstract.Expression import *
from abstract.Return import * 
from sym.Generator import * 

class ReturnSt(Expression):

    def __init__(self, expr, line, column):
        Expression.__init__(self, line, column)
        self.expr = expr

    def compile(self, env):
        if(env.return_lbl == ''):
            print('retorno fuera de una funcion')
            return
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        value = self.expr.compile(env)
        if (value.type == Type.BOOL):
            temp_lbl = generator.new_label()
            generator.put_label(value.true_lbl)
            generator.set_stack('P', '1')
            generator.add_goto(temp_lbl)
            generator.put_label(value.false_lbl)
            generator.set_stack('P', '0')
            generator.put_label(temp_lbl)
        else:
            generator.set_stack('P', value.value)
        generator.add_goto(env.return_lbl)
