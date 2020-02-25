#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
new_name=""
try:
  while True:
    print('Place Card to\nregister')
    id, text = reader.read()
##    cursor.execute("SELECT id FROM users WHERE rfid_uid="+str(id))
##    cursor.fetchone()
    
##    if cursor.rowcount >= 1:
##      lcd.clear()
##      lcd.message("Overwrite\nexisting user?")
##      overwrite = input("Overwite (Y/N)? ")
##      if overwrite[0] == 'Y' or overwrite[0] == 'y':
##        lcd.clear()
##        lcd.message("Overwriting user.")
##        time.sleep(1)
##        sql_insert = "UPDATE users SET name = %s WHERE rfid_uid=%s"
##      else:
##        continue;
##    else:
##      sql_insert = "INSERT INTO users (name, rfid_uid) VALUES (%s, %s)"
##    lcd.clear()
    print(str(id))
    print('Enter new name')
    name=input("Name: ")
    if(name==new_name):
        print("name vergeben")
    else:
        new_name = name
        print("User " + new_name + "\nSaved")
##    cursor.execute(sql_insert, (new_name, id))

##    db.commit()

 ##   lcd.clear()

    time.sleep(2)
finally:
  GPIO.cleanup()
