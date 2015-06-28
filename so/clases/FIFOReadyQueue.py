from collections import deque
class FIFOReadyQueue:

    def __init__(self):
        self.readyQueue = deque()

    def put(self,elemet):
        self.readyQueue.append(elemet)

        
    def next(self): 
        if(self.readyQueue.__len__()>0):
            return self.readyQueue.popleft()
        
    def pcbCount(self):
        return self.readyQueue.__len__()