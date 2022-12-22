from .Symbol import *
from abstract.Return import *

class Environment:
    variables = {}
    functions = {}
    structs = {}
    errores = []
    entrada = []
    heapsS = []
    heapsA = []

    def __init__(self, prev_env):
        self.variables = {}
        self.functions = {}
        self.structs = {}
        self.prev = prev_env
        self.size = 0
        self.break_lbl = ''
        self.continue_lbl = ''
        self.return_lbl = ''
        if prev_env is not None:
            self.size = self.prev.size
            self.break_lbl = self.prev.break_lbl
            self.continue_lbl = self.prev.continue_lbl
            self.return_lbl = self.prev.return_lbl

    def get_items_array(self, array):
        env = self
        array_return = []
        for element in array:
            if isinstance(element, int) or isinstance(element, bool) or isinstance(element, str) or isinstance(element, float):
                array_return.append(element)
            elif isinstance(element, Return):
                array_return.append(element.value)
            elif isinstance(element, list):
                array_return.append(self.get_items_array(element))
            else:
                element_value = element.execute(env)
                if element_value.type != Type.LIST:
                    array_return.append(element_value.value)
                else:
                    array_return.append(
                        self.get_items_array(element_value.value))
        return array_return
    
    def save_var(self, id_var, sym_type, in_heap, struct_type=''):
        env = self
        while env is not None:
            if id_var in env.variables.keys():
                print("Variable ya existe")
                env.variables[id_var] = Symbol(id_var, sym_type, env.variables[id_var].pos,
                                               env.prev == None, in_heap, struct_type)
                Environment.variables = env.variables
                return env.variables[id_var]
            env = env.prev
        if(id_var[-1] == '#'):
            id_var = id_var[0:-1]
        newSymbol = Symbol(id_var, sym_type, self.size,
                           self.prev == None, in_heap, struct_type)
        self.size += 1
        self.variables[id_var] = newSymbol
        Environment.variables = self.variables
        return self.variables[id_var]

    def save_func(self, id_func, function):
        if id_func in self.functions.keys():
            print("Función repetida")
        else:
            self.functions[id_func] = function
            Environment.functions = self.functions

    def save_struct(self, id_struct, attributes):
        if id_struct in self.structs.keys():
            print("Struct repetido")
        else:
            self.structs[id_struct] = attributes
            Environment.structs = self.structs

    def get_var(self, id_var):
        env = self
        while env is not None:
            if id_var in env.variables.keys():
                return env.variables[id_var]
            env = env.prev
        return None

    def get_func(self, id_func):
        env = self
        while env is not None:
            if id_func in env.functions.keys():
                return env.functions[id_func]
            env = env.prev
        return None

    def get_struct(self, id_struct):
        env = self
        while env != None:
            if id_struct in env.structs.keys():
                return env.structs[id_struct]
            env = env.prev
        return None

    def get_global(self):
        env = self
        while env.prev != None:
            env = env.prev
        return env

