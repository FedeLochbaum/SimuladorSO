class SchedullingPolitic:
    
    def __init__(self,queuesManager):
        self.queuesManager = queuesManager
    
    def next(self):
        return self.queuesManager.getReady().firstQ()


     