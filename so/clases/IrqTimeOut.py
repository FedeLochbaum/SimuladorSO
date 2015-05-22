
class IrqTimeOut:
    
    def __init__(self,process,irqHandler):
        self.process = process
        self.irqHandler = irqHandler
        self.processToReady()


    def processToReady(self):
        self.irqHandler.addToReady(self.process)
