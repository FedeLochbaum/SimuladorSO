from tkinter import Label, Scrollbar, Frame, StringVar
from tkinter._fix import v
from tkinter.constants import RIGHT, TOP, BOTTOM, LEFT, CENTER
from tkinter.ttk import Entry

import tkinter as tk
from pydoc_data.topics import topics


class ViewSo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(side=BOTTOM)
        self.shell = None
        self.master.title("Sistema Operativo Shell")
        self.master.minsize(150,200)
        self.master.maxsize(1000,300)
        self.programSelected = None
        
    def showPrograms(self):
        frame = Frame()
        frame.pack(side=RIGHT)
        self.label = Label(frame,text= "Todos los Programas en Disco")
        self.label.pack(side=TOP)
        self.buttonLoad = tk.Button(frame,text= "Load Program",command = self.load)
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
        self.prompCm = StringVar()
        self.prompFile = StringVar()
        frame = Frame()
        frame.pack(side=LEFT)
        self.buttonLoadCommand = tk.Button(frame,text= "Load Command", command = self.runCommand)
        self.buttonLoadCommand.pack(side=BOTTOM, fill=tk.BOTH)
        self.titleRoot = Label(frame,text="Direccion Actual :")
        self.titleRoot.pack(side =TOP)
        self.line = Label(frame,text=self.shell.getRoot())
        self.line.pack(side=TOP)
        self.com = Entry(frame, textvariable=self.prompCm,width =3)
        self.com.pack(side =LEFT)
        self.file = Entry(frame, textvariable=self.prompFile,width =15)
        self.file.pack(side =LEFT)
        self.showViewData(self)
        
        
    def showViewData(self,master):
        self.error = Label(master,text="")
        self.error.pack(side=BOTTOM)
    
    def runCommand(self):
        self.error["text"] = self.shell.readCommand(self.prompCm.get(),None,self.prompFile.get())
        self.line["text"] = self.shell.getRoot()
        self.prompCm.set("")
        self.prompFile.set("")
        print(self.error["text"])
        
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
