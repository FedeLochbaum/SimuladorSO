from Irq.Irq import Irq
from clases.Cpu import Cpu


class CpuPaginacion(Cpu):

    def __init__(self,memoryManager,irqHandler):
        Cpu.__init__(self, memoryManager, irqHandler)
        
        
    def fetch(self):
        if(self.pcb != None):
            instruccionActual =  self.memoryManager.getInstruction(self.pcb.getPages().Get(),self.pcb.getActualBaseDir())
            if(instruccionActual==None):
                return;
            self.actualInstruction=instruccionActual
            if(instruccionActual.isIO()):
                self.irqHandler.handle(Irq.io)
                self.cleanRegisters()
                return;
            instruccionActual.execute()
            self.pcb.incrementDir()
            if(self.memoryManager.isFinalInPage(self.pcb.getPages().Get()),self.pcb.getActualBaseDir()):
                self.pcb.setActualDir(0)
                self.pcb.getPages().pop() 
            if(self.pcb.getPages() == []):
                self.irqHandler.handle(Irq.kill,self)
                return;