class Page():
    


    def __init__(self,dirBase,count):
        self.instructions=[]
        self.maxInstructionsCount=count
        self.dirBase = dirBase
        
    def getLogicDir(self):
        return self.dirBase
        
    def addInstruction(self,instruction):
        if(self.maxInstructionsCount>0):
            self.instructions.append(instruction)
            self.maxInstructionsCount-=1
            return True
        else:
            return False
        
    def removeInstruction(self,instruction):
        self.instructions.remove(instruction)
        self.maxInstructionsCount+=1
       
    def fill(self,instructions):
        for instruction in instructions:
            if not self.addInstruction(instruction):
                return; 
    def isFree(self):
        return self.instructions==[]
    
    def setInstructions(self,program):
        for instruction in program.getInstructions():
            if(self.maxInstructionsCount>0):
                self.addInstruction(instruction)
        

    def getInstructions(self):
        return self.instructions   
    
    def getBaseDir(self):
        return self.dirBase