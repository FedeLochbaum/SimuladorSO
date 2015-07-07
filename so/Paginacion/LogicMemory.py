
class LogicMemory():



    def __init__(self,space,sizeFrame):
        self.dirPageTable={}
        self.totalSpace=space
        self.freeSpace=space
        self.sizePage = sizeFrame
        #aca te falta inicializar las pages como hice yo en la fisica con los marcos
        
    def setandLoadPages(self,program):
        #tenes que ahcer este metodo
        pass
        
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
    
    def getFreeSpace(self):
        return self.freeSpace 
    
    def getTotalSpace(self):
        return self.totalSpace