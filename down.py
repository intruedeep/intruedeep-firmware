import RPi.GPIO as GPIO
import smbus
from time import sleep

GPIO.setmode(GPIO.BOARD);
GPIO.setup(12, GPIO.OUT);
p = GPIO.PWM(12, 50);
p.start(7.5);

try:
	while(1):
		p.ChangeDutyCycle(7.5);
		sleep(1);
		p.ChangeDutyCycle(5);
		sleep(1);
		p.ChangeDutyCycle(10);
		sleep(1);


except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup();
