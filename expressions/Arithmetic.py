from abstract.Expression import *
from abstract.Return import *
from sym.Generator import *
from enum import Enum
import uuid


class ArithmeticOption(Enum):
    PLUS = 0
    MINUS = 1
    TIMES = 2
    DIV = 3
    RAISED = 4
    MODULE = 5


class Arithmetic(Expression):
    def __init__(self, left, right, type, line, column):
        Expression.__init__(self, line, column)
        self.left = left
        self.right = right
        self.type = type

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        left_value = self.left.compile(env)
        right_value = self.right.compile(env)

        temp = generator.add_temp()
        op = ''
        if self.type == ArithmeticOption.PLUS:
            op = '+'
        elif self.type == ArithmeticOption.MINUS:
            op = '-'
        elif self.type == ArithmeticOption.TIMES:
            op = '*'
        elif self.type == ArithmeticOption.DIV:
            op = '/'
        elif self.type == ArithmeticOption.MODULE:
            op = '%'

        if (self.type == ArithmeticOption.RAISED and left_value.type != Type.STRING):
            generator.f_potencia()
            param_temp = generator.add_temp()
            generator.add_expression(param_temp, 'P', env.size, '+')
            generator.add_expression(param_temp, param_temp, '1', '+')
            generator.set_stack(param_temp, left_value.value)
            generator.add_expression(param_temp, param_temp, '1', '+')
            generator.set_stack(param_temp, right_value.value)
            generator.new_env(env.size)
            generator.call_fun('potencia')
            temp = generator.add_temp()
            generator.get_stack(temp, 'P')
            generator.ret_env(env.size)
            fin = generator.new_label()
            generator.add_if(right_value.value, "0", '!=', fin)
            generator.add_expression(temp, '1', '', '')
            generator.put_label(fin)
            return Return(temp, Type.INT, True)
        else:
            if(left_value.type == Type.FLOAT or right_value.type == Type.FLOAT or self.type == ArithmeticOption.DIV):
                label1 = generator.new_label()
                label2 = generator.new_label()
                if ArithmeticOption.DIV == self.type:
                    generator.add_if(right_value.value, '0', '==', label1)
                    aux = generator.add_temp()
                    generator.add_expression(aux, right_value.value, '', '')
                    generator.add_expression(
                        temp, left_value.value, aux, op)
                    generator.add_goto(label2)
                    generator.put_label(label1)
                    # ya mero solo falta cuando es 0 literal
                    generator.add_print('c', 109)  # m
                    generator.add_print('c', 97)  # a
                    generator.add_print('c', 116)  # t
                    generator.add_print('c', 104)  # h
                    generator.add_print('c', 32)
                    generator.add_print('c', 101)  # e
                    generator.add_print('c', 114)  # r
                    generator.add_print('c', 114)  # r
                    generator.add_print('c', 111)  # o
                    generator.add_print('c', 114)  # r

                    generator.put_label(label2)
                elif ArithmeticOption.MODULE == self.type:
                    generator.add_module(
                        temp, left_value.value, right_value.value)
                else:
                    generator.add_expression(
                        temp, left_value.value, right_value.value, op)

                return Return(temp, Type.FLOAT, True)
            elif (left_value.type == Type.STRING):
                left_temp = generator.add_temp()
                right_temp = generator.add_temp()
                ret_temp = generator.add_temp()
                auxiliar_temp = generator.add_temp()
                generator.add_expression(ret_temp, 'H', '', '')
                generator.add_expression(
                    left_temp, left_value.value, '', '')
                generator.add_expression(
                    right_temp, right_value.value, '', '')
                generator.add_expression(
                    auxiliar_temp, left_value.value, '', '')
                if ArithmeticOption.TIMES and right_value.type == Type.STRING:

                    left_label = generator.new_label()
                    right_label = generator.new_label()
                    left_swaper = generator.add_temp()
                    right_swaper = generator.add_temp()
                    generator.get_heap(left_swaper, left_temp)
                    generator.get_heap(right_swaper, right_temp)

                    generator.put_label(left_label)
                    generator.set_heap('H', left_swaper)
                    generator.next_heap()
                    generator.add_expression(left_temp, left_temp, '1', '+')
                    generator.get_heap(left_swaper, left_temp)
                    generator.add_if(left_swaper, '-1', '!=', left_label)

                    generator.put_label(right_label)
                    generator.set_heap('H', right_swaper)
                    generator.next_heap()
                    generator.add_expression(right_temp, right_temp, '1', '+')
                    generator.get_heap(right_swaper, right_temp)
                    generator.add_if(right_swaper, '-1', '!=', right_label)
                    generator.set_heap('H', '-1')
                    generator.next_heap()
                elif self.type == ArithmeticOption.RAISED and right_value.type == Type.INT:
                    begin_lbl = generator.new_label()
                    generator.put_label(begin_lbl)
                    # aqui tengo que formatear el coso ese
                    generator.add_expression(left_temp, auxiliar_temp, '', '')
                    contador = generator.add_temp()
                    generator.add_expression(contador, contador, '1', '+')
                    left_label = generator.new_label()
                    left_swaper = generator.add_temp()
                    generator.get_heap(left_swaper, left_temp)
                    generator.put_label(left_label)
                    generator.set_heap('H', left_swaper)
                    generator.next_heap()
                    generator.add_expression(
                        left_temp, left_temp, '1', '+')
                    generator.get_heap(left_swaper, left_temp)
                    generator.add_if(left_swaper, '-1', '!=', left_label)
                    generator.add_expression(
                        left_temp, left_temp, '1', '-')
                    generator.add_if(right_value.value,
                                     contador, '>', begin_lbl)
                    generator.set_heap('H', '-1')
                    generator.next_heap()
                else:
                    error = {}
                    error['type'] = "aritmetico"
                    error['text'] = "no se puede operar"
                    Environment.errores.append(error)
                    print("no se puede operar")
                    return Return(ret_temp, Type.STRING, True)
            else:
                if op == '%':
                    generator.add_module(
                        temp, left_value.value, right_value.value)
                else:
                    generator.add_expression(
                        temp, left_value.value, right_value.value, op)
                return Return(temp, Type.INT, True)