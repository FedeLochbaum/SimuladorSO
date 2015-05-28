
class IrqTimeOut:
    
    def __init__(self,cpu):
        self.cpu = cpu
        self.processToReady()


    def processToReady(self):
        process = self.cpu.getPcb()
        self.cpu.getIrqHandler().addToReady(process)
        self.cpu.callNext()
