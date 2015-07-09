from Paginacion.Frame import Frame
class PhysicalMemory():
    
    
    def __init__(self,space,sizeFrame):
        self.dirFrameTable = {}
        self.freeSpace=space
        self.sizeFrame = sizeFrame
        self.totalSpace = space
        self.emptyFrames = []
        self.divideMemoryIn(sizeFrame)
    

    def removeFromFrame(self,physicalDir):
        return self.dirFrameTable[physicalDir].removeFrame()
    
    def divideMemoryIn(self,sizeFrame):
        cant = round(self.totalSpace / sizeFrame,1)
        sigDir = 1
        while(cant > 0):
            frame = Frame(sigDir, sigDir +sizeFrame-1)
            self.dirFrameTable[sigDir] = frame
            sigDir = sigDir + sizeFrame
            self.emptyFrames.append(frame)
            cant = cant -1
            
    def put(self,frame,instruction):
        frame.addInstruction(instruction)
        self.freeSpace-=1
    
    def getSizeFrame(self):
        return self.sizeFrame

    def getFrame(self):
        return self.emptyFrames.pop()
    
    def get(self,physicalDir):
        return self.dirFrameTable[physicalDir]
        
    def getNextIndex(self):
        return self.dirFrameTable.__len__()

    def getFreeSpace(self):
        return self.freeSpace
    
    def cleanMemory(self,pcb):
        #esto esta de mas desp sacarlo
        for i in range(0,pcb.getFinalPc()):
            print(i)
            self.instructions.__delitem__(pcb.getBaseDir()+i)
            
    def getInstructionsCount(self):
        return self.instructions.__len__()
    
    def getTotalSpace(self):
        return self.totalSpace