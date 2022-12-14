from abstract.Instruction import *


class Statement(Instruction):
    def __init__(self, instructions, line, column):
        Instruction.__init__(self, line, column)
        self.instructions = instructions

    def compile(self, env):
        for ins in self.instructions:
            ret = ins.compile(env)
            if ret is not None:
                return ret