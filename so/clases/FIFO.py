from clases import SchedullingPolitic

class FIFO(SchedullingPolitic):
    def __init__(self,queuesManager):
        self.queuesManager = queuesManager
        


    def next(self):
        first = self.queuesManager.getReadyQueue().first()
        self.queuesManager.getReadyQueue().deque()
        return first

        
