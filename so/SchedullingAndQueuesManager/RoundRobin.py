from SchedullingAndQueuesManager.SchedullingPolitic import SchedullingPolitic


class RoundRobin(SchedullingPolitic):
    def __init__(self,quantum,queuesManager):
        self.quantum = quantum
        self.queuesManager = queuesManager
        

        
    def next(self):
        nextP = self.queuesManager.getReadyQueue().next()
        return nextP
    
    def setPcbInReady(self,pcb):
        self.queuesManager.putInReady(pcb)

    def getqueuesManager(self):
        return self.queuesManager
    
    def getQuantum(self):
        SchedullingPolitic.getQuantum(self)
        return self.quantum
        
    