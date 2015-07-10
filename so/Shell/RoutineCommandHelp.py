from Shell.RoutineCommand import RoutineCommand
from Shell.typeCommand import Command


class RoutineCommandHelp(RoutineCommand):
    MESSAGE='Bienvenido a la ayuda del Sistema Operativo, tiene los siguientes comando disponibles:\n-help\n-?\n-load\n'
    #Modificar texto

    def canHandle(self, command):
        RoutineCommand.canHandle(self, command)
        command=str(command)
        return command==Command.help1.value or command==Command.help2.value or command==Command.help3.value 
    
    def handle(self, command):
        RoutineCommand.handle(self, command)
        return self.MESSAGE
        

        