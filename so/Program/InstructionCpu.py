from Program.Instruction import Instruction

class InstructionCpu(Instruction):
    
    def __init__(self,message,resource=None):
        Instruction.__init__(self, message, resource)
        
        
    def isIO(self):
        return False
    
    def execute(self):
        Instruction.execute(self)
        self.resource.addInfo(self.message)