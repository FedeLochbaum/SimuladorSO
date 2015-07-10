class MemoryManager:
    
    def __init__(self,memory):
        self.memory=memory
       
    def getMemory(self):
        return self.memory
    
    def addinstructionsToMemory(self,program):
        if(self.memoryFree()>=program.getInstructionsCount()):       
            for instruction in program.getInstructions():
                index=self.memory.getNextIndex() 
                self.memory.put(index,instruction)
            return True;   
        else:
            return False #TODO : aca deberia agergarlo a la cola WAITING
                        # Fijate que son solo las instrucciones del pcb, y previamente en kenrel se agrego a ready, waiting o running
    
    def memoryFree(self):
        return self.memory.getFreeSpace()
    
    def cleanMemory(self,pcb):
        self.memory.cleanMemory(pcb)
        
    def getInstructionsCount(self):
        return self.memory.getInstructionsCount()
    
    def getInstruction(self,index):
        return self.memory.get(index)
    def esContinua(self):
        #por defecto
        return True