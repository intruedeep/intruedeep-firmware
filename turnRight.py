import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
Motor1A = 12 
GPIO.setup(Motor1A,GPIO.OUT)

while(1):

	p = GPIO.PWM(12, 50)
	p.start(10);
	sleep(1);
	p.stop()

	sleep(2);
 
GPIO.cleanup()
