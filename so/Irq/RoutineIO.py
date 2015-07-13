from IO.ResourceManager import ResourceManager
from Irq.Irq import Irq
from Irq.Routine import Routine
import logging


class RoutineIO(Routine):
    
    def __init__(self):
        self.resourceManager=ResourceManager()
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.io
    
    def handle(self, irq,cpu,program=None,ioInstruction=None):
        logging.debug('Running I/O Interruptions')
        Routine.handle(self, irq,cpu,program,ioInstruction)
        self.resourceManager.receiveResourcePcb( cpu.getPcb(),ioInstruction)
        cpu.cleanPcb()
        cpu.callNext()
        