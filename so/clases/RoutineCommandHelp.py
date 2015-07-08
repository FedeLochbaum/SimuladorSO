from clases.RoutineCommand import RoutineCommand
from clases.typeCommand import Command


class RoutineCommandHelp(RoutineCommand):
    MESSAGE='Bienvenido a la ayuda del Sistema Operativo, tiene los siguientes comando disponibles:\n-help\n-?\n-load\n'


    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.help1.value or command==Command.help2.value
    
    def handle(self, command):
        RoutineCommand.handle(self, command)
        return self.MESSAGE
        

        