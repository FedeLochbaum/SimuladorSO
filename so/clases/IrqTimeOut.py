
class IrqTimeOut:
    
    def __init__(self,cpu):
        self.cpu = cpu
        


    def execute(self):
        process = self.cpu.getPcb()
        self.cpu.getIrqHandler().addToReady(process)
        self.cpu.callNext()
