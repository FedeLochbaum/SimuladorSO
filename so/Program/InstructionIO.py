from Program.Instruction import Instruction


class InstructionIO(Instruction):
    def __init__(self,message,resource):
        Instruction.__init__(self,message,resource)
        
        
    def isIO(self):
        return True
    def execute(self):
        Instruction.execute(self)
        self.resourse.show(self.getMessage())