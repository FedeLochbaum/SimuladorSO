from AsignacionContinua.RoutineBlock import RoutineBlock
class FirstFit(RoutineBlock):
    
    def __init__(self):
        self.super.__init__()
    
    def blockFor(self,cantidad,listaDeBloques,mmu):
        list = filter(item.size > cantidad,listaDeBloques)#hay que ver que onda
        bloque = list[1]
        mmu.sacarBloque(bloque)
        bloque  = super.recortarBLoque(bloque)
        mmu.agregarABloquesLibres(bloque)
        return bloque
    