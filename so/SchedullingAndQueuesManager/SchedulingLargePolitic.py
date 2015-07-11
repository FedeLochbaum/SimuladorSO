class SchedullingLargePolitic():
    
    def __init__(self):
            pass
        
    def handleProcess(self,program,pcb,queuesManager,memoryManager):
        #if(not memoryManager.addinstructionsToMemory(program)):
        if(memoryManager.loadProgram(program)):
            queuesManager.getReadyQueue().put(pcb)
            return True
        
        queuesManager.getWaitingQueue().put(pcb)
        return False
        
        
        