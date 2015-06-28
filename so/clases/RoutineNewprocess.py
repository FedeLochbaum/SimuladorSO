from clases.Irq import Irq
from clases.Pcb import Pcb
from clases.PidGenerator import PidGenerator
from clases.Routine import Routine
from clases.SchedulingLargePolitic import SchedullingLargePolitic


class RoutineNewprocess(Routine):
    
    def __init__(self):
        self.pidGenerator=PidGenerator()
        self.largePolitic=SchedullingLargePolitic()
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.newProcess
    
    def handle(self, irq,cpu,program=None):
        Routine.handle(self, irq,cpu,program)
        pcb=self.generateProcess(program,cpu)
        self.largePolitic.handleProcess(program, pcb, cpu.getQueuesManager(), cpu.getMemoryManager())
        
        
    def generateProcess(self,program,cpu):
        name=program.getName()
        pid=self.pidGenerator.generateNewPid()
        pc=0
        finalPc=program.getInstructionsCount()-1
        baseDir=cpu.getMemoryManager().getMemory().getNextIndex()
        return Pcb(name,pid,pc,finalPc,baseDir)
    