#этот код запукает ток по 7 пину. только запускает.

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7, GPIO.OUT)

GPIO.output(7, GPIO.HIGH)
