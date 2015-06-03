from clases import SchedullingPolitic


class SchedullingLargePolitic(SchedullingPolitic):
    def __init__(self,queuesManager,memory):
        super.__init__(queuesManager)
        self.memory = memory
            
        
    def tryAddingToReady(self):
        memoriaLibre = self.memory.getFreeSpace()
        for each in self.queuesManager.getWaitingQueue():
            if(each.getInstructionsCount() <= memoriaLibre):
                self.queuesManager.getReadyQueue().put(each)
                self.queuesManager.getWaitingQueue().get(each)
                memoriaLibre = memoriaLibre - each.getInstructionsCount()
        #falta que el irq especifico le diga cuando ..  y revisar que ahce lo que pide con casos de borde