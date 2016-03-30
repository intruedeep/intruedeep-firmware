import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
Motor1A = 12 
GPIO.setup(Motor1A,GPIO.OUT)


p = GPIO.PWM(12, 5)


p.start(1);
sleep(.01);
p.stop()


GPIO.cleanup()
