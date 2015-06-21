class Block:
    
    def __init__(self,inicio,fin):
        self.inicio = inicio
        self.fin = fin
        self.estaLibre = True
        self.instructions = {}
        self.proximaPos = 1
        
        
    def addInstruction(self,instruction):
        self.instructions[self.proximaPos] = instruction
        self.proximaPos = self.proximaPos + 1
        
    def size(self):
        return self.fin - self.inicio