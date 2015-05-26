class Memory():
    
    
    def __init__(self,space):
        self.instructions = {}
        self.freeSpace=space
    
    def put(self,celda,instruction):
        self.instructions[celda] = instruction
        self.freeSpace-=1

    def remove(self,cell):
        self.instructions.__delitem__(cell)
        self.freeSpace+=1

    def getInstructions(self):
        return self.instructions

    def get(self,cell):
        return self.instructions[cell]
        
    def getNextIndex(self):
        return self.instructions.__len__()+1

    def getFreeSpace(self):
        return self.freeSpace
    
    def borrarInstruccionesDe(self,pcb):
        
        for i in range(0,pcb.getFinalPc()):
            print(i)
            self.instructions[pcb.getBaseDir()+i]=None