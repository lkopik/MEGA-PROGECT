import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
if GPIO.input(7):
    print("Выключение Аэропорта через 2 минуты. пожалуйста не прекращайте процесс.")
    time.sleep(300)
    print("Выключение.")
    time.sleep(5)
    GPIO.output(7, GPIO.LOW)
    os.system("bash /home/air/control_AIR/.ssh_change_num.sh")
    print("Аэропорт была успешно выключен.")
else:
    print("Аэропорт не отвечает")
