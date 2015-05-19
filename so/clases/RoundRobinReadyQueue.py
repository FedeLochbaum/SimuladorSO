
class RoundRobinReadyQueue :
    def __init__(self):
        
        self.procesos= dict()

    def add(self,pid,elemet):
        self.procesos[pid] = elemet

    def remove(self,pid):
        self.instructions.__delitem__(pid)


    def getReadyQueue(self):
        return self.procesos