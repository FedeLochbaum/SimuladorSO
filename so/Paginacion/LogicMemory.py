from Paginacion.Page import Page


class LogicMemory():



    def __init__(self,space,sizePage):
        self.dirPageTable={}
        self.totalSpace=space
        self.freeSpace=space
        self.sizePage = sizePage
        self.divideMemoryIn(sizePage)
        
    def setandLoadPages(self,program):
        while (program.getInstructionsCount()>0):
            for page in self.dirPageTable.values():
                if page.isFree():
                    page.setInstructions(program)
        
    def divideMemoryIn(self,sizePage):
        cant = self.totalSpace / sizePage
        sigDir = 1
        while(cant > 0):
            self.dirPageTable[sigDir] = Page(sizePage)
            sigDir = sigDir + sizePage
            cant = cant -1
        
    def put(self,logicDir,page):
        self.dirPageTable[page]=logicDir
        self.freeSpace-=1
        
    def get(self,page):
        return self.dirPageTable[page]
    
    def remove(self,page):
        self.freeSpace+=1
        return self.dirPageTable.pop(page)
       
    
    def getFreeSpace(self):
        return self.freeSpace 
    
    def getTotalSpace(self):
        return self.totalSpace