from AsignacionContinua.RoutineBlock import RoutineBlock
class WorstFit(RoutineBlock):
    
    def __init__(self):
        self.super.__init__()
    
    def blockFor(self,cantidad,listaDeBloques):
        list = filter(item.size > cantidad,listaDeBloques)#hay que ver que onda
        blockR = Block(1,100000000000000000000)
        for block in list:
            if(block.size > blockR.size):
                blockR = block
        
        return blockR
    
        #HORRIBLE... LO SE.. A VER DESP