from clases.RoutineKill import RoutineKill
from clases.RoutineIO import RoutineIO
from clases.RoutineIOFinish import RoutineIOFinish
from clases.RoutineNewprocess import RoutineNewprocess
from clases.RoutineTimeout import RoutineTimeout


class IrqHandler:
    
    def __init__(self,schedullingPolitic):
        self.irqs={}
        self.routines=[RoutineKill(),RoutineTimeout(schedullingPolitic),RoutineNewprocess(),RoutineIO(),RoutineIOFinish(schedullingPolitic)]#falta la de page
        #No se si va a estar el schedulling aca o solo la queueManager
        self.queueManager = schedullingPolitic.getqueuesManager()
        self.schedullingPolitic=schedullingPolitic
        
    def handle(self,irq,cpu,program=None,resource=None): #falta la memoria falta saber que le pasamos en routineIOfinish
        self.put[irq] = (cpu,program,resource)
        #self.anyRoutineHandle(irq,cpu,program,resource)
    
    def put(self,irq):
        self.irqs.append(irq)
        
    def notify(self):
        for (k,irq) in self.irqs:
            self.anyRoutineHandle(k,irq[0],irq[1],irq[2])
        self.irqs = {}
        
    def get(self,index):
        return self.irqs[index]
    
    def cantIrqs(self):
        return self.irqs.__len__()
    
    def addToReady(self,process):
        self.queueManager.putInReady(process)
        
    def addtoIOQueue(self,process):
        self.queueManager.getIOQueue().add(process)
        
    def getNext(self):
        return self.schedullingPolitic.next()
        
    def anyRoutineHandle(self,irq,cpu,program=None,resource=None):
        for routine in self.routines:
            if(routine.canHandle(irq)):
                routine.handle(irq,cpu,program,resource)
                return;
            
    def getQueuesManager(self):
        return self.queueManager
    
    def getQuantum(self):
        return self.schedullingPolitic.getQuantum()