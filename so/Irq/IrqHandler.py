import logging

from Irq.RoutineIO import RoutineIO
from Irq.RoutineIOFinish import RoutineIOFinish
from Irq.RoutineKill import RoutineKill
from Irq.RoutineNewprocess import RoutineNewprocess
from Irq.RoutineTimeout import RoutineTimeout


class IrqHandler:
    
    def __init__(self,schedullingPolitic):
        self.irqs={}
        self.routines=[RoutineKill(),RoutineTimeout(schedullingPolitic),RoutineNewprocess(),RoutineIO(),RoutineIOFinish(schedullingPolitic)]#falta la de page
        self.queueManager = schedullingPolitic.getqueuesManager()
        self.schedullingPolitic=schedullingPolitic
        logging.basicConfig(filename='logSo.log',level=logging.DEBUG)
        
    def handle(self,irq,cpu,program=None,ioInstruction=None): 
        self.irqs[irq] = (cpu,program,ioInstruction)
        logging.debug('New Interruption: %s' % irq.value)
        #self.anyRoutineHandle(irq,cpu,program,resource)
    
        
    def runIrqs(self):
        logging.debug('Running all added Interruptions')
        for (irq,params) in self.irqs.items():
            self.anyRoutineHandle(irq,params[0],params[1],params[2])
        self.irqs = {}
    
    
    def cantIrqs(self):
        return self.irqs.__len__()
    
    def addToReady(self,process):
        self.queueManager.putInReady(process)
        
    def addtoIOQueue(self,process):
        self.queueManager.getIOQueue().add(process)
        
    def getNext(self):
        return self.schedullingPolitic.next()
        
    def anyRoutineHandle(self,irq,cpu,program=None,ioInstruction=None):
        for routine in self.routines:
            if(routine.canHandle(irq)):
                routine.handle(irq,cpu,program,ioInstruction)
                return;
            
    def getQueuesManager(self):
        return self.queueManager
    
    def getQuantum(self):
        return self.schedullingPolitic.getQuantum()
    def get(self,irq):
        return self.irqs[irq]