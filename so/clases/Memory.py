class Memory():
    
    
    def __init__(self,space):
        self.instructions = dict()
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

    def freeSpace(self):
        return self.freeSpace