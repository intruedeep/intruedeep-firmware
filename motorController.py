import RPi.GPIO as GPIO
import smbus
import sys
from time import sleep

bus = smbus.SMBus(1)
address = 0x30
turnTime = .001;
fireTIme = .5;
Motor1A = 12
FireGPIO = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1A,GPIO.OUT)
#GPIO.setup(FireGPIO,GPIO.OUT)
p = GPIO.PWM(Motor1A, 50);
offset = 0

def Fire():
	GPIO.output(FireGPIO, True);
	sleep(.5);
	GPIO.output(FireGPIO, False);


def getBearing1():
	while(1):
		try:
			bear = bus.read_byte_data(address, 64)
			return bear
		except:
			print "had a bus error"

def getBearing2():
	while(1):
		try:
			bear = bus.read_byte_data(address, 65)
			return bear
		except:
			print "hard a bus error"

def turnMotor(rotdir, seconds):
	if(rotdir == 'cw'):
		dutyCycle = 10;
	else:
		dutyCycle = 6;
		
	p.start(dutyCycle);

	print "Trying to turn";
	sleep(seconds);
	p.stop()
	 
def Postition(msb, lsb):
	return (msb * 255 + lsb)
	
def findDestinationPos(x):
	return x * 15;

def goToDestination(destinationPos):
	pos = Postition(msb, lsb);
	while(pos < destinationPos):
		turnMotor("cw", turnTime);
		msb = getBearing1();
		lsb = getBearing2();
		pos = Postition(msb, lsb);

def returnHome(startingPos):
	pos = Postition(msb, lsb);
	while(pos > startingPos + offset):
		turnMotor("ccw", turnTime);
		msb = getBearing1();
		lsb = getBearing2();
		pos = Postition(msb, lsb);

def main(x):
	while(1):
		turnMotor("cw", turnTime);
		sleep(5);
	'''
	msb = getBearing1();
	lsb = getBearing2();

        startingPos = Postition(msb, lsb);
	targetPos = findDestionationPos(x);
	destinationPos = startingPos + targetPos;

	goToDestination(destinationPos);
	returnHome(startingPos);

	p.stop()
	GPIO.cleanup()
	'''
if __name__ == "__main__":
	main(sys.argv[1]);

