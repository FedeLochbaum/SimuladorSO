import logging


class SchedullingLargePolitic():
    
    def __init__(self):
        logging.basicConfig(filename='logSo.log',level=logging.DEBUG)
            
    def handleReadyProcess(self,pcb,queuesManager):
            logging.debug('Added process %s to Ready Queue' % pcb.getName())
            queuesManager.getReadyQueue().put(pcb)
            return True
        
    def handleWaitingProgram(self,program,queuesManager):
        logging.debug('Added program %s to Waiting Queue' % program.getName())
        queuesManager.getWaitingQueue().put(program)
        return False
        
        
        