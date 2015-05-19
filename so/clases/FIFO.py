from clases import SchedullingPolitic

class FIFO(SchedullingPolitic):
    def __init__(self):
        pass
        


    def next(self,colaReady):
        first = colaReady.first()
        colaReady.deque()
        return first

        
