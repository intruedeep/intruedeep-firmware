import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 12

GPIO.setup(Motor1A,GPIO.OUT)

 
GPIO.cleanup()


#GPIO.output(Motor1A,GPIO.HIGH)
