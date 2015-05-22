from clases import SchedullingPolitic

class FIFO(SchedullingPolitic):
    def __init__(self,queuesManager):
        self.queuesManager = queuesManager
        


    def next(self):
        return self.queuesManager.getReadyQueue().next()

        
