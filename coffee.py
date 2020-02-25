import tkinter as tk
from tkinter import*
import tkinter.messagebox
from tkinter.ttk import *
import time
from subprocess import call
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import query
import mysql.connector


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master =master
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        self.quit =tk.Button(self,text="Quit",fg="red", command=self.master.destroy)
        self.quit.pack(side="right")
        self.buttonstatus =tk.Button(self)
        self.buttonstatus["text"]= "Wasser vorheizen"
        self.buttonstatus["command"]= self.status
        self.buttonstatus.pack()
        self.progress=Progressbar(self,orient=HORIZONTAL,length=100,mode="determinate")
        self.progress.pack(pady="8",fill='x')
        self.buttonkaffeeklein =tk.Button(self)
        self.buttonkaffeeklein["text"]= "Kleiner Kaffee"
        self.buttonkaffeeklein["height"]= 6
        #self.buttonkaffeeklein["width"]= "x"
        self.buttonkaffeeklein["command"] = self.kaffeeklein
        self.buttonkaffeeklein["state"]= "disabled"
        self.buttonkaffeegross =tk.Button(self)
        self.buttonkaffeegross["text"]= "Großer Kaffee"
        self.buttonkaffeegross["height"]= 6
        #self.buttonkaffeegross["width"]= 12
        self.buttonkaffeegross["command"] = self.kaffeegross
        self.buttonkaffeegross["state"]= "disabled"
        self.buttonkaffeegross.pack(side="left")
        self.buttonkaffeeklein.pack(side="right")
        self.ausgabe =tk.Label(self)
        self.ausgabe["text"]="Hallo"
        self.ausgabe.pack()

    def rfid(self, chipid,preis):
        if chipid==129353831365:
                print("Hallo Georg")
                self.ausgabe["text"]="Name Georg"
        print(chipid)
        print(preis)

    def warteaufkarte(self):
        try:
                id, text = reader.read()
                
        finally:
                GPIO.cleanup()
        return id

    def fortschritt(self):
        #Progress Bar
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

    def kaffeemachen(self,kaffee,preis):
        
        self.ausgabe["text"]="Chipkarte anlegen"
        kartenid= str(self.warteaufkarte())
        connection=query.connect()
        auth = query.authenticate(connection, kartenid)

        if not auth:
            disconnect(connection)
            self.ausgabe["text"]="Chipkarte nicht erkannt"
            return False
        
        id, fname, lname, cnumber, pref, debt = query.get_person_entries(connection, kartenid)


        


        allowed = query.is_allowed(debt)
        if not allowed:
            self.ausgabe["text"]="Bezahlen Sie ihre Schulden"
            return False
        else:
            query.get_coffee(cnumber, kaffee)
            query.update_debt(connection, cnumber, debt, preis)
            self.ausgabe["text"]=round(dept+preis,1)
            self.fortschritt()

        query.disconnect(connection)

    def kaffeeklein(self):

        kaffee="klein"
        preis=0.7
        
        self.kaffeemachen(kaffee,preis)
        
    def kaffeegross(self):
        kaffee="groß"
        preis=1.0
        self.kaffeemachen(kaffee,preis)
        
    def status(self):
        self.buttonstatus["state"]= "disabled"

 
        #Button aktivieren
        self.buttonkaffeegross["state"]= "normal"
        self.buttonkaffeeklein["state"]= "normal"

        


root = tk.Tk()
reader = SimpleMFRC522()
root.title("Kaffeemaschine")
root.attributes('-fullscreen', True)
app=Application(master=root)
app.mainloop()
