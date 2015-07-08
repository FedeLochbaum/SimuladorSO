from clases.Clock import Clock
from clases.Irq import Irq


class Kernel :
    def __init__(self,cpu,disk,irqHandler):
        self.cpu = cpu
        self.disk = disk
        self.irqHandler=irqHandler
        self.clock=Clock(self.cpu)
        #self.clock.start()
    
    def loadProgram(self,programName):
        program = self.disk.getProgram(programName)
        self.irqHandler.handle(Irq.newProcess,self.cpu,program)