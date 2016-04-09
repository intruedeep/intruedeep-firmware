import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
Motor1A = 37 
GPIO.setup(Motor1A,GPIO.OUT)


p = GPIO.PWM(37, 3.3333)


p.start(.35);
sleep(.1);
p.stop()


GPIO.cleanup()
