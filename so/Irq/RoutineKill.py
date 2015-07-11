from Irq.Irq import Irq
from Irq.Routine import Routine


class RoutineKill(Routine):
    
    def __init__(self):
        pass
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.kill
    
    def handle(self,irq,cpu,program=None,ioInstruction=None):
        Routine.handle(self, irq,cpu,program,ioInstruction)
        cpu.cleanRegisters()
        cpu.callNext()