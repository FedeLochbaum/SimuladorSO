class Block:
    
    def __init__(self,inicio,fin):
        self.inicio = inicio
        self.fin = fin
        self.estaLibre = True
        self.instructions = {}
        self.proximaPos = 1
        
        
    def addInstruction(self,instruction):