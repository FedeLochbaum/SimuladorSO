from clases.PidGenerator import PidGenerator
from clases.Pcb import Pcb
from clases.Clock import Clock

class Kernel :
    def __init__(self,cpu,disk,memoryManager,queuesManager):
        self.cpu = cpu
        self.disk = disk 
        self.memoryManager = memoryManager
        self.queuesManager=queuesManager
        self.pidGenerator = PidGenerator()
        self.clock=Clock()
        self.clock.start()
    
    def loadProgram(self,programName):
        program = self.disk.getprogram(programName)
        if(program==None):
            return;
        if(not self.memoryManager.addinstructionsToMemory(program)):
            self.queuesManager.getWaitingQueue().add(self.generateProcess(program))

    def runProgram(self,programName):
        program = self.disk.getProgram(programName)
        if(program==None):
            return;
        process= self.generateProcess(program)
        if(self.cpu.noRunning()):
            self.cpu.setProcess(process)
        else:
            self.memoryManager.getReadyQueue().add(process)

    def generateProcess(self,program):
        return Pcb(program.getName(),self.generadorDePid.generateNewPid(),0,program.getInstructionsCount(),self.memoryManager.getMemory().getNextIndex())
    
    def getClock(self):
        return self.clock