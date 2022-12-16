from .Environment import *

class Generator:
    generator = None
    heap = [0 for i in range(3010199)]
    stack = [0 for i in range(3010199)]
    dict_temp = {"H": 0, "P": 0, '': 0}

    def __init__(self):
        self.count_temp = 0
        self.count_label = 0
        self.code = ''
        self.funcs = ''
        self.natives = ''
        self.in_func = False
        self.in_natives = False
        self.temps = []
        self.print_string = False
        self.print_array = False
        self.potencia = False
        self.to_upper = False
        self.to_lower = False
        self.module = False

    def clean_all(self):
        self.count_temp = 0
        self.count_label = 0
        self.code = ''
        self.funcs = ''
        self.natives = ''
        self.in_func = False
        self.in_natives = False
        self.temps = []
        self.print_string = False
        self.print_array = False
        self.module = False
        Generator.generator = Generator()

    def get_header(self):
        ret = '/*----HEADER----*/\npackage main;\n\nimport (\n\t"fmt"\n)\n\n'
        if self.module:
            ret = '/*----HEADER----*/\npackage main;\n\nimport (\n\t"fmt"\n\t"math"\n)\n\n'
        if len(self.temps) > 0:
            ret += 'var '
            for temp in range(len(self.temps)):
                ret += self.temps[temp]
                if temp != (len(self.temps) - 1):
                    ret += ", "
            ret += " float64;\n"
        ret += "var P, H float64;\nvar stack [30101999]float64;\nvar heap [30101999]float64;\n\n"
        return ret

    def get_code(self):
        return f'{self.get_header()}{self.natives}\n{self.funcs}\nfunc main(){{\n{self.code}\n}}'

    def code_in(self, code, tab="\t"):
        if(self.in_natives):
            if(self.natives == ''):
                self.natives = self.natives + '/*-----NATIVES-----*/\n'
            self.natives = self.natives + tab + code
        elif(self.in_func):
            if(self.funcs == ''):
                self.funcs = self.funcs + '/*-----FUNCS-----*/\n'
            self.funcs = self.funcs + tab + code
        else:
            self.code = self.code + '\t' + code

    def add_comment(self, comment):
        self.code_in(f'/* {comment} */\n')

    def get_instance(self):
        if Generator.generator == None:
            Generator.generator = Generator()
        return Generator.generator

    def add_space(self):
        self.code_in("\n")

    # Manejo de Temporales
    def add_temp(self):
        Generator.dict_temp[f't{self.count_temp}'] = 0
        temp = f't{self.count_temp}'
        self.count_temp += 1
        self.temps.append(temp)
        return temp

    # Manejo de Labels
    def new_label(self):
        label = f'L{self.count_label}'
        self.count_label += 1
        return label

    def put_label(self, label):
        self.code_in(f'{label}:\n')

    # GOTO
    def add_goto(self, label):
        self.code_in(f'goto {label};\n')

    # IF
    def add_if(self, left, right, op, label):
        self.code_in(f'if {left} {op} {right} {{goto {label};}}\n')

    # EXPRESIONES
    def add_expression(self, result, left, right, op):
        if left in Generator.dict_temp.keys() and right in Generator.dict_temp.keys():
            Generator.dict_temp[result] = self.operaciones(
                Generator.dict_temp[left], Generator.dict_temp[right], op)
        elif left in Generator.dict_temp.keys():
            Generator.dict_temp[result] = self.operaciones(
                Generator.dict_temp[left], float(right), op)
        elif right in Generator.dict_temp.keys():
            Generator.dict_temp[result] = self.operaciones(
                float(left), Generator.dict_temp[right], op)
        else:
            Generator.dict_temp[result] = self.operaciones(
                float(left), float(right), op)
        self.code_in(f'{result}={left}{op}{right};\n')

    def add_module(self, result, left, right):
        self.module = True
        self.code_in(f'{result} = math.Mod({left},{right});\n')

    def add_trunc(self, result, data):
        self.module = True
        self.code_in(f'{result} = math.Floor({data});\n')
    # FUNCS

    def add_begin_func(self, id):
        if(not self.in_natives):
            self.in_func = True
        self.code_in(f'func {id}(){{\n', '')

    def add_end_func(self):
        self.code_in('return;\n}\n')
        if(not self.in_natives):
            self.in_func = False

    # STACK
    def set_stack(self, pos, value):
        if pos in Generator.dict_temp.keys() and value in Generator.dict_temp.keys():
            Generator.stack[int(Generator.dict_temp[pos])
                            ] = Generator.dict_temp[value]
        elif pos in Generator.dict_temp.keys():
            Generator.stack[int(Generator.dict_temp[pos])] = float(value)
        elif(value in Generator.dict_temp.keys()):
            Generator.stack[pos] = Generator.dict_temp[value]
        else:
            Generator.stack[pos] = (float(value))
        self.code_in(f'stack[int({pos})]={value};\n')

    def get_stack(self, place, pos):
        if pos in Generator.dict_temp.keys():
            Generator.dict_temp[place] = Generator.stack[int(
                Generator.dict_temp[pos])]
        else:
            Generator.dict_temp[place] = Generator.stack[int(pos)]
        self.code_in(f'{place}=stack[int({pos})];\n')

    # ENVS
    def new_env(self, size):
        self.code_in(f'P=P+{size};\n')

    def call_fun(self, id):
        self.code_in(f'{id}();\n')

    def ret_env(self, size):
        self.code_in(f'P=P-{size};\n')

    # HEAP
    def set_heap(self, pos, value):
        if pos in Generator.dict_temp.keys() and value in Generator.dict_temp.keys():
            Generator.heap[int(Generator.dict_temp[pos])
                           ] = Generator.dict_temp[value]
        elif pos in Generator.dict_temp.keys():
            Generator.heap[int(Generator.dict_temp[pos])] = float(value)
        elif(value in Generator.dict_temp.keys()):
            Generator.heap[pos] = Generator.dict_temp[value]
        else:
            Generator.heap[pos] = (float(value))
        self.code_in(f'heap[int({pos})]={value};\n')

    def get_heap(self, place, pos):
        if pos in Generator.dict_temp.keys():
            Generator.dict_temp[place] = Generator.heap[int(
                Generator.dict_temp[pos])]
        else:
            Generator.dict_temp[place] = Generator.heap[int(pos)]
        self.code_in(f'{place}=heap[int({pos})];\n')

    def next_heap(self):
        Generator.dict_temp["H"] = Generator.dict_temp["H"]+1
        self.code_in('H=H+1;\n')

    # INSTRUCCIONES
    def add_print(self, type, value):
        self.code_in(f'fmt.Printf("%{type}", int({value}));\n')

    def print_float(self, type, value):
        self.code_in(f'fmt.Printf("%{type}", {value});\n')

    def print_true(self):
        self.add_print("c", 116)
        self.add_print("c", 114)
        self.add_print("c", 117)
        self.add_print("c", 101)

    def print_false(self):
        self.add_print("c", 102)
        self.add_print("c", 97)
        self.add_print("c", 108)
        self.add_print("c", 115)
        self.add_print("c", 101)
    
    def fprint_string(self):
        if(self.print_string):
            return
        self.print_string = True
        self.in_natives = True

        self.add_begin_func('print_string')
        # Label para salir de la funcion
        returnLbl = self.new_label()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.new_label()

        # Temporal puntero a Stack
        tempP = self.add_temp()

        # Temporal puntero a Heap
        tempH = self.add_temp()

        self.add_expression(tempP, 'P', '1', '+')

        self.get_stack(tempH, tempP)

        # Temporal para comparar
        tempC = self.add_temp()

        self.put_label(compareLbl)

        self.get_heap(tempC, tempH)

        self.add_if(tempC, '-1', '==', returnLbl)

        self.add_print('c', tempC)

        self.add_expression(tempH, tempH, '1', '+')

        self.add_goto(compareLbl)

        self.put_label(returnLbl)
        self.add_end_func()
        self.in_natives = False

    def fprint_array(self):
        trigger1 = False
        trigger2 = False
        self.fprint_string()

        if(self.print_array):
            return
        self.print_array = True
        self.in_natives = True
        self.add_begin_func('print_array')
        # Label para salir de la funcion
        returnLbl = self.new_label()
        # Label para hacer la comparacion para saber cuando termina el arreglo
        compareLbl = self.new_label()
        # label para strings
        printS = self.new_label()
        # label para arreglos
        printA = self.new_label()
        # Puntero a stack
        tempP = self.add_temp()
        # Puntero a heap
        tempH = self.add_temp()
        self.add_expression(tempP, 'P', '1', '+')
        self.get_stack(tempH, tempP)
        # contador
        contador = self.add_temp()
        # tamano
        tamano = self.add_temp()
        self.get_heap(tamano, tempH)
        # puntero tamano
        punteroinicial = self.add_temp()
        self.add_expression(tempH, tempH, '1', '+')
        tempC = self.add_temp()
        self.add_print('c', 91)
        self.put_label(compareLbl)
        self.get_heap(tempC, tempH)
        self.add_expression(punteroinicial, tempC, '', '')
        self.add_if(contador, tamano, '>=', returnLbl)

        for element in Environment.heapsA:
            self.add_if(element, punteroinicial, '==', printA)
            trigger1 = True
        for element in Environment.heapsS:
            self.add_if(element, tempC, '==', printS)
            trigger2 = True
        self.print_float('f', tempC)
        self.add_print('c', 44)
        self.add_expression(tempH, tempH, '1', '+')
        self.add_expression(contador, contador, '1', '+')
        self.add_goto(compareLbl)
        # son 5 temporales
        if(trigger1):
            self.put_label(printA)

            tempauxP = self.add_temp()
            tempauxcont = self.add_temp()
            tempauxtam = self.add_temp()
            tempauxC = self.add_temp()
            tempauxPP = self.add_temp()
            tempauxH = self.add_temp()
            self.add_expression(tempauxP, 'P', '', '')
            self.add_expression(tempauxcont, contador, '', '')
            self.add_expression(tempauxtam, tamano, '', '')
            self.add_expression(tempauxC, tempC, '', '')
            self.add_expression(tempauxPP, tempP, '', '')
            self.add_expression(tempauxH, tempH, '', '')
            self.add_expression(contador, '0', '', '')
            self.set_stack(tempP, tempC)
            self.call_fun("print_array")

            self.add_expression(contador, tempauxcont, '1', '+')
            self.add_expression(tamano, tempauxtam, '', '')
            self.add_expression(tempC, tempauxC, '', '')
            self.add_expression(tempP, tempauxPP, '', '')
            self.add_expression(tempH, tempauxH, '1', '+')

            self.add_goto(compareLbl)
        if(trigger2):
            self.put_label(printS)

            tempauxP = self.add_temp()
            tempauxcont = self.add_temp()
            tempauxtam = self.add_temp()
            tempauxC = self.add_temp()
            tempauxPP = self.add_temp()
            tempauxH = self.add_temp()

            self.add_expression(tempauxP, 'P', '', '')
            self.add_expression(tempauxcont, contador, '', '')
            self.add_expression(tempauxtam, tamano, '', '')
            self.add_expression(tempauxC, tempC, '', '')
            self.add_expression(tempauxPP, tempP, '', '')
            self.add_expression(tempauxH, tempH, '', '')
            self.set_stack(tempP, tempC)
            self.call_fun("print_string")

            self.add_expression('P', tempauxP, '', '')
            self.add_expression(contador, tempauxcont, '1', '+')
            self.add_expression(tamano, tempauxtam, '', '')
            self.add_expression(tempC, tempauxC, '', '')
            self.add_expression(tempP, tempauxPP, '', '')
            self.add_expression(tempH, tempauxH, '1', '+')
            self.add_print('c', 44)

            self.add_goto(compareLbl)

        self.put_label(returnLbl)
        self.add_print('c', 93)
        self.add_expression(contador, '0', '', '')
        self.add_end_func()
        self.in_natives = False

    def operaciones(self, left, right, op):
        try:
            if(op == '+'):
                return left + right
            elif(op == '-'):
                return left - right
            elif(op == '*'):
                return left * right
            elif(op == '/'):
                return left / right
            elif(op == '%'):
                return left % right
            else:
                return left
        except:
            return left

    def f_to_upper(self):
        if(self.to_upper):
            return
        self.to_upper = True
        self.in_natives = True

        self.add_begin_func('to_upper')
        # Label para salir de la funcion
        returnLbl = self.new_label()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.new_label()

        # Temporal puntero a Stack
        tempP = self.add_temp()

        # Temporal puntero a Heap
        tempH = self.add_temp()

        self.add_expression(tempP, 'P', '1', '+')

        self.get_stack(tempH, tempP)

        # Temporal para comparark
        tempC = self.add_temp()

        self.put_label(compareLbl)

        self.get_heap(tempC, tempH)

        self.add_if(tempC, '-1', '==', returnLbl)

        temp = self.add_temp()
        pass_label = self.new_label()
        self.add_if(tempC, '97', '<', pass_label)
        self.add_if(tempC, '122', '>', pass_label)
        self.add_expression(temp, tempC, '32', '-')
        self.set_heap(tempH, temp)
        self.put_label(pass_label)
        self.add_expression(tempH, tempH, '1', '+')

        self.add_goto(compareLbl)

        self.put_label(returnLbl)
        self.add_end_func()
        self.in_natives = False

    def f_to_lower(self):
        if(self.to_lower):
            return
        self.to_lower = True
        self.in_natives = True

        self.add_begin_func('to_lower')
        # Label para salir de la funcion
        returnLbl = self.new_label()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.new_label()

        # Temporal puntero a Stack
        tempP = self.add_temp()

        # Temporal puntero a Heap
        tempH = self.add_temp()

        self.add_expression(tempP, 'P', '1', '+')

        self.get_stack(tempH, tempP)

        # Temporal para comparark
        tempC = self.add_temp()

        self.put_label(compareLbl)

        self.get_heap(tempC, tempH)

        self.add_if(tempC, '-1', '==', returnLbl)

        temp = self.add_temp()
        pass_label = self.new_label()
        self.add_if(tempC, '65', '<', pass_label)
        self.add_if(tempC, '90', '>', pass_label)
        self.add_expression(temp, tempC, '32', '+')
        self.set_heap(tempH, temp)
        self.put_label(pass_label)
        self.add_expression(tempH, tempH, '1', '+')

        self.add_goto(compareLbl)

        self.put_label(returnLbl)
        self.add_end_func()
        self.in_natives = False