class SchedullingLargePolitic():
    
    def __init__(self):
            pass
            
    def handleReadyProcess(self,pcb,queuesManager):
            queuesManager.getReadyQueue().put(pcb)
            return True
        
    def handleWaitingProgram(self,program,queuesManager):
        queuesManager.getWaitingQueue().put(program)
        return False
        
        
        