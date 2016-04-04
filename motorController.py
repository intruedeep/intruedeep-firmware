import RPi.GPIO as GPIO
import smbus
import sys
from time import sleep

bus = smbus.SMBus(1)
address = 0x30
turnTime = .00005;
fireTIme = .5;
Motor1A = 12
FireGPIO = 11
#If the gun is within offset ticks of its desination location, just stop there. 
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
			bear = bus.read_byte_data(address, 64)
			return bear
		except:
			print "had a bus error on 64"
		

def getBearing2():
	while(1):
		try:
			bear = bus.read_byte_data(address, 65)
			return bear
		except:
			print "had a bus error on 65"

def turnMotor(rotdir, distance):
	if(rotdir == 'cw'):
		#The lower duty cycle is more precise, but slow. So switch to the lower cycle when you are within a close distance of the taget
		if(distance > 200):
			dutyCycle = .53
		else:
			dutyCycle = .5;
	else:
		if(distance > 200):
			dutyCycle = .39
		else:
			dutyCycle = .42;
		
	p = GPIO.PWM(Motor1A, 3.3333);
	p.start(dutyCycle);
	sleep(turnTime);
	p.stop
	 
def Postition():
	msb = getBearing1();
	lsb = getBearing2();
	return (msb * 255 + lsb)
	

def findDestinationTicks(index):
	TicksPerDegree = 3449.5 / 360;


	degrees = [1.3631164591600067, 1.40431393310737, 1.4456434205564785, 1.486902441626652, 1.5278648068465346, 1.568281176545824, 1.6078803699140154, 1.646371526719773, 1.6834472021318871, 1.718787440866362, 1.7520648308221207, 1.7829504795736577, 1.8111207921908659, 1.8362648602662743, 1.8580922055217846, 1.8763405639418504, 1.890783355280717, 1.9012364646142086, 1.9075639722393514, 1.9096825077443618, 1.9096825077443618, 1.9075639722393514, 1.9012364646142086, 1.890783355280717, 1.8763405639418504, 1.8580922055217846, 1.8362648602662743, 1.8111207921908659, 1.7829504795736577, 1.7520648308221207, 1.718787440866362, 1.6834472021318871, 1.646371526719773, 1.607880369913562, 1.568281176545824, 1.5278648068465346, 1.4869024416264067, 1.4456434205564785, 1.4043139331076293, 1.3631164591600067]

	totalDegrees = 0;

	for i in range(0, index):
		totalDegrees += degrees[i];

	return(totalDegrees * TicksPerDegree);
	


def goToDestination(destinationPos):
	pos = Postition();
	while(pos + offset < destinationPos):
		turnMotor("cw", destinationPos - pos);
		#The motor might still be moving when you call Position, so if you're close to the destination, sleep for a second so that you have an accurate postion returned
		if(pos - destinationPos < 50):
			sleep(1);
		sleep(.1);
		pos = Postition();
		print "pos = " + str(pos);

def returnHome(startingPos):
	print "Returning Home";
	pos = Postition();
	while(pos > startingPos + offset):
		turnMotor("ccw", pos - startingPos);
		if(pos - startingPos + offset < 50):
			sleep(1);
		sleep(.1);
		pos = Postition();
		#The position wraps around to 65000 when it falls below 0. So in this scenario, we've already past the home position
		if(pos > 64000):
			break;
		print "pos = " + str(pos);

def main(x):
        startingPos = Postition();
	print "starting = " + str(startingPos);

	targetPos = findDestinationTicks(int(x));
	destinationPos = startingPos + targetPos
	#destinationPos = startingPos + 496



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
	GPIO.cleanup()

if __name__ == "__main__":
	main(sys.argv[1]);

