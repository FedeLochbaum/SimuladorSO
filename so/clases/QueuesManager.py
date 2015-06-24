class QueuesManager :
    
    def __init__(self,readyQueue,waitingQueue,waitingIO):
        self.readyQueue = readyQueue
        self.waitingQueue = waitingQueue
        self.waitingIO = waitingIO

        
        
    def getReadyQueue(self):
        return self.readyQueue
    
    def getWaitingQueue(self):
        return self.waitingQueue
    
    def putInReady(self,process):
        self.readyQueue.put(process)
        
    def getIOQueue(self):
        return self.waitingIO    