#этот код проверяет включен ли тэц. если да, то пишется ТЦЭ не отвечает. если же нет. то выключает.
#после чего выполняет bash скрипт по вычитанию hp.
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7, GPIO.OUT)

if GPIO.input(7):
    print("Выключение ТЭЦ через 5 минут. пожалуйста не прекращайте процесс.")
    time.sleep(10)
    print("Выключение.")
    time.sleep(5)
    GPIO.output(7, GPIO.LOW)
    os.system("bash /home/chp/control_CHP/.ssh_change_num.sh")
    print("ТЭЦ была успешно выключенна.")
else:
    print("ТЭЦ не отвечает")
