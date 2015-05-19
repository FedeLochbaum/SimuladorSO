from clases.IrqHandler import IrqHandler
from clases.IrqKill import IrqKill
from clases.IrqTimeOut import IrqTimeOut
class Cpu:

    def __init__(self,memory):
        self.memory=memory
        self.pcb=None
        self.irqHandler=IrqHandler()
       


    def fetch(self):
        instruccionActual =  self.memory.get(self.pcb.getBaseDir()+self.pcb.getPc())
        if(instruccionActual==None):
            return;
        self.pcb.incrementPc()
        instruccionActual.execute()
        if(self.pcb.getPc()==self.pcb.getFinalPc()):
            self.irqHandler.handle(IrqKill())
            self.pcb=None
       

    '''def decode(self):
        print("decode",self.instruccionActual)

    def execute(self):
        print("execute", self.operacionActual)'''

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

    def getMemory(self):
        return self.memory
    
    def getIrqHandler(self):
        return self.irqHandler

    def timeOut(self):
        self.irqHandler.handle(IrqTimeOut(self.pcb))
        self.pcb=None
