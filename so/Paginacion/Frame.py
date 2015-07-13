class Frame:
    
    def __init__(self,baseDir,end):
        self.baseDir=baseDir
        self.end=end
        self.instructions=[]
        
    def size(self):
        return self.end - self.baseDir +1
    

    def getBaseDir(self):
        return self.baseDir
    
    def setEnd(self,end):
        self.end=end
        
    def setBaseDir(self,baseDir):
        self.baseDir=baseDir
    
    def getEnd(self):
        return self.end
    
    def isFree(self):
        return self.page==None
    
    def addInstruction(self,instruction):
        self.instructions.append(instruction)
    
    def removeFrame(self):
        self.instructions = []
    
    def getInstructions(self):
        return self.instructions