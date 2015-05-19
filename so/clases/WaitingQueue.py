class WaitingQueue :
     
    def __init__(self,scheduller):
        self.wait = []
        
     
    def add(self, process):
        self.wait.append(process)

    def remove(self, process):
        self.wait.pop(self.wait.index(process ))

    def getWait(self):
        return self.wait

