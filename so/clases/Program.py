class Program:
    def __init__(self,name,*instructionss):
        self.name=name
        self.instructions=[]
        self.pages = []
        for inst in instructionss:
            self.addInstruction(inst) 
        
        
    def getName(self):
        return self.name
    
    def setPages(self,pages):
        self.pages = pages
    
    def getInstructions(self):
        return self.instructions
    
    def addInstruction(self,instruction):
        self.instructions.append(instruction)

    def getInstructionsCount(self):
        return self.instructions.__len__()

    def getPages(self):
        return self.pages
    
    def removeInstructionsFrom(self,page):
        for inst in page.getInstructions():
            self.instructions.remove(inst)