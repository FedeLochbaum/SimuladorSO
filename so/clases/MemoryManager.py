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
            return False
    
    def memoryFree(self):
        return self.memory.getFreeSpace()
