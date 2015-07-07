from Paginacion.Frame import Frame
class PhysicalMemory():
    
    
    def __init__(self,space,sizeFrame):
        self.dirFrameTable = {}
        self.freeSpace=space
        self.sizeFrame = sizeFrame
        self.totalSpace = space
        self.dividirMemoryIn(sizeFrame)
    
    def put(self,physicalDir,frame):
        self.instructions[physicalDir] = frame
        self.freeSpace-=1

    def removeFromFrame(self,physicalDir):
        return self.dirFrameTable[physicalDir].removePage()
    
    def dividirMemoryIn(self,sizeFrame):
        cant = self.totalSpace / sizeFrame
        sigDir = 1
        while(cant > 0):
            self.dirFrameTable[sigDir] = Frame(sigDir, sigDir +sizeFrame-1)
            sigDir = sigDir + sizeFrame
            cant = cant -1
    
    def sizeFrame(self):
        return self.sizeFrame

    def get(self,physicalDir):
        return self.dirFrameTable[physicalDir]
        
    def getNextIndex(self):
        return self.dirFrameTable.__len__()

    def getFreeSpace(self):
        return self.freeSpace
    
    
    def cleanMemory(self,pcb):
        for i in range(0,pcb.getFinalPc()):
            print(i)
            self.instructions.__delitem__(pcb.getBaseDir()+i)
            
    def getInstructionsCount(self):
        return self.instructions.__len__()
    
    def getTotalSpace(self):
        return self.totalSpace