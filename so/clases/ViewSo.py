import tkinter as tk
from tkinter.constants import RIGHT
from tkinter import Label


class ViewSo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.shell = None
        self.master.title("Sistema Operativo Shell")
        self.master.minsize(400,200)
        self.master.maxsize(600,400)
        self.programSelected = None 
        
    def showPrograms(self):
        self.programs = tk.Listbox(self,width =20,height = 10,name = "programs")
        for program in [2,3,4]:
            self.programs.insert(program)
        self.programs.bind('<<ListboxSelect>>',self.seleccionarProgram)
        self.programs.pack(side=RIGHT)
        
        self.buttonLoad = tk.Button(self)
        self.buttonLoad["text"] = "Load Program"
        self.buttonLoad["command"] = self.load()
        self.buttonLoad.pack(side=RIGHT)
    
    def showConsole(self):
        self.line = Label(self)
        #self.line.bind(sequence, func, add)
    
    def seleccionarProgram(self,evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.programSelected = value
    
    def setShell(self,shell):
        self.shell = shell
        self.showPrograms()
        self.showConsole()
        
    def load(self):
        #self.shell.load(self.programSelected)
        pass
