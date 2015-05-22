from collections import deque
class FIFOReadyQueue:

    def __init__(self):
        self.readyQueue = deque()

    def put(self,elemet):
        self.readyQueue.append(elemet)

        
    def next(self): 
        return self.readyQueue.popleft()
        
    
    

   