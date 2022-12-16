from abstract.Instruction import *
from abstract.Return import *
from sym.Generator import *

class Len(Instruction):

    def __init__(self, line, column, array):
        Instruction.__init__(self, line, column)
        self.array = array

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        generator.add_comment("compilacion de len (obtener la longitud de un arreglo o string)")
        array = self.array.compile(env)
        if array is None:
            print("arreglo inexistente")
            return
        temp = generator.add_temp()
        generator.add_expression(temp, array.value, '','')
        generator.get_heap(temp,temp)
        return Return(temp, Type.INT, True)

