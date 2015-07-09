from clases.Irq import Irq
from clases.Routine import Routine


class RoutineKill(Routine):
    
    def __init__(self):
        pass
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.kill
    
    def handle(self,irq,cpu,program=None,resource=None):
        Routine.handle(self, irq,cpu,program,resource)
        cpu.getMemoryManager().cleanMemory(cpu.getPcb())
        cpu.cleanRegisters()
        cpu.callNext()