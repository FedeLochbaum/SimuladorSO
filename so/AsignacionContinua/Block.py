class Block:
    
    def __init__(self,inicio,fin):
        self.inicio = inicio
        self.fin = fin
        self.proximaPos = 1
        self.isFree = True
    
    def size(self):
        return self.fin - self.inicio
    
    def getInicio(self):
        return self.inicio
    
    def setFin(self,fin):
        self.fin = fin
        
    def setInicio(self,inicio):
        self.inicio = inicio
    
    def getFin(self):
        return self.fin
    
    def getIsFree(self):
        return self.isFree
    
    def setPcb(self,pcb):
        self.pcb = pcb
        
    def getPcb(self):
        return self.pcb
    
    