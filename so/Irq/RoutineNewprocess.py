from Irq.Irq import Irq
from Irq.PidGenerator import PidGenerator
from Irq.Routine import Routine
from Program.Pcb import Pcb
from SchedullingAndQueuesManager.SchedulingLargePolitic import SchedullingLargePolitic
from Paginacion.PcbPaginacion import PcbPaginacion


class RoutineNewprocess(Routine):
    
    def __init__(self):
        self.pidGenerator=PidGenerator()
        self.largePolitic=SchedullingLargePolitic()
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.newProcess
    
    def handle(self,irq,cpu,program=None,resource=None):
        Routine.handle(self, irq,cpu,program,resource)
        pcb=self.generateProcess(program,cpu)
        self.largePolitic.handleProcess(program, pcb, cpu.getQueuesManager(), cpu.getMemoryManager())
        
        
    def generateProcess(self,program,cpu):
        name=program.getName()
        pid=self.pidGenerator.generateNewPid()
        pc=0
        finalPc=program.getInstructionsCount()-1
        if(cpu.getMemoryManager().esContinua()):
            baseDir=cpu.getMemoryManager().getMemory().getNextIndex()
            return Pcb(name,pid,pc,finalPc,baseDir)
        else:
            baseDirs=program.getBaseDirs()
            return PcbPaginacion(name,pid,pc,finalPc,baseDirs)
    
   
    