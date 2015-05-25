class IrqHandler:
    
    def __init__(self,queueManager):
        self.irqs=[]
        self.queueManager = queueManager
        
    def handle(self,irq):
        self.put(irq)
        #irq.execute()
    
    def put(self,irq):
        self.irqs.append(irq)
        
    def get(self,index):
        return self.irqs[index]
    
    def cantIrqs(self):
        return self.irqs.__len__()
    
    def addToReady(self,process):
        self.queueManager.getReadyQueue().put(process)#a observar.. puede ser mas simple