from abstract.Expression import *
from abstract.Return import *
from sym.Environment import *
from sym.Generator import *

class CallFunc(Expression):

    def __init__(self,id, params, line, column):
        Expression.__init__(self, line, column)
        self.id = id
        self.params = params

    def compile(self, env):
        try:
            func = env.get_func(self.id)
            if func is not None:
                param_values = []
                gen_aux = Generator()
                generator = gen_aux.get_instance()
                size = env.size
                for param in self.params:
                    param_values.append(param.compile(env))
                temp = generator.add_temp()
                generator.add_expression(temp, 'P', size+1, "+")
                aux = 0
                for param in param_values:
                    aux = aux + 1
                    generator.set_stack(temp. param.value)
                    if aux != len(param_values):
                        generator.add_expression(temp,temp,'1','+')
                generator.new_env(size)
                generator.call_fun(self.id)
                generator.get_stack(temp, 'P')
                generator.ret_env(size)
                return Return(temp, func.type, True)
            else:
                struct = env.get_struct(self.id)
                if struct is not None:
                    self.struct_type = self.id
                    gen_aux = Generator()
                    generator = gen_aux.get_instance()
                    return_temp = generator.add_temp()
                    generator.add_expression(return_temp, 'H', '','')
                    aux = generator.add_temp()
                    generator.add_expression(aux, return_temp,'','')
                    generator.add_expression('H','H',len(struct), '+')
                    for att in self.params:
                        value = att.compile(env)
                        if value.type != Type.BOOL:
                            generator.set_heap(aux, value.value)
                        else:
                            return_lbl = generator.new_label()
                            generator.put_label(value.true_lbl)
                            generator.set_heap(aux, '1')
                            generator.add_goto(return_lbl)
                            generator.put_label(value.false_lbl)
                            generator.set_heap(aux, '0')
                            generator.put_label(return_lbl)
                        generator.add_expression(aux, aux, '1', '+')
                    return Return(return_temp, Type.STRUCT, True, self.struct_type)

        except Exception as e:
            error = {}
            error["type"] = "function"
            error["text"] = "error en la llamada de funciones"
            Environment.errores.append(error)
            print("error en la llamada de funciones",e)

