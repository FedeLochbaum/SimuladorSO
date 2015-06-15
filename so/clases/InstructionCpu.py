from clases.Instruction import Instruction
class InstructionCpu(Instruction):
    
    def __init__(self,message,window):
        self.message=message
        self.window=window
        
    def isIO(self):
        return False