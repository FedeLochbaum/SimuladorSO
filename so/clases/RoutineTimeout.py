from clases.Irq import Irq
from clases.Routine import Routine


class RoutineTimeout(Routine):
    
    def __init__(self,schedullingPolitic):
        self.schedullingPolitic = schedullingPolitic
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.timeOut
    
    def handle(self, irq,cpu,disk=None):
        Routine.handle(self, irq,cpu,disk)
        self.schedullingPolitic.setPcbInReady(cpu.getPcb())
        cpu.cleanPcb()
        cpu.callNext()