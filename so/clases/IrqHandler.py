class IrqHandler:
    
    def __init__(self):
        self.irqs=[]
        
    def handle(self,irq):
        self.put(irq)
    
    def put(self,irq):
        self.irqs.append(irq)
        
    def get(self,index):
        return self.irqs[index]
    
    def cantIrqs(self):
        return self.irqs.__len__()