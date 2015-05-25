class MemoryManager:
    
    def __init__(self,memory):
        self.memory=memory
       
    def getMemory(self):
        return self.memory
    
    def addinstructionsToMemory(self,program):
        if(self.memoryFree()>=program.getInstructionsCount()):       
            for instruction in program.getInstructions():
                index=self.memory.getNextIndex() 
                print(index)
                self.memory.put(index,instruction)
            return True;   
        else:
            return False #TODO : aca deberia agergarlo a la cola WAITING
                        # Fijate que son solo las instrucciones del pcb, y previamente en kenrel se agrego a ready, waiting o running
    
    def memoryFree(self):
        return self.memory.getFreeSpace()
    
    def borrarRegistrosDe(self,pcb):
        self.memory.borrarInstruccionesDe(pcb)