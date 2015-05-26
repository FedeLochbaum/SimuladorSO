from clases.SchedullingPolitic import SchedullingPolitic

class FIFO(SchedullingPolitic):
    def __init__(self,queuesManager):
        self.queuesManager = queuesManager
        


    def next(self):
        return self.queuesManager.getReadyQueue().next()

    def getqueuesManager(self):
        return self.queuesManager    
