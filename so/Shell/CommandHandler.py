from Shell.RoutineCommandCd import RoutineCommandCd
from Shell.RoutineCommandHelp import RoutineCommandHelp
from Shell.RoutineCommandLoad import RoutineCommandLoad
from Shell.RoutineCommandLs import RoutineCommandLs
from Shell.RoutineCommandShow import RoutineCommandShow


class CommandHandler:
    def __init__(self):
        self.commandRoutines =[RoutineCommandHelp(),RoutineCommandCd(),RoutineCommandLs(),RoutineCommandShow(),RoutineCommandLoad()]
        
        
        
    def handle(self,command,param=None,kernel=None):
        return self.anyRoutineHandle(command,param,kernel)
    
    def anyRoutineHandle(self,command,param=None,kernel=None):
        for routine in self.commandRoutines:
            if routine.canHandle(command):
                return routine.handle(command,param,kernel)

        return False
