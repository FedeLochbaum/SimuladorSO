from heapq import heappush
from heapq import heappop

class ReadyQueuePriority:
    def __init__(self):
        self.ready = []
   
    def put(self,elemet):
        heappush(self.ready,[elemet.getPriority(), elemet])

    def get(self):
        return self.ready.heappop(self.ready)
            