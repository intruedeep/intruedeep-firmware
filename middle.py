import RPi.GPIO as GPIO
import smbus
import sys
import time

GPIO.setmode(GPIO.BOARD)

def moveServo(y):
	servo = 35;
	frequency = 200;

	GPIO.setup(servo, GPIO.OUT);

	pwm = GPIO.PWM(servo, frequency);

	Pos = 1.23 + ((float(y) + 5) * .0075)

	msPerCycle = 1000 / frequency;

	dutyCycle = Pos * 100 / msPerCycle;
	pwm.start(dutyCycle);
	time.sleep(2);
	pwm.stop()

if __name__ == '__main__':
	moveServo(sys.argv[1]);
