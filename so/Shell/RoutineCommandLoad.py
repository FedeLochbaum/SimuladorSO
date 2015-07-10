from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandLoad(RoutineCommand):
    
    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.load.value 
    
    def handle(self, command):
        RoutineCommand.handle(self, command)
        #decirle al irq que lance new process con el nombre del programa que deberia llegar por parametro aca