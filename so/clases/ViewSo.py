from tkinter import Label, Scrollbar, Frame
from tkinter.constants import RIGHT, TOP, BOTTOM, LEFT

import tkinter as tk


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
        frame = Frame()
        frame.pack(side=RIGHT)
        label = Label(self,name= "todos los programas en Disco")
        self.buttonLoad = tk.Button(frame)
        self.buttonLoad["text"] = "Load Program"
        self.buttonLoad["command"] = self.load()
        self.buttonLoad.pack(side=BOTTOM, fill=tk.BOTH)
        
        
        self.scrollbar = Scrollbar(frame, orient=tk.VERTICAL)
        self.programs = tk.Listbox(frame,width =20,height = 5,name = "programs",yscrollcommand=self.scrollbar.set)
        for program in self.shell.programs():
            self.programs.insert(tk.END,program)
        self.scrollbar.config(command=self.programs.yview())
        self.scrollbar.pack(side=RIGHT,fill=tk.Y)
        self.programs.pack(side=TOP)
        self.programs.bind('<<ListboxSelect>>',self.onselect)
        
        

    
    def showConsole(self):
        #self.line = Label(self)
        #self.line.pack(side=LEFT)
        #self.line.bind(sequence, func, add)
        pass
    def onselect(self,evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.programSelected = value
    
    def setShell(self,shell):
        self.shell = shell
        self.showPrograms()
        self.showConsole()
        
    def load(self):
        if(self.programSelected != None):
            self.shell.readCommand('load',self.programSelected)
