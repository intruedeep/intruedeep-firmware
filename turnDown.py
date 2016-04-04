import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
Motor1A = 12
GPIO.setup(Motor1A,GPIO.OUT)


p = GPIO.PWM(12, 50)


p.start(5);
sleep(.5)
p.stop()

GPIO.cleanup()
