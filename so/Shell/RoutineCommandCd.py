from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandCd(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.cd.value 
    
    def handle(self, command,dir):
        RoutineCommand.handle(self, command)
        #aca hay que acceder a ese directorio 
    