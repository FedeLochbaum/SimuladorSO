from clases.SchedullingPolitic import SchedullingPolitic 
from clases.Timer import Timer


class RoundRobin(SchedullingPolitic):
    def __init__(self,quantum,queuesManager,cpu):
        self.quantum = quantum
        self.queuesManager = queuesManager
        self.temp = Timer(self.quantum,cpu)
        

        
    def next(self):
        next = self.queuesManager.getReadyQueue().next()
        self.temp.restart()
        return next


        
