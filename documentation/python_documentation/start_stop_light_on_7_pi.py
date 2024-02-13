#########################################

#ЗАПУСКАТЬ ОТ ИМЕНИ ПОЛЬЗОВАТЕЛЯ

#########################################
import os
import RPi.GPIO as GPIO # Импортируйте библиотеку для управления GPIO.


GPIO.setmode(GPIO.BOARD) # Устанавливает режим набора номера (Доска)
GPIO.setwarnings(False) # Мы деактивируем оповещения

LED = 7 # Определяет номер порта GPIO, от которого питается светодиод.

GPIO.setup(LED, GPIO.OUT) # Включает управление GPIO

state = GPIO.input(LED) #Считывает текущий статус GPIO: true, если включено, false, если выключено.

if state : # Если GPIO включен
    GPIO.output(LED, GPIO.LOW) # Мы выключим его
else : #Sinon
    GPIO.output(LED, GPIO.HIGH) # Мы зажигаем его
