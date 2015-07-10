from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandLoad(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.load.value 
    
    def handle(self, command,param=None,kernel=None):
        RoutineCommand.handle(self, command)
        param=str(param)
        return kernel.newProcess(param)