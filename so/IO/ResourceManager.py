import logging

from IO.Printer import Printer
from IO.Scanner import Scanner
from IO.Window import Window


class ResourceManager:
    
    
    def __init__(self):
        self.ioResources=[Window(),Scanner(),Printer()] 
        logging.basicConfig(filename='logSo.log',level=logging.DEBUG)
        
    def addResource(self,resourceIo):
        self.ioResources.append(resourceIo)
        
    def receiveResourcePcb(self,pcb,ioInstruction):
        logging.debug('ResourceManager received: %s' % pcb.getName())
        self.anyHandle(pcb,ioInstruction)
        
    def anyHandle(self,pcb,ioInstruction=None):
        for res in self.ioResources:
            if(res.canHandle(ioInstruction.getResource())):
                res.handle(pcb,ioInstruction)
                