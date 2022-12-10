from abstract.Expression import *
from abstract.Return import *
from sym.Generator import *
from enum import Enum


class LogicOption(Enum):
    AND = 0
    OR = 1
    NOT = 2


class Logical(Expression):
    def __init__(self, left, right, type, line, column):
        Expression.__init__(self, line, column)
        self.left = left
        self.right = right
        self.type = type

    def compile(self, env):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        generator.add_comment("inicio de expression logica")
        self.check_labels()
        lbl_and_or = ''

        if self.type == LogicOption.AND:
            lbl_and_or = self.left.true_lbl = generator.new_label()
            self.right.true_lbl = self.true_lbl
            self.left.false_lbl = self.right.false_lbl = self.false_lbl
        elif self.type == LogicOption.OR:
            self.left.true_lbl = self.right.true_lbl = self.true_lbl
            lbl_and_or = self.left.false_lbl = generator.new_label()
            self.right.false_lbl = self.false_lbl
        else:
            self.left.true_lbl = self.right.true_lbl = self.false_lbl
            self.left.false_lbl = self.right.false_lbl = self.true_lbl
        left = self.left.compile(env)
        if left.type != Type.BOOL:
            error = {}
            error['type'] = "logica"
            error['text'] = "no se puede utilizar esta expresion"
            Environment.errores.append(error)
            print("error, no se puede utilizar la expression")
            return
        if(lbl_and_or != ''):
            generator.put_label(lbl_and_or)
        right = self.right.compile(env)
        if right.type != Type.BOOL:
            error = {}
            error['type'] = "logica"
            error['text'] = "no se puede utilizar esta expresion"
            Environment.errores.append(error)
            print("erro, no se puede utilizar la expression")
            return
        generator.add_comment("finalizo la expression logica")
        generator.add_space()
        ret = Return(None, Type.BOOL, False)
        ret.true_lbl = self.true_lbl
        ret.false_lbl = self.false_lbl
        return ret

    def check_labels(self):
        gen_aux = Generator()
        generator = gen_aux.get_instance()
        if self.true_lbl == '':
            self.true_lbl = generator.new_label()
        if self.false_lbl == '':
            self.false_lbl = generator.new_label()