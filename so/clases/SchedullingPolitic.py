class SchedullingPolitic:
    
    def __init__(self,queuesManager):
        self.queuesManager = queuesManager
    
    def next(self):
        return self.queuesManager.getReady().firstQ()


    def interruptProcess(self,process,cpu):
        if process.haveNextInstruction():
            cpu.loadPrceso((process.getPid(), process.avanzarSigInstruccion()))
            #Ver esto
        else:
            return False
        
    def getQueuesManager(self):
        return self.queuesManager    