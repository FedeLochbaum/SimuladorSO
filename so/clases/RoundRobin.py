from clases import SchedullingPolitic, Timer


class RoundRobin(SchedullingPolitic):
    def __init__(self,quantum,queuesManager):
        self.quantum = quantum
        self.queuesManager = queuesManager
        self.temp = Timer(self.quantum)
        

        
    def next(self):
        first = self.queuesManager.getReadyQueue().first()
        self.queuesManager.getReadyQueue().deque()
        self.temp.restart()
        return first


        
