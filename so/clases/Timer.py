class Timer:


    def __init__(self,cpu):
        self.quantum = None
        self.count = None
        self.cpu = cpu

    def setQuantum(self,quantum):
        self.quantum = quantum
        self.count = quantum

    def notifyCycle(self):
        self.count-=1
        if(self.count == 0):
            self.cpu.timeOut()

    def restart(self):
        self.count = self.quantum


