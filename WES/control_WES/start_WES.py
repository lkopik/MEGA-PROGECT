import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7, GPIO.OUT)

GPIO.output(7, GPIO.HIGH)
print("Все системы работает в штатном режиме")
