import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
Motor1A = 12
GPIO.setup(Motor1A,GPIO.OUT)


p = GPIO.PWM(12, 400)


p.start(48);
sleep(.25);
p.stop()

GPIO.cleanup()
