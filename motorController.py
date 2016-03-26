import RPi.GPIO as GPIO
import smbus
from time import sleep

bus = smbus.SMBus(1)
address = 0x30
turnTime = .05;

#Set up motor
GPIO.setmode(GPIO.BOARD)
Motor1A = 12
GPIO.setup(Motor1A,GPIO.OUT)
p = GPIO.PWM(Motor1A, 200);

def getBearing1():
	bear = bus.read_byte_data(address, 64)
	return bear

def getBearing2():
	bear = bus.read_byte_data(address, 65)
	return bear

def turnMotor(rotdir, seconds):
	if(rotdir == 'cw'):
		p.ChangeDutyCycle(40);
		dutyCycle = 40;
	else:
		p.ChangeDutyCycle(24);
		dutyCycle = 24;
		
	p.start(dutyCycle);

	sleep(seconds);
	 

def Postition(msb, lsb):
	return (msb * 255 + lsb)
	

def main():
	msb = getBearing1();
	lsb = getBearing2();

	targetPos = 2156
	startingPos = Postition(msb, lsb);
	destinationPos = startingPos + targetPos;
	pos = startingPos;

	while(pos < destinationPos):
		msb = getBearing1();
		lsb = getBearing2();
		pos = Postition(msb, lsb);
		turnMotor("cw", turnTime);
		print msb;

	print "here";

	while(pos > startingPos):
		msb = getBearing1();
		lsb = getBearing2();
		pos = Postition(msb, lsb);
		turnMotor("ccw", turnTime);
		print msb;

	GPIO.cleanup()

main();
