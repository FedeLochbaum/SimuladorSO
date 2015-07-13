import logging

from Irq.Irq import Irq


class Kernel :
    def __init__(self,cpu,disk,irqHandler,clock):
        self.cpu = cpu
        self.disk = disk
        self.irqHandler=irqHandler
        self.clock=clock
        logging.basicConfig(filename='logSo.log',level=logging.DEBUG)
    
    def loadProgram(self,programName):
        logging.info('Loading program: %s' % programName)
        program = self.disk.getProgram(programName)
        self.irqHandler.handle(Irq.newProcess,self.cpu,program)
        
    def start(self):
        self.clock.start()
        
    def getDisk(self):
        return self.disk
