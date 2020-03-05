import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def brew_coffee(coffeetype):
    GPIO.setmode(GPIO.BCM)
    if coffeetype=="klein":
         # GPIO Nummern statt Board Nummern
        RELAIS_klein = 21
        GPIO.setup(RELAIS_klein, GPIO.OUT) # GPIO Modus zuweisen


        GPIO.output(RELAIS_klein, GPIO.LOW) # an
        time.sleep(2)
        GPIO.output(RELAIS_klein, GPIO.HIGH) # aus

    if coffeetype=="groß":
         # GPIO Nummern statt Board Nummern
        RELAIS_groß = 20
        GPIO.setup(RELAIS_groß, GPIO.OUT) # GPIO Modus zuweisen


        GPIO.output(RELAIS_groß, GPIO.LOW) # an
        time.sleep(2)
        GPIO.output(RELAIS_groß, GPIO.HIGH) # aus

def starte_coffee():

         # GPIO Nummern statt Board Nummern
        RELAIS_an = 16
        GPIO.setup(RELAIS_an, GPIO.OUT) # GPIO Modus zuweisen


        GPIO.output(RELAIS_an, GPIO.LOW) # an
        time.sleep(2)
        GPIO.output(RELAIS_an, GPIO.HIGH) # aus


