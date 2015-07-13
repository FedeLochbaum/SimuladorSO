from Irq.Irq import Irq
from Irq.Routine import Routine
import logging


class RoutineTimeout(Routine):
    
    def __init__(self,schedullingPolitic):
        self.schedullingPolitic = schedullingPolitic
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.timeOut
    
    def handle(self,irq,cpu,program=None,ioInstruction=None):
        logging.debug('Running Time Out Interruption')
        Routine.handle(self, irq,cpu,program,ioInstruction)
        self.schedullingPolitic.setPcbInReady(cpu.getPcb())
        cpu.cleanPcb()
        cpu.callNext()