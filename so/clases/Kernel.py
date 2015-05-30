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
        self.clock=Clock(self.cpu)
        self.clock.start()
        self.process = {}
    
    def loadProgram(self,programName):
        program = self.disk.getProgram(programName)
        process = self.generateProcess(program)
        if(program==None):
            return;
        if(not self.memoryManager.addinstructionsToMemory(program)):
            self.queuesManager.getWaitingQueue().add(process)
            return False
        self.addProcess(process)
        return True

    def runProgram(self,programName):
        process= self.getProcess(programName)
        if(self.cpu.noRunning()):
            self.cpu.setProcess(process)
            print("agrego a cpu")
            return not(self.cpu.noRunning());#que carajo?
        else:
            self.queuesManager.getReadyQueue().put(process)
            print("agrego en ready")
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
    
    def addProcess(self,process):
        self.process[process.getName()] = process
        
    def getProcess(self,nameProcess):
        return self.process[nameProcess]