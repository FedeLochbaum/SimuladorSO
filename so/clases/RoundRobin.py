from clases import SchedullingPolitic, Timer


class RoundRobin(SchedullingPolitic):
    def __init__(self,quantum,queuesManager):
        self.quantum = quantum
        self.queuesManager = queuesManager
        self.temp = Timer(self.quantum)
        

        
    def next(self):
        next = self.queuesManager.getReadyQueue().next()
        self.temp.restart()
        return next


        
