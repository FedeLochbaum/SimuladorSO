from clases.Irq import Irq
from clases.IrqHandler import IrqHandler
from clases.IrqIO import IrqIO
from clases.IrqKill import IrqKill
from clases.IrqTimeOut import IrqTimeOut


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
                self.irqHandler.handle(IrqIO(self))
                self.cleanRegisters()
                return;
            if(self.pcb.getPc()==self.pcb.getFinalPc()):
                self.irqHandler.handle(Irq.kill)
                self.cleanRegisters()
                return;
            self.pcb.incrementPc()
                
    def notify(self):
        self.fetch()  

    '''def decode(self):
        print("decode",self.instruccionActual)
    
    def execute(self):
        print("execute", self.operacionActual)'''
                ###  aca deberia ver que onda con la instruccion .. si es IO tiene que lanzar irqIO    ###
    ''' def avanzarClock(self):
        self.fetch()

        if (self.instruccionActual== self.pcFinal):
            print("Senal de fin")
        elif (self.instruccionActual=='IO'):
            print("Senal de interrupcion")
        else:
            self.decode()
            self.execute()'''



    def setProcess(self, process):
        self.pcb = process

    def noRunning(self):
        return self.pcb==None

    def getMemoryManager(self):
        return self.memoryManager
    
    def getIrqHandler(self):
        return self.irqHandler

    def timeOut(self):
        self.irqHandler.handle(IrqTimeOut(self))
        self.cleanRegisters()
        
    def cleanRegisters(self):
        self.pcb = None 
        
    def getPcb(self):
        return self.pcb
    
    def callNext(self):
        self.pcb=self.irqHandler.getNext()