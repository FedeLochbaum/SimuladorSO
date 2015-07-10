from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandLs(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.ls.value 
    
    def handle(self, command):
        RoutineCommand.handle(self, command)
       #mostrar lista de directorios dentro del directorio actual