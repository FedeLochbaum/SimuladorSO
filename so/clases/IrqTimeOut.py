from clases.IrqHandler import IrqHandler
class IrqTimeOut:
    
    def __init__(self,process,irqHandler):
        self.process = process
        self.irqHandler = irqHandler
        self.processToReady()


    def processToReady(self):
        self.IrqHandler.addToReady(self.process)
