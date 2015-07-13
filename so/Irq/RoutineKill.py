from Irq.Irq import Irq
from Irq.Routine import Routine
import logging


class RoutineKill(Routine):
    
    def __init__(self):
        pass
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.kill
    
    def handle(self,irq,cpu,program=None,ioInstruction=None):
        logging.debug('Running Kill Interruption')
        Routine.handle(self, irq,cpu,program,ioInstruction)
        cpu.cleanRegisters()
        cpu.callNext()