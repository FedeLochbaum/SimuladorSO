
class IrqKill:

    def __init__(self,cpu):
        self.cpu=cpu
        
    def execute(self):
        memoryManager=self.cpu.getMemoryManager()
        pcb=self.cpu.getPcb()
        memoryManager.borrarRegistrosDe(pcb)
        self.cpu.callNext() #TODO : handler lo que hace aca es pedir el sig y asignarlo al cpu pero para eso.. deberia conocer al scheduller
        