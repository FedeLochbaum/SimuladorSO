from IO.Printer import Printer
from IO.Scanner import Scanner
from IO.Window import Window


class ResourceManager:
    
    
    def __init__(self):
        self.ioResources=[Window(),Scanner(),Printer()] 
        
    def addResource(self,resourceIo):
        self.resources.append(resourceIo)
        
    def receiveResourcePcb(self,resource,pcb):
        self.anyHandle(resource,pcb)
        
    def anyHandle(self,resource,pcb):
        for res in self.ioResources:
            if(res.canHandle(resource)):
                res.handle(pcb)
                