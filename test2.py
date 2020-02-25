import tkinter as tk
from tkinter import*
import tkinter.messagebox
from tkinter.ttk import *
import time
from subprocess import call

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master =master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.progress=Progressbar(self,orient=HORIZONTAL,length=100,mode="determinate")
        self.progress.pack()
        self.buttonkaffee =tk.Button(self)
        self.buttonkaffee["text"]= "Kaffee rauslassen"
        self.buttonkaffee["command"] = self.kaffee
        self.buttonkaffee.pack(side="top")
        self.quit =tk.Button(self,text="Quit",fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")
    def kaffee(self):
        self.progress["value"]=0
        self.progress["maximum"]=100
  
        self.progress["value"]=20
        self.progress.update()
        time.sleep(1)
        self.progress["value"]=40
        self.progress.update()
        time.sleep(1)

        self.progress["value"]=60
        self.progress.update()
        time.sleep(1)
        self.progress["value"]=80
        self.progress.update()
        time.sleep(1)
        self.progress["value"]=100
        self.progress.update()
        time.sleep(1)
        self.progress["value"]=0
        self.progress.update()
        #tk.messagebox.showinfo("Alert Message", "Kaffee ist unterwegs!")
        

root = tk.Tk()
root.title("Kaffeemaschine")
root.attributes('-fullscreen', True)
app=Application(master=root)
app.mainloop()
