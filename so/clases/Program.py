class Program:
    def __init__(self,name,*instructionss):
        self.name=name
        self.instructions=[]
        for inst in instructionss:
            self.addInstruction(inst) 
        
        
    def getName(self):
        return self.name
    
    def getInstructions(self):
        return self.instructions
    
    def addInstruction(self,instruction):
        self.instructions.append(instruction)

    def getInstructionsCount(self):
        return self.instructions.__len__()

