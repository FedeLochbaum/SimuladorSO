class QueuesManager :
    
    def __init__(self,readyQueue,waitingQueue):
        self.readyQueue = readyQueue
        self.waitingQueue = waitingQueue

        
        
    def getReadyQueue(self):
        return self.readyQueue
    
    def getWaitingQueue(self):
        return self.waitingQueue
    
    