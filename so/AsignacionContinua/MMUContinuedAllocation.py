from clases.MemoryManager import MemoryManager
from AsignacionContinua.Block import Block
class MMUContinuedAllocation(MemoryManager):
        
    def __init__(self,memory,routineBlock):
        MemoryManager.__init__(self,memory)
        self.bloquesDisponibles = {}
        self.bloquesDisponibles[1] = Block(1,memory.getTotalSpace())
        self.bloquesUsados = {}
        self.routine = routineBlock
        
    def loadProgram(self,program):
        if(self.memoryFree() >= program.getInstructionsCount()):
            if(self.hayBloqueDisponible(program)):
                block = self.routine.getBlockFor(program.getInstructionsCount(),self.bloquesDisponibles,self)
                block.setProgram(program)
                self.bloquesUsados[program.getName()] =  block
                self.addToMemory(program,block)
                
            else:
                self.compactMemory()
                self.loadProgram(program)
        
    def addToMemory(self,program,block):
        self.addinstructionsToMemory(block.getInicio(),block.getFin(),program)
            
    def hayBloqueDisponible(self,program):
        for (dirBase,block) in self.bloquesDisponibles.items(): 
            if(block.size() > program.getInstructionsCount()):
                return True
        return False
    
    def traerBloqueSegunRutina(self,cantidad):
        return self.routine.blockFor(cantidad,self.bloquesDisponibles,self)        
       
    def cleanMemory(self,program):
        block1 = self.bloquesUsados.get(program.getName())
        self.bloquesUsados.__delitem__(program.getName())
        block = Block(block1.getInicio(),block1.getFin())
        self.agregarABloquesLibres(block)
        #para que sea mas eficiente.. no ahce falta borrarlas de verdad .. sino que sepa que se puede volver a escribir
        self.memory.setFreeSpace(self.memory.getFreeSpace()+block1.size())
        self.reordenarBloques()
        
    def sacarBloque(self,block):
        self.bloquesDisponibles.__delitem__(block.getInicio())
    '''def reordenarBloques(self):
        for (dirBase,block) in self.bloquesDisponibles.items():
            sigBLock = self.bloquesDisponibles.get(block.getFin()+1)
            if(sigBLock != None):
                inicio = block.getInicio()
                fin = sigBLock.getFin()
                newBlock = Block(inicio,fin)
                self.sacarBloque(block)
                self.sacarBloque(sigBLock)
                self.bloquesDisponibles[inicio]= newBlock
    '''
    def reordenarBloques(self):
        if(self.bloquesDisponibles.__len__() > 0):
            newMap = {}
            iniNewBlock = (list( self.bloquesDisponibles.keys() )) [0]        # dir donde empieza el primer bloque
            finNewBlock = self.bloquesDisponibles[iniNewBlock].getFin()     # dir donde termina 

            for (dirBase,block) in self.bloquesDisponibles.items():
                if (finNewBlock+1 < dirBase):
                    newBlock = Block(iniNewBlock, finNewBlock) 
                    newMap[iniNewBlock] = newBlock 
                    iniNewBlock = block.getInicio()
                    finNewBlock = block.getFin()
                else: 
                    finNewBlock = block.getFin()

            self.bloquesDisponibles = newMap
                    
    def compactMemory(self):
        proxIns = 0
        #recorre el map de bloquesUsados reasignandolos A memory 
        for (k,block) in self.bloquesUsados.items():
            tam = block.size()
            tamF = proxIns + tam
            self.addinstructionsToMemory(proxIns, tamF, block.getProgram())
            block.setInicio(proxIns)
            block.setFin(tamF)
            proxIns = proxIns + tam + 1
        
        #aca reasigno el nuevo gran Bloque disponible
        self.bloquesDisponibles[proxIns] = Block(proxIns,self.memory.getTotalSpace())
            
    def agregarABloquesLibres(self,block):
        self.bloquesDisponibles[block.getInicio()] =  block
        
    def addinstructionsToMemory(self,inicio,final,program):
        i = inicio
        for instruction in program.getInstructions():
            if(i <= final):
                self.memory.put(i,instruction)
                i = i+1