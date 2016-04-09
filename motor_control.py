import RPi.GPIO as GPIO
from time import sleep
import smbus

def fire(slptime=.8):
	GPIO.setmode(GPIO.BOARD);
	GPIO.setup(33, GPIO.OUT);
	GPIO.output(33, True);
	sleep(slptime);
	GPIO.output(33, False);


def turn_left(slptime=.1):
	GPIO.setmode(GPIO.BOARD)
	Motor1A = 12 
	GPIO.setup(Motor1A,GPIO.OUT)


	p = GPIO.PWM(12, 3.3333)

	p.start(.35);
	sleep(slptime);
	p.stop()


	GPIO.cleanup()


def turn_right(slptime=1):
	GPIO.setmode(GPIO.BOARD)
	Motor1A = 12 
	GPIO.setup(Motor1A,GPIO.OUT)


	p = GPIO.PWM(12, 3.3333)


	p.start(.51);
	sleep(slptime);
	p.stop()


	GPIO.cleanup()


def turn_up(slptime=.5):
	GPIO.setmode(GPIO.BOARD)
	Motor1A = 12
	GPIO.setup(Motor1A,GPIO.OUT)


	p = GPIO.PWM(12, 400)


	p.start(48);
	sleep(slptime);
	p.stop()

	GPIO.cleanup()


def turn_down(slptime=.1):  #for what?
	GPIO.setmode(GPIO.BOARD)
	Motor1A = 12
	GPIO.setup(Motor1A,GPIO.OUT)


	p = GPIO.PWM(12, 400)


	p.start(80);
	sleep(slptime);
	p.stop()

	GPIO.cleanup()



turn_up();
