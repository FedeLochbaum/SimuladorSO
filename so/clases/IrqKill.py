
class IrqKill:

    def __init__(self,cpu):
        self.cpu=cpu
        self.execute()
        
    def execute(self):
        memoryManager=self.cpu.getMemoryManager()#BARDEASTE EL CPU CONOCE  ALA MEMORY N A LA MANAGER
        pcb=self.cpu.getPcb()
        memoryManager.borrarRegistrosDe(pcb)
        self.cpu.callNext()
        