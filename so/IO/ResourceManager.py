from IO.Printer import Printer
from IO.Scanner import Scanner
from IO.Window import Window


class ResourceManager:
    
    
    def __init__(self):
        self.ioResources=[Window(),Scanner(),Printer()] 
        
    def addResource(self,resourceIo):
        self.resources.append(resourceIo)
        
    def receiveResourcePcb(self,pcb,ioInstruction):
        self.anyHandle(pcb,ioInstruction)
        
    def anyHandle(self,pcb,ioInstruction=None):
        for res in self.ioResources:
            if(res.canHandle(ioInstruction.getResource())):
                res.handle(pcb,ioInstruction)
                