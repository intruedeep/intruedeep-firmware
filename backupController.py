import RPi.GPIO as GPIO
import smbus
from time import sleep

bus = smbus.SMBus(1)
address = 0x30
turnTime = .1;

#Set up motor
GPIO.setmode(GPIO.BOARD)
Motor1A = 12
GPIO.setup(Motor1A,GPIO.OUT)
p = GPIO.PWM(Motor1A, 50);
offset = 0

def getBearing1():
	while(1):
		try:
			bear = bus.read_byte_data(address, 64)
			return bear
		except:
			print "Error with bus";

def getBearing2():
	while(1):
		try:
			bear = bus.read_byte_data(address, 65)
			return bear
		except:
			print "Error with bus";

def turnMotor(rotdir, seconds):
	if(rotdir == 'cw'):
		dutyCycle = 10;
	else:
		dutyCycle = 6;
		
	p.start(dutyCycle);

	sleep(seconds);
	 

def Postition(msb, lsb):
	return (msb * 255 + lsb)
	

def main():
	msb = getBearing1();
	lsb = getBearing2();
	print lsb;
	print msb;

	#targetPos = 2156
	targetPos = 3449
	
        startingPos = Postition(msb, lsb);
	destinationPos = startingPos + targetPos;
	pos = startingPos;

	print startingPos;
	while(pos < destinationPos):
		msb = getBearing1();
		lsb = getBearing2();
		pos = Postition(msb, lsb);
		turnMotor("cw", turnTime);

	print "here";

	while(pos >= startingPos + offset):
		msb = getBearing1();
		lsb = getBearing2();
		pos = Postition(msb, lsb);
		turnMotor("ccw", turnTime);

	GPIO.cleanup()
	msb = getBearing1();
	lsb = getBearing2();
	pos = Postition(msb, lsb);
	print lsb;
	print msb;
	print pos;

main();
