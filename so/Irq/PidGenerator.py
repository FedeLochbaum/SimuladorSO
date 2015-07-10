class PidGenerator:
    def __init__(self):
        self.freePids = []
        self.pid = 0
        
    def generateNewPid(self):
        if(len(self.freePids)== 0):
            self.pid+=1
            return self.getPid()
        else:
            return self.getFreePids().pop()
        
    def addPidToFree(self,pid):
        self.freePids.append(pid)
    
    def getFreePids(self):
        return self.freePids
    
    def getPid(self):
        return self.pid

        
            
        
        
        
