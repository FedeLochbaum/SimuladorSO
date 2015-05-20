import heapq

class ReadyQueuePriority:
    def __init__(self):
        self.ready = heapq
   
    def put(self,elemet):
        self.ready.heappush(self.ready, elemet)

    def get(self):
        return self.ready.heappop(self.ready)
            