#!/usr/bin/env python3
#-- coding: utf-8 --
# Script Original: https://raspberry-pi.fr/led-raspberry-pi/

# python3 led.py "n° pin led" "action"

import RPi.GPIO as GPIO # Importe la bibliothèque pour contrôler les GPIOs

from sys import argv

whichled=int( argv[1] ) # Récupération variable entré 1 "n° pin led"  (nombre)

ledaction = 'switch on/off'
if argv[2:]:                # Vérif si varialbe 2 non vode
   ledaction = argv[2]  # Récupération variable entré 2 "action"
    
GPIO.setmode(GPIO.BCM)  # Définit le mode de numérotation (Board)
GPIO.setwarnings(False) # On désactive les messages d'alerte
LED = whichled          # Définit le numéro du port GPIO qui alimente la led


GPIO.setup(LED, GPIO.OUT) #Active le contrôle du GPIO

state = GPIO.input(LED) #Lit l'état actuel du GPIO, vrai si allumé, faux si éteint

print('LED n°',whichled, ledaction)

if ledaction=="off" or ledaction=="0" :
    GPIO.output(LED, GPIO.LOW)  #On l’éteint
elif ledaction=="on" or ledaction=="1":
    GPIO.output(LED, GPIO.HIGH) #On l'allume
elif state : # Si GPIO allumé
    GPIO.output(LED, GPIO.LOW) #On l’éteint
else :       # Sinon
    GPIO.output(LED, GPIO.HIGH) #On l'allume
