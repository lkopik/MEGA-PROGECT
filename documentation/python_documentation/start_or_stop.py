#версия 2.0 с выполнением bash скрипта. который вычитает значение из файла на сервере main.

#########################################

#ЗАПУСКАТЬ ОТ ИМЕНИ ПОЛЬЗОВАТЕЛЯ

#########################################

import os
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs

os.system("bash /home/"NAME"/control_"NAME"/ssh_change_num.sh")

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

LED = 7 #Définit le numéro du port GPIO qui alimente la led

GPIO.setup(LED, GPIO.OUT) #Active le contrôle du GPIO

state = GPIO.input(LED) #Lit l'état actuel du GPIO, vrai si allumé, faux si éteint

if state : #Si GPIO allumé
    GPIO.output(LED, GPIO.LOW) #On l’éteint
else : #Sinon
    GPIO.output(LED, GPIO.HIGH) #On l'allume

