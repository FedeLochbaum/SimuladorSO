from clases.Pcb import Pcb


class PcbPaginacion(Pcb):

    def __init__(self,name,pid,pc,finalPc,baseDirs):
        Pcb.__init__(self, name, pid, pc, finalPc, None, None)
        self.baseDirs=baseDirs
        self.actualBaseDir=None
        
    def setActualDir(self,baseDir):
        self.actualBaseDir=baseDir
        
    
        