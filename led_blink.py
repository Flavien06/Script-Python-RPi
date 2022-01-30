#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Script Original:  https://apical.xyz/fiches/scripts_python_pour_interagir_avec_le_gpio/la_base_des_scripts_avec_rpi_gpio

# python3 led_blink.py "n° pin led" "nombre de répétition"

"""
Fait clignoter une LED rouge sur le Raspberry Pi
Paramètres : aucun
Montage : LED rouge branchée sur GPIO.BCM 23 et résistance de 330 Ohms
Auteur Original : Christiane Lagacé
Date : 8 novembre 2021
"""

import RPi.GPIO as GPIO    # il faudra mettre GPIO. devant le nom des classes du paquet
from time import sleep     # les classes du paquets peuvent être utilisées directement sans le nom du paquet

from sys import argv
whichled=int( argv[1] )     # Récupération variable entré 1 "n° pin led"  (nombre)
boucle=int( argv[2] )       # Récupération variable entré 2 "nombre de boucle"


GPIO.setmode(GPIO.BCM)      # type d'adressage broadcom (numéros de ports)
GPIO.setwarnings(False)     # On désactive les messages d'alerte
LED = whichled              # adresse broadcom du branchement de la LED
GPIO.setup(LED, GPIO.OUT)   # sens du signal : le Pi peut envoyer un signal à sa broche

print('Programme qui fait clignoter la LED',whichled, boucle, 'fois')
print('Appuyez sur Ctrl+C pour terminer.')

try:
    while boucle > 0:
        print(boucle)
        boucle -= 1
        GPIO.output(LED, 1)     # envoie 3.3V au port
        sleep(1)
        GPIO.output(LED, 0)     # n'envoie rien au port
        sleep(1)
except KeyboardInterrupt:
    print('Fin du programme, vous avez appuyé sur Ctrl+C.')
except Exception as e:
    print('Une exception est survenue.' + str(e))
finally:
    GPIO.cleanup()     # réinitialise les ports
    print('Nettoyage final réalisé avec succès!')
