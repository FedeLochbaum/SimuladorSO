from AsignacionContinua.RoutineBlock import RoutineBlock
class First-Fit(RoutineBlock):
    
    def __init__(self):
        self.super.__init__()
    
    def blockFor(self,cantidad,listaDeBloques):
        list = filter(item.size > cantidad,listaDeBloques)***hay que ver que onda
            return list.first()  ***nose si es asi