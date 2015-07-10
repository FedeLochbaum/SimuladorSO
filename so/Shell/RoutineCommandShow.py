from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandShow(RoutineCommand):
    

    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.show.value 
    
    def handle(self, command):
        RoutineCommand.handle(self, command)
         #mostrar un file.. osea como si se ejecutara con un editor