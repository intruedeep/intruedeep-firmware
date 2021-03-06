import RPi.GPIO as GPIO
import smbus
import sys
import motor_control
import random;

from time import sleep

bus = smbus.SMBus(1)
address = 0x30
turnTime = .00005;
fireTIme = .5;
Motor1A = 37
FireGPIO = 11
#If the gun is within offset ticks of its desination location, just stop there. 
offset = 5;
homeOffset = 5;
downPos = 1.22
middlePos = downPos + .15
gravityOffset = 0;
homePos = 16;
yOffset = 0;

servo = 35;
frequency = 200;
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(servo, GPIO.OUT);
pwm = GPIO.PWM(servo, frequency);


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

def turnMotor(rotdir, distance, pos, prevPos):
	if(rotdir == 'cw'):
		#The lower duty cycle is more precise, but slow. So switch to the lower cycle when you are within a close distance of the taget
		if(distance > 200):
			dutyCycle = .55
		elif(pos == prevPos):
			seed = random.randint(0, 2);
			if(seed % 2 == 0):
				dutyCycle = .57;
			else:
				dutyCycle = .59;
		else:
			dutyCycle = .51;
	else:
		if(distance > 200):
			dutyCycle = .39
		elif(pos == prevPos):
			dutyCycle = .37;
			seed = random.randint(0, 2);
			if(seed % 2 == 0):
				dutyCycle = .37;
			else:
				dutyCycle = .35;



		else:
			dutyCycle = .43
		
	p = GPIO.PWM(Motor1A, 3.3333);
	p.start(dutyCycle);
	sleep(turnTime);
	p.stop
	 
def Postition():
	msb = getBearing1();
	lsb = getBearing2();
	if(msb * 255 + lsb > 64000):
		return msb * 255 + lsb - 65280

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
	prevPos = 0;
	while(1):
		if(destinationPos > pos + offset):
			turnMotor("cw", destinationPos - pos, pos, prevPos);
			#sleep to ensure proper encoder reading
			if(pos - destinationPos < 50):
				sleep(.5);
			prevPos = pos;
			pos = Postition();
			print "pos = " + str(pos);

		elif(destinationPos + offset < pos):
			turnMotor("cww", pos -  destinationPos, pos, prevPos);
			if(destinationPos - pos < 50):
				sleep(.5);
			prevPos = pos;
			pos = Postition();
			print "pos = " + str(pos);

		else:
			break;


def moveServo(y):

	angles = [1.3631164591600067, 1.40431393310737, 1.4456434205564785, 1.486902441626652, 1.5278648068465346, 1.568281176545824, 1.6078803699140154, 1.646371526719773, 1.6834472021318871, 1.718787440866362, 1.7520648308221207, 1.7829504795736577, 1.8111207921908659, 1.8362648602662743, 1.8580922055217846, 1.8763405639418504, 1.890783355280717, 1.9012364646142086, 1.9075639722393514, 1.9096825077443618, 1.9096825077443618, 1.9075639722393514, 1.9012364646142086, 1.890783355280717, 1.8763405639418504, 1.8580922055217846, 1.8362648602662743, 1.8111207921908659, 1.7829504795736577, 1.7520648308221207, 1.718787440866362, 1.6834472021318871, 1.646371526719773, 1.607880369913562, 1.568281176545824, 1.5278648068465346, 1.4869024416264067, 1.4456434205564785, 1.4043139331076293, 1.3631164591600067]

	print(y)
	angle = sum(angles[0:int(y)+1]); 

	print "Angle = " + str(angle);

	Pos = angle * (.3 / 68) + downPos;
	
	print "Pos = " + str(Pos);
	
#        Pos = downPos + ((float(y) + gravityOffset) * .0075)

	

        msPerCycle = 1000 / frequency;

        dutyCycle = Pos * 100 / msPerCycle;
        pwm.start(dutyCycle);
        sleep(2);
#        pwm.stop()




def main(x, y):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(servo, GPIO.OUT);
	pwm = GPIO.PWM(servo, frequency);
        startingPos = Postition();
	print "starting = " + str(startingPos);

		
	targetPos = findDestinationTicks(int(x));
	destinationPos = startingPos + targetPos



	print "Goal destination = " + str(destinationPos);
	goToDestination(destinationPos);
        currentPos = Postition();
	print "Reached destination = " + str(currentPos);

	moveServo(int(y) + yOffset);
	
	motor_control.fire()
	sleep(1);

	offset = homeOffset;

        endingPos = Postition();

	print "Actually fired at " + str(endingPos);
	#Return home
	goToDestination(startingPos);
        endingPos = Postition();
	print "Returned Home = " + str(endingPos);

        endingPos = Postition();
	#Go to a neutral position;
	moveServo(homePos);
	
	GPIO.cleanup()
	return 0;

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2]);

