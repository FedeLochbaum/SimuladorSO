from clases.Irq import Irq



class Cpu:

    def __init__(self,memoryManager,irqHandler):
        self.memoryManager=memoryManager
        self.pcb=None
        self.irqHandler=irqHandler
       


    def fetch(self):
        if(self.pcb != None):
            instruccionActual =  self.memoryManager.getMemory().get(self.pcb.getBaseDir()+self.pcb.getPc())
            if(instruccionActual==None):
                return; 
            instruccionActual.execute()
            if(instruccionActual.isIO()):
                self.irqHandler.handle(Irq.io)
                self.cleanRegisters()
                return;
            if(self.pcb.getPc()==self.pcb.getFinalPc()):
                self.irqHandler.handle(Irq.kill,self)
                return;
            self.pcb.incrementPc()
                
    def notify(self):
        self.fetch()  

    def setProcess(self, process):
        self.pcb = process

    def noRunning(self):
        return self.pcb==None

    def getMemoryManager(self):
        return self.memoryManager
    
    def getIrqHandler(self):
        return self.irqHandler

    def timeOut(self):
        self.irqHandler.handle(Irq.timeOut)
        self.cleanRegisters()
        
    def cleanRegisters(self):
        self.memoryManager.cleanMemory(self.pcb)
        self.cleanPcb()
        
    def cleanPcb(self):
        self.pcb = None
        
    def getPcb(self):
        return self.pcb
    
    def instructionsInMemoryCount(self):
        return self.memoryManager.getInstructionsCount()
    
    def callNext(self):
        self.pcb=self.irqHandler.getNext()
        
    def getQueuesManager(self):
        return self.irqHandler.getQueuesManager()