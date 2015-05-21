from clases import SchedullingPolitic


class SchedullingLargePolitic(SchedullingPolitic):
    def __init__(self,queuesManager,memory):
        super.__init__(queuesManager)
        self.memory = memory
        
    
    def next(self):
        #tal ves... deberia observar a la memoria y cuando haya espacio agergar el proceso de waiting a ready