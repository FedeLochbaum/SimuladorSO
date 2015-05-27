
class IrqKill:

    def __init__(self,cpu):
        self.cpu=cpu
        
        
    def execute(self):
        memoryManager=self.cpu.getMemoryManager()
        pcb=self.cpu.getPcb()
        memoryManager.borrarRegistrosDe(pcb)
        self.cpu.callNext()
        