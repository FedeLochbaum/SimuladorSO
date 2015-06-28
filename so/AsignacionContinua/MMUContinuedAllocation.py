from clases.MemoryManager import MemoryManager
from AsignacionContinua.Block import Block
from _overlapped import NULL
class MMUContinuedAllocation(MemoryManager):
        
    def __init__(self,memory,routineBlock):
        self.super.__init__(memory)
        self.bloquesDisponibles = {}
        self.bloquesDisponible[1] = Block(1,memory.space)
        self.bloquesUsados = {}
        self.routine = routineBlock
        
    def loadProgram(self,pcb):
        if(self.memoryFree()>pcb.getFinalPc):
            if(self.hayBloqueDisponible()):
                block = self.getBlockFor(pcb.getFinalPc())
                block.setPcb(pcb)
                self.addToMemory(pcb,block)
            else:
                self.compactMemory()
                self.loadProgram(pcb)
        
    def addToMemory(self,pcb,block):
        self.addinstructionsToMemory(block.getInicio(),block.getFin(),pcb)
            
    def hayBloqueDisponible(self,pcb):
        for dirBase,block in self.bloquesDisponibles: 
            if(block.size() > pcb.getFinalPc()):
                return True
        return False
    
    def traerBloqueSegunRutina(self,cantidad):
        return self.routine.blockFor(cantidad,self.bloquesDisponibles,self)        
       
    def cleanMemory(self,pcb):
        bloque = self.bloquesUsados.get(pcb.getPid())
        self.agregarABloquesLibres(bloque)
        self.reordenarBloques()
        
    def sacarBloque(self,block):
        self.bloquesDisponibles.__delitem__(block.getInicio())
    def reordenarBloques(self):
        for k,block in self.bloquesDisponibles:
            sigBLock = self.bloquesDisponibles.get(block.getFin()+1)
            if(sigBLock != NULL):
                inicio = block.getInicio()
                fin = sigBLock.getFin()
                newBlock = Block(inicio,fin)
                self.sacarBloque(block)
                self.sacarBloque(sigBLock)
                self.bloquesDisponibles__setitem__(inicio,newBlock)
                    
    def compactMemory(self):
        proxIns = 0
        #recorre el map de bloquesUsados reasignandolos A memory 
        for k,block in self.bloquesUsados:
            tam = block.size()
            tamF = proxIns + tam
            self.addinstructionsToMemory(proxIns, tamF, block.getPcb())
            block.setInicio(proxIns)
            block.setFin(tamF)
            proxIns = proxIns + tam + 1
        
        #aca reasigno el nuevo gran Bloque disponible
        self.bloquesDisponibles__setitem__(proxIns,Block(proxIns,self.memory.space()))
            
    def agregarABloquesLibres(self,block):
        self.bloquesDisponibles.__setitem__(block.getInicio(), block)
        
    def addinstructionsToMemory(self,inicio,final,pcb):
        i = inicio 
        for instruction in pcb.getInstructions():
            if(i <= final):
                self.memory.put(i,instruction)
                i = i+1
            #hay que ver.. creoque esta bien