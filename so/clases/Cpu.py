from clases.Irq import Irq
from clases.Timer import Timer


class Cpu:

    def __init__(self,memoryManager,irqHandler):
        self.memoryManager=memoryManager
        self.pcb=None
        self.irqHandler=irqHandler
        self.timer=Timer()
        self.setCpuToTimer()
        self.setQuantum()
        self.actualInstruction=None
       


    def fetch(self):
        if(self.pcb != None):
            instruccionActual =  self.memoryManager.getMemory().get(self.pcb.getBaseDir()+self.pcb.getPc())
            if(instruccionActual==None):
                return;
            self.actualInstruction=instruccionActual
            if(instruccionActual.isIO()):
                self.irqHandler.handle(Irq.io)
                self.cleanRegisters()
                return;
            instruccionActual.execute()
            self.pcb.incrementPc()
            if(self.pcb.getPc()==self.pcb.getFinalPc()):
                self.irqHandler.handle(Irq.kill,self)
                return;
            
                
    def notifyUserMode(self):
        self.fetch() 
    
    def notifyKernelMode(self):
        self.runIrqs() 
    
    def runIrqs(self):
        self.irqHandler.runIrqs()
        
    def show(self,item):
        print (item)
        
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
        self.timer.restart()
        
    def getQueuesManager(self):
        return self.irqHandler.getQueuesManager()
    
    def setCpuToTimer(self):
        self.timer.setCpu(self)
        
    def setQuantum(self):
        self.timer.setQuantum(self.irqHandler.getQuantum())
    def getActualInstruction(self):
        return self.actualInstruction