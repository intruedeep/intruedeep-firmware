import RPi.GPIO as GPIO
import smbus
import sys
import time

GPIO.setmode(GPIO.BOARD)

servo = 35;
frequency = 200;

GPIO.setup(servo, GPIO.OUT);

pwm = GPIO.PWM(servo, frequency);

Pos = 1.65;

msPerCycle = 1000 / frequency;

dutyCycle = Pos * 100 / msPerCycle;
pwm.start(dutyCycle);
time.sleep(2);


pwm.stop()
GPIO.cleanup()
