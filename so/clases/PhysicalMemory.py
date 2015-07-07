class PhysicalMemory():
    
    
    def __init__(self,space):
        self.dirFrameTable = {}
        self.freeSpace=space
        self.totalSpace = space
    
    def put(self,physicalDir,frame):
        self.instructions[physicalDir] = frame
        self.freeSpace-=1

    def removeFromFrame(self,physicalDir):
        return self.dirFrameTable[physicalDir].removePage()


    def get(self,physicalDir):
        return self.dirFrameTable[physicalDir]
        
    def getNextIndex(self):
        return self.dirFrameTable.__len__()

    def getFreeSpace(self):
        return self.freeSpace
    
    def setFreeSpace(self,space):
        self.freeSpace = space
    
    def cleanMemory(self,pcb):
        for i in range(0,pcb.getFinalPc()):
            print(i)
            #self.instructions[pcb.getBaseDir()+i]=None
            self.instructions.__delitem__(pcb.getBaseDir()+i)
            
    def getInstructionsCount(self):
        return self.instructions.__len__()
    
    def getTotalSpace(self):
        return self.totalSpace