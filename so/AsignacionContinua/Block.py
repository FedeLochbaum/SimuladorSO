class Block:
    
    def __init__(self,inicio,fin):
        self.inicio = inicio
        self.fin = fin
        self.proximaPos = 1
    
    def size(self):
        return self.fin - self.inicio