
class LogicMemory():



    def __init__(self,space):
        self.dirPageTable={}
        self.totalSpace=space
        self.freeSpace=space
        
    def put(self,logicDir,page):
        self.dirPageTable[page]=logicDir
        self.freeSpace-=1
        
    def get(self,page):
        return self.dirPageTable[page]
    
    def remove(self,page):
        self.freeSpace+=1
        return self.dirPageTable.pop(page)
     
    def getNextIndex(self):
        return self.dirPageTable.__len__()   