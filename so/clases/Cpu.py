from clases.IrqHandler import IrqHandler
from clases.IrqKill import IrqKill
from clases.IrqTimeOut import IrqTimeOut

class Cpu:

    def __init__(self,memory,irqHandler):
        self.memory=memory
        self.pcb=None
        self.irqHandler=irqHandler
       


    def fetch(self):
        print(self.pcb)
        if(self.pcb != None):
            print("BASE DIR+PC"+str(self.pcb.getBaseDir()+self.pcb.getPc()))
            print("BASE DIR"+str(self.pcb.getBaseDir()))
            instruccionActual =  self.memory.get(self.pcb.getBaseDir()+self.pcb.getPc())
            if(instruccionActual==None):
                return;
            self.pcb.incrementPc()
            instruccionActual.execute()
            if(self.pcb.getPc()==self.pcb.getFinalPc()):
                self.irqHandler.handle(IrqKill(self))#el irqKill tiene que borrar las instrucciones de memoria del proceso actual
                self.cleanRegisters()#falta hacerla .. deberia organizar tood para un nuevo proceso
              
                
    def notify(self):
        #print("NOTIFICADO CPU")
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
        self.irqHandler.handle(IrqTimeOut(self.pcb,self.irqHandler))#TODO : creo que deberiamos pasarle el irqHandler a los irq para que desp les diga que hacer con el process
        self.cleanRegisters()
        
    def cleanRegisters(self):
        self.pcb = None   
    def getPcb(self):
        return self.pcb
    
    def callNext(self):
        self.pcb=self.irqHandler.getNext()