from clases.Irq import Irq
from clases.Routine import Routine
from clases.ResourceManager import ResourceManager


class RoutineIO(Routine):
    
    def __init__(self):
        self.resourceManager=ResourceManager()
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.io
    
    def handle(self, irq,cpu,program=None,resource=None):
        Routine.handle(self, irq,cpu,program,resource)
        self.resourceManager.receiveResourcePcb(resource, cpu.getPcb())
        cpu.cleanPcb()
        