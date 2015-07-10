from clases.Pcb import Pcb


class PcbPaginacion(Pcb):

    def __init__(self,name,pid,pc,finalPc,baseDirs):
        Pcb.__init__(self, name, pid, pc, finalPc, None, None)
        self.baseDirs=baseDirs
        self.pages = baseDirs
        #baseDirs es una lista de direcciones base a las paginas asignadas
        self.actualBaseDir=0
        
    def setActualDir(self,baseDir):
        self.actualBaseDir=baseDir
        
    def incrementDir(self):
        self.actualBaseDir+=1
        
    def getDirsPage(self):
        return self.baseDirs
    
    def getPages(self):
        return self.pages
    
    def getActualBaseDir(self):
        return self.actualBaseDir
        
    
        