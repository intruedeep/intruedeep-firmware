import RPi.GPIO as GPIO
import smbus
from time import sleep

bus = smbus.SMBus(1)
address = 0x30
turnTime = .01;

#Set up motor
GPIO.setmode(GPIO.BOARD)
Motor1A = 12
GPIO.setup(Motor1A,GPIO.OUT)
p = GPIO.PWM(Motor1A, 50);
offset = 188

def getBearing1():
	bear = bus.read_byte_data(address, 64)
	return bear

def getBearing2():
	bear = bus.read_byte_data(address, 65)
	return bear

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
	print lsb;
	print msb;
	print pos;

	print startingPos;
	while(pos < destinationPos):
		msb = getBearing1();
		lsb = getBearing2();
		pos = Postition(msb, lsb);
		turnMotor("cw", turnTime);

	print "here";

#	while(pos > 0 and msb <= 240):
	while(pos > 180 and pos <= 65000):
		print pos;
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
