import tkinter as tk


class ViewSo(tk.Frame):
    def __init__(self, master=None,shell):
        tk.Frame.__init__(self, master)
        self.pack()
        self.shell = shell
        self.master.title("Sistema Operativo Shell")
        self.master.minsize(400,200)
        self.master.maxsize(600,400)
        self.showPrograms()
        self.programSelected = None 
        
    def showPrograms(self):
        self.programs = tk.Listbox()
        for program in self.shell.programs():
            self.programs.insert(program)
        self.programs.bind('<<ListboxSelect>>',self.programSelected)
        
        self.buttonLoad = tk.Button(self)
        self.buttonLoad["text"] = "Load Program"
        self.buttonLoad["command"] = self.load()
        self.buttonLoad.pack(side="top")
    
    def load(self):
        #self.shell.load(self.programSelected)
        pass

root = tk.Tk()
app = ViewSo(master=root)
app.mainloop()