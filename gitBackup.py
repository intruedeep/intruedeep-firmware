import RPi.GPIO as GPIO
import smbus
import sys
from time import sleep

bus = smbus.SMBus(1)
address = 0x30
<<<<<<< HEAD
turnTime = .00005;
fireTIme = .5;
Motor1A = 12
FireGPIO = 11
offset = 10;

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1A,GPIO.OUT)

def Fire():
	GPIO.output(FireGPIO, True);
	sleep(.5);
	GPIO.output(FireGPIO, False);


def getBearing1(): 
	while(1):
		try:
			sleep(.1);
			bear = bus.read_byte_data(address, 64)
			return bear
		except:
			print "had a bus error on 64"
		
=======
turnTime = .001;
fireTIme = .5;
Motor1A = 12
FireGPIO = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(FireGPIO,GPIO.OUT)
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
			print "hard a bus error"
>>>>>>> 7e48fb70e68f5c70a9e0f9e711897112b3be6d9b

def getBearing2():
	while(1):
		try:
<<<<<<< HEAD
			sleep(.1);
			bear = bus.read_byte_data(address, 65)
			return bear
		except:
			print "had a bus error on 65"
=======
			bear = bus.read_byte_data(address, 65)
			return bear
		except:
			print "hard a bus error"
>>>>>>> 7e48fb70e68f5c70a9e0f9e711897112b3be6d9b

def turnMotor(rotdir, distance):
	if(rotdir == 'cw'):
<<<<<<< HEAD
		if(distance > 200):
			dutyCycle = .53
		else:
			dutyCycle = .49;
	else:
		if(distance > 200):
			dutyCycle = .39
		else:
			dutyCycle = .42;
=======
		dutyCycle = 10;
	else:
		dutyCycle = 6;
>>>>>>> 7e48fb70e68f5c70a9e0f9e711897112b3be6d9b
		
	p = GPIO.PWM(Motor1A, 3.3333);
	p.start(dutyCycle);
	sleep(turnTime);
	p.stop
	 
<<<<<<< HEAD
def Postition():
	msb = getBearing1();
	lsb = getBearing2();
	return (msb * 255 + lsb)
	
def findDestionationPos(x):
	return x * 11.29;

def goToDestination(destinationPos):
	pos = Postition();
	while(pos < destinationPos):
		turnMotor("cw", destinationPos - pos);
		pos = Postition();
		print "pos = " + str(pos);

def returnHome(startingPos):
	print "Returning Home";
	pos = Postition();
	while(pos > startingPos + offset):
		turnMotor("ccw", pos - startingPos);
		sleep(.5);
		pos = Postition();
		print "pos = " + str(pos);

def main(x):
        startingPos = Postition();
	print "starting = " + str(startingPos);

	targetPos = findDestionationPos(int(x));
	#destinationPos = startingPos + targetPos
	destinationPos = startingPos + 496



	print "Goal destination = " + str(destinationPos);
	goToDestination(destinationPos);
        currentPos = Postition();
	print "Reached destination = " + str(currentPos);

	
	sleep(3);

        endingPos = Postition();
	print "After 3 seconds = " + str(endingPos);

	returnHome(startingPos);
        endingPos = Postition();
	print "Returned Home = " + str(endingPos);
	
	sleep(3);

        endingPos = Postition();
	print "After 3 seconds = " + str(endingPos);
=======
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
	msb = getBearing1();
	lsb = getBearing2();

        startingPos = Postition(msb, lsb);
	targetPos = findDestionationPos(x);
	destinationPos = startingPos + targetPos;

	goToDestination(destinationPos);
	returnHome(startingPos);

	p.stop()
>>>>>>> 7e48fb70e68f5c70a9e0f9e711897112b3be6d9b
	GPIO.cleanup()

if __name__ == "__main__":
	main(sys.argv[1]);

<<<<<<< HEAD


=======
>>>>>>> 7e48fb70e68f5c70a9e0f9e711897112b3be6d9b
