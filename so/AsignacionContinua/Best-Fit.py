from AsignacionContinua.RoutineBlock import RoutineBlock
class BestFit(RoutineBlock):
    
    def __init__(self):
        self.super.__init__()
    
    def blockFor(self,cantidad,listaDeBloques,mmu):
        list = filter(item.size > cantidad,listaDeBloques)#hay que ver que onda
        blockR = Block(1,100000000000000000000)
        for block in list:
            if(block.size < blockR.size):
                blockR = block
        

        mmu.sacarBloqueDeLista(bloque)
        bloque  = super.recortarBLoque(bloque)
        mmu.agregarBloqueALista(bloque)
        return blockR       
            