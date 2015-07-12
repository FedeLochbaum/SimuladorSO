import tkinter as tk


class ViewSo(tk.Frame):
    def __init__(self, master=None,shell):
        tk.Frame.__init__(self, master)
        self.pack()
        self.shell = shell
        self.showPrograms()
        

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        
    def showPrograms(self):
        self.programs = tk.Listbox()
        self.programs = tk.Listbox(self.shell.programs(), name='programs')
        self.programs.bind('<<ListboxSelect>>')
    


root = tk.Tk()
app = ViewSo(master=root)
app.master.title("Sistema Operativo Shell")
app.master.minsize(400,200)
app.master.maxsize(600,400)
app.mainloop()