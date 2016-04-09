import RPi.GPIO as GPIO
import smbus
import sys
import time

GPIO.setmode(GPIO.BOARD)

servo = 35;
frequency = 50;

GPIO.setup(servo, GPIO.OUT);

pwm = GPIO.PWM(servo, frequency);

leftPos = 1;
rightPos = 2;
middlePos = (rightPos * 1.0 + leftPos) / 2.0;
quartile = (middlePos * 1.0 + leftPos) / 2.0;

positionList = [leftPos, rightPos, middlePos, quartile]

msPerCycle = 1000 / frequency;

for i in range(3):
	for position in positionList:
		dutyCycle = position * 100 / msPerCycle;
		print "Pos = " + str(position);
		print "DC = " + str(dutyCycle);
		print;
		pwm.start(dutyCycle);
		time.sleep(.5);

pwm.stop()
GPIO.cleanup()
