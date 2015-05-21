from clases.IrqHandler import IrqHandler
from clases.IrqKill import IrqKill
from clases.IrqTimeOut import IrqTimeOut
from clases.QueuesManager import QueuesManager
from clases.ReadyQueuePriority import ReadyQueuePriority
from clases.WaitingQueue import WaitingQueue
class Cpu:

    def __init__(self,memory):
        self.memory=memory
        self.pcb=None
        self.irqHandler=IrqHandler(QueuesManager(ReadyQueuePriority(),WaitingQueue()))
       


    def fetch(self):
        instruccionActual =  self.memory.get(self.pcb.getBaseDir()+self.pcb.getPc())
        if(instruccionActual==None):
            return;
        self.pcb.incrementPc()
        instruccionActual.execute()
        if(self.pcb.getPc()==self.pcb.getFinalPc()):
            self.irqHandler.handle(IrqKill())#el irqKill tiene que borrar las instrucciones de memoria del proceso actual
            self.cleanRegisters()#falta hacerla .. deberia organizar tood para un nuevo proceso
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

    def getMemory(self):
        return self.memory
    
    def getIrqHandler(self):
        return self.irqHandler

    def timeOut(self):
        self.irqHandler.handle(IrqTimeOut(self.pcb,self.irqHandler))#TODO : creo que deberiamos pasarle el irqHandler a los irq para que desp les diga que hacer con el process
        self.cleanRegisters()
