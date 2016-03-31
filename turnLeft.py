import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
Motor1A = 12 
GPIO.setup(Motor1A,GPIO.OUT)


p = GPIO.PWM(12, 3.3333)


p.start(.42);
sleep(.01);
p.stop()


GPIO.cleanup()
