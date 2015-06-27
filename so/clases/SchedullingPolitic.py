class SchedullingPolitic:
    
    def __init__(self,queuesManager):
        self.queuesManager = queuesManager
    
    def next(self):
        return self.queuesManager.getReadyQueue().next()
    
    
    def getqueuesManager(self):
        return self.queuesManager  
    
    def setPcbInReady(self,pcb):
        self.queuesManager.getReadyQueue().put(pcb)