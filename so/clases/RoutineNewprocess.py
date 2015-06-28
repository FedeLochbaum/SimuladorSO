from clases.Irq import Irq
from clases.Pcb import Pcb
from clases.PidGenerator import PidGenerator
from clases.Routine import Routine


class RoutineNewprocess(Routine):
    
    def __init__(self):
        self.pidGenerator=PidGenerator()
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.newProcess
    
    def handle(self, irq,cpu,program=None):
        Routine.handle(self, irq,cpu,program)
        pcb=self.generateProcess(program)
        
        
    def generateProcess(self,program):
        name=program.getName()
        pid=self.pidGenerator.generateNewPid()
        pc=0
        finalPc=program.getInstructionsCount()-1
        baseDir=self.cpu.getMemoryManager.getMemory().getNextIndex()
        return Pcb(name,pid,pc,finalPc,baseDir)
    