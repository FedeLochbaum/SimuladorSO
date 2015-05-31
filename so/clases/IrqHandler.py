class IrqHandler:
    
    def __init__(self,schedullinPolitic):
        self.irqs=[]
        self.queueManager = schedullinPolitic.getqueuesManager()
        self.schedullingPolitic=schedullinPolitic
        
    def handle(self,irq):
        self.put(irq)
        irq.execute()
    
    def put(self,irq):
        self.irqs.append(irq)
        
    def get(self,index):
        return self.irqs[index]
    
    def cantIrqs(self):
        return self.irqs.__len__()
    
    def addToReady(self,process):
        self.queueManager.putInReady(process)
        
    def addtoIOQueue(self,process):
        self.queueManager.getIOQueue().add(process)
        
    def getNext(self):
        self.schedullingPolitic.next()