from clases.Irq import Irq
from clases.Routine import Routine


class RoutineKill(Routine):
    
    def __init__(self):
        pass
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.kill
    
    def handle(self, irq,cpu,program=None):
        Routine.handle(self, irq,cpu,program)
        cpu.cleanRegisters()
        cpu.callNext()