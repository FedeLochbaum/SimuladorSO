from Shell.RoutineCommandHelp import RoutineCommandHelp


class CommandHandler:
    def __init__(self):
        self.commandRoutines =[RoutineCommandHelp()]
        
        
        
    def handle(self,command):
        return self.anyRoutineHandle(command)
    
    def anyRoutineHandle(self,command):
        for routine in self.commandRoutines:
            if routine.canHandle(command):
                return routine.handle(command)

        return False
