from Irq.Irq import Irq
from clases.Cpu import Cpu


class CpuPaginacion(Cpu):

    def __init__(self,memoryManager,irqHandler):
        Cpu.__init__(self, memoryManager, irqHandler)
        
        
    def fetch(self):
        if(self.pcb != None):
            
            actualBaseDirPage=self.pcb.getPages()
            
            instruccionActual =  self.memoryManager.getInstruction( actualBaseDirPage[0],self.pcb.getActualBaseDir())
            
            if(instruccionActual==None):
                return;
            self.actualInstruction=instruccionActual
            if(instruccionActual.isIO()):
                self.irqHandler.handle(Irq.io)
                self.cleanRegisters()
                return;
            instruccionActual.execute()
            self.pcb.incrementDir()
            if(self.memoryManager.isFinalInPage(actualBaseDirPage.__getitem__(0),self.pcb.getActualBaseDir())):
                self.pcb.setActualDir(0)
                self.pcb.getPages().pop() 
            if(self.pcb.getPages() == []):
                self.irqHandler.handle(Irq.kill,self)
                return;
        else:
            self.callNext() 