

class LogicMemory():



    def __init__(self,space):
        self.dirPageTable={}
        self.totalSpace=space
        self.freeSpace=space
        
    def put(self,logicDir,page):
        self.dirPageTable[logicDir]=page
        
    def get(self,logicDir):
        return self.dirPageTable[logicDir]
        