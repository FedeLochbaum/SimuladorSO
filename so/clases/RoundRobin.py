from clases.SchedullingPolitic import SchedullingPolitic 

class RoundRobin(SchedullingPolitic):
    def __init__(self,quantum,queuesManager,timer):
        self.quantum = quantum
        self.queuesManager = queuesManager
        self.temp = timer
        self.temp.setQuantum(quantum)
        

        
    def next(self):
        nextP = self.queuesManager.getReadyQueue().next()
        self.temp.restart()
        return nextP
    
    def setPcbInReady(self,pcb):
        self.queuesManager.putInReady(pcb)

    def getqueuesManager(self):
        return self.queuesManager
        
    