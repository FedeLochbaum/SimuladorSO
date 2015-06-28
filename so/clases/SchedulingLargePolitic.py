class SchedullingLargePolitic():
    
    def __init__(self):
            pass
        
    def handleProcess(self,program,pcb,queuesManager,memoryManager):
        if(not memoryManager.addinstructionsToMemory(program)):
            queuesManager.getWaitingQueue().put(pcb)
            return False
        queuesManager.getReadyQueue().put(pcb)
        return True
        
        