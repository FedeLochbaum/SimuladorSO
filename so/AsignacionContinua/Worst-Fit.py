from AsignacionContinua.RoutineBlock import RoutineBlock
class Worst-Fit(RoutineBlock):
    
    def __init__(self):
        self.super.__init__()
    
    def blockFor(self,cantidad,listaDeBloques):
        list = filter(item.size > cantidad,listaDeBloques)***hay que ver que onda
        for block in list:
        