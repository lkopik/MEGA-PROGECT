import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
if GPIO.input(7):
    print("Выключение через несколько минут. пожалуйста не прекращайте процесс.")
    time.sleep(60)
    print("Выключение.")
    time.sleep(5)
    GPIO.output(7, GPIO.LOW)
    os.system("bash /home/chp/control_CHP/.ssh_change_num.sh")
    print("успешно выключено.")
else:
    print("Не отвечает")
