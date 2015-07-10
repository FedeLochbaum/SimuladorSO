from Irq.Irq import Irq
from clases.Clock import Clock


class Kernel :
    def __init__(self,cpu,disk,irqHandler):
        self.cpu = cpu
        self.disk = disk
        self.irqHandler=irqHandler
        self.clock=Clock(self.cpu)
        self.clock.start()
    
    def loadProgram(self,programName):
        program = self.disk.getProgram(programName)
        self.irqHandler.handle(Irq.newProcess,self.cpu,program)
        
    def newProcess(self,programName):
        program=self.disk.getProgram(programName)
        self.irqHandler.handle(Irq.newProcess,self.cpu,program)