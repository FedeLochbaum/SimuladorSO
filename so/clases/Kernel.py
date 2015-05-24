from clases.PidGenerator import PidGenerator
from clases.Pcb import Pcb
from clases.Clock import Clock
from _ast import Return

class Kernel :
    def __init__(self,cpu,disk,memoryManager,queuesManager):
        self.cpu = cpu
        self.disk = disk 
        self.memoryManager = memoryManager
        self.queuesManager=queuesManager
        self.pidGenerator = PidGenerator()
        self.clock=Clock(self.cpu)
        self.clock.start()
    
    def loadProgram(self,programName):
        program = self.disk.getProgram(programName)
        if(program==None):
            return;
        if(not self.memoryManager.addinstructionsToMemory(program)):
            self.queuesManager.getWaitingQueue().add(self.generateProcess(program))
            return False
        return True

    def runProgram(self,programName):
        program = self.disk.getProgram(programName)
        if(program==None):
            return;
        process= self.generateProcess(program)
        if(self.cpu.noRunning()):
            self.cpu.setProcess(process)
            return True;
        else:
            self.queuesManager.getReadyQueue().put(process)
            return False

    def generateProcess(self,program):
        name=program.getName()
        pid=self.pidGenerator.generateNewPid()
        pc=0
        finalPc=program.getInstructionsCount()-1
        baseDir=self.memoryManager.getMemory().getNextIndex()
        return Pcb(name,pid,pc,finalPc,baseDir)
    
    def getClock(self):
        return self.clock