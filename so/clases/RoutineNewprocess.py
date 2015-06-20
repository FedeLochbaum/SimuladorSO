from clases.Irq import Irq
from clases.Routine import Routine


class RoutineNewprocess(Routine):
    
    def __init__(self):
        pass
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.newProcess
    
    def handle(self, irq):
        Routine.handle(self, irq)
        #hacer