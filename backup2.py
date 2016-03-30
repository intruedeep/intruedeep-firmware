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
offset = 180

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
	sleep(seconds);
	 
def Postition():
	msb = getBearing1();
	lsb = getBearing2();
	return (msb * 255 + lsb)
	
def findDestionationPos(x):
	return x * 15;

def goToDestination(destinationPos):
	pos = Postition();
	while(pos < destinationPos):
		turnMotor("cw", turnTime);
		pos = Postition();

def returnHome(startingPos):
	pos = Postition();
	while(pos > startingPos + offset):
		turnMotor("ccw", turnTime);
		pos = Postition();
	turnMotor("cw", turnTime);
	p.stop()

def main(x):
        startingPos = Postition();
	print startingPos;

	targetPos = findDestionationPos(int(x));
	destinationPos = startingPos + targetPos;


	goToDestination(destinationPos);
        currentPos = Postition();
	print currentPos;

	sleep(3);

        endingPos = Postition();
	print endingPos;

	returnHome(startingPos);
	
        endingPos = Postition();
	print endingPos;

	sleep(3);

        endingPos = Postition();
	print endingPos;

	sleep(3);

        endingPos = Postition();
	print endingPos;
	GPIO.cleanup()

if __name__ == "__main__":
	main(sys.argv[1]);

