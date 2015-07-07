class Page():
    


    def __init__(self,count):
        self.instructions=[]
        self.maxInstructionsCount=count
        
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
        

        