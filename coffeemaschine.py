import RPi.GPIO as GPIO
import time



def brew_coffee(coffetype):
    GPIO.setmode(GPIO.BCM)
     # GPIO Nummern statt Board Nummern
    RELAIS_1_GPIO = 21
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen


    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
    time.sleep(2)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
    print("brewing "+coffetype)
