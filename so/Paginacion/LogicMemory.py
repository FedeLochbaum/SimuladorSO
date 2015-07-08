from Paginacion.Page import Page


class LogicMemory():



    def __init__(self,space,sizePage):
        self.dirPageTable={}
        self.totalSpace=space
        self.freeSpace=space
        self.sizePage = sizePage
        self.emptyPages = []
        self.divideMemoryIn(sizePage)
        
    def setandLoadPages(self,program):
        pages = self.pagesFor(program.getInstructionsCount())
        self.fillPagesWithProgram(pages,program)
        program.setPages(pages)
        #for instruction in program.getInstructions():
            #page=self.emptyPages.pop()
            #while():
            #    page.setInstructions(program)
            #    program.addPage(page)
                    
    def pagesFor(self,cant):
        result = []
        cantPages =round(cant / self.sizePage,1)
        while(cantPages > 0):
            result.append(self.emptyPages.pop())
            cantPages-=1
            
        return result
    
    def fillPagesWithProgram(self,pages,program):
        instructions = program.getInstructions()
        for page in pages:
            page.fill(instructions)
            
    def divideMemoryIn(self,sizePage):
        cant = self.totalSpace / sizePage
        sigDir = 1
        while(cant > 0):
            page = Page(sigDir,sizePage)
            self.dirPageTable[sigDir] = page
            sigDir = sigDir + sizePage
            self.emptyPages.append(page)
            cant = cant -1
        
        
    def put(self,logicDir,page):
        self.dirPageTable[page]=logicDir
        self.freeSpace-=1
        
    def get(self,page):
        return self.dirPageTable[page]
    
    def remove(self,page):
        elem=self.dirPageTable.pop(page)
        self.freeSpace+=1
        return elem
    
    def getFreeSpace(self):
        return self.freeSpace 
    
    def getTotalSpace(self):
        return self.totalSpace