class Timer:


    def __init__(self,quantum,cpu):
        self.quantum = quantum
        self.count = quantum
        self.cpu = cpu



    def notifyCycle(self):
        self.count--
        if(self.count == 0):
            self.cpu.timeOut()

    def restart(self):
        self.count = self.quantum


