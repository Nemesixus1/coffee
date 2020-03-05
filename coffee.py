import tkinter as tk
from tkinter import*
import tkinter.messagebox
from tkinter.ttk import *
import time
from subprocess import call
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import query
import coffeemaschine
import mysql.connector


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master =master
        self.pack(side="bottom",fill="both")
        self.create_widgets()
        
        

    def create_widgets(self):
        self.quit =tk.Button(self,text="Quit",fg="red", command=self.master.destroy)
        self.quit.pack(side="top")
        self.buttonstatus =tk.Button(self)
        self.buttonstatus["text"]= "Wasser vorheizen"
        self.buttonstatus["command"]= self.status
        self.buttonstatus.pack()
        self.progress=Progressbar(self,orient=HORIZONTAL,length=100,mode="determinate")
        self.progress.pack(pady="8",fill='x')
        self.ausgabe =tk.Label(self,textvariable=v,font=("Courier",20))
        self.ausgabe.pack(fill="x")
        v.set("Bitte wählen Sie ein Getränk.")
        
        self.buttonkaffeeklein =tk.Button(self)
        self.buttonkaffeeklein["text"]= "Kleiner Kaffee"
        self.buttonkaffeeklein["height"]= 25
        self.buttonkaffeeklein["width"]= 20
        self.buttonkaffeeklein["command"] = self.kaffeeklein
        self.buttonkaffeeklein["state"]= "disabled"

        self.buttonkaffeekleinstark =tk.Button(self)
        self.buttonkaffeekleinstark["text"]= "Kleiner Kaffee STARK"
        self.buttonkaffeekleinstark["height"]= 25
        self.buttonkaffeekleinstark["width"]= 20
        self.buttonkaffeekleinstark["command"] = self.kaffeekleinstark
        self.buttonkaffeekleinstark["state"]= "disabled"
        
        self.buttonkaffeegross =tk.Button(self)
        self.buttonkaffeegross["text"]= "Großer Kaffee"
        self.buttonkaffeegross["height"]= 25
        self.buttonkaffeegross["width"]= 20
        self.buttonkaffeegross["command"] = self.kaffeegross
        self.buttonkaffeegross["state"]= "disabled"
        
        self.buttonkaffeegrossstark =tk.Button(self)
        self.buttonkaffeegrossstark["text"]= "Großer Kaffee STARK"
        self.buttonkaffeegrossstark["height"]= 25
        self.buttonkaffeegrossstark["width"]= 20
        self.buttonkaffeegrossstark["command"] = self.kaffeegrossstark
        self.buttonkaffeegrossstark["state"]= "disabled"

        self.buttonkaffeeklein.pack(side="left",fill="y")
        self.buttonkaffeekleinstark.pack(side="left",fill="y")  
        self.buttonkaffeegross.pack(side="right",fill="y")
        self.buttonkaffeegrossstark.pack(side="right",fill="y")


    def rfid(self, chipid,preis):
        if chipid==129353831365:
                print("Hallo Georg")
                self.ausgabe["text"]="Name Georg"
        print(chipid)
        print(preis)

    def label(self, text):
        v.set(text)
        root.update_idletasks()

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
        
        self.label("Chipkarte anlegen")
        
        kartenid= str(self.warteaufkarte())
        if not kartenid:
            return
            
        self.label("Bitte warten...")
        connection=query.connect()
        auth = query.authenticate(connection, kartenid)

        if not auth:
            query.disconnect(connection)
            self.label("Chipkarte nicht in Datenbank")
            return False
        
        id, fname, lname, cnumber, pref, debt = query.get_person_entries(connection, kartenid)
        self.label("Eine Sekunde noch "+ fname +" ;)")

        


        allowed = query.is_allowed(debt,preis)
        if not allowed:
            self.label("Bitte bezahlen Sie ihre Schulden.")
            return False
        else:
            query.get_coffee(cnumber, kaffee)
            query.update_debt(connection, cnumber, debt, preis)
            self.label("Ihre Schulden betragen: "+ str(round(debt+preis,1)) +"€.")
            self.fortschritt()
            self.label("Bitte wählen Sie ein Getränk.")

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
        coffeemaschine.starte_coffee()
 
        #Button aktivieren
        self.buttonkaffeegross["state"]= "normal"
        self.buttonkaffeeklein["state"]= "normal"
        


root = tk.Tk()
reader = SimpleMFRC522()
v=StringVar() 
root.title("Kaffeemaschine")
root.attributes('-fullscreen', True)
#root.config(cursor="none")

app=Application(master=root)
app.mainloop()
