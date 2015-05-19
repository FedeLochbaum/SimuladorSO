

class Pcb:

    def __init__(self,name,pid,pc,finalPc,baseDirection):
        self.pid = pid
        self.pc = pc
        self.name = name
        self.finalPc = finalPc
        self.baseDirection = baseDirection

    def incrementPc(self):
        self.pc=self.pc+1
    
    def getName(self):
        return self.name
    
    def getPid(self):
        return self.pid
    
    def getPc(self):
        return self.pc

    def getFinalPc(self):
        return self.finalPc
    
    def getBaseDir(self):
        return self.baseDirection
    
