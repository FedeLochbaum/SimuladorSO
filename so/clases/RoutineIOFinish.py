from clases.Irq import Irq
from clases.Routine import Routine


class RoutineIOFinish(Routine):
    
    def __init__(self,schedullingPolitic):
        schedullingPolitic = schedullingPolitic
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.ioFinish
    
    def handle(self,irq,cpu,program=None,resource=None):
        Routine.handle(self, irq,cpu,program,resource)
        self.schedullingPolitic.setPcbInReady(cpu.getPcb())
        #aca esta mal por cpu