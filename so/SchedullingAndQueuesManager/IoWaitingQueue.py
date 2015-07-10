class IoWaitingQueue:

    def __init__(self):
        self.waiting = []
     
    def add(self, process):
        self.waiting.append(process)
      
    def remove(self, process):
        self.waiting.pop(self.waiting.index(process))
        
    def getWaiting(self):
        return self.waiting
