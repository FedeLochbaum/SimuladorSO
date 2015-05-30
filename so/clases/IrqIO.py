from clases import Irq


class IrqIO:
    def __init__(self,cpu):
        self.cpu =cpu
        
        
    def execute(self):
        pcb = self.cpu.getPcb()
        self.cpu.getIrqHandler().addtoIOQueue(pcb)
        self.cpu.callNext()    

