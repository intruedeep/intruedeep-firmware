import RPi.GPIO as GPIO
import smbus
from time import sleep

GPIO.setmode(GPIO.BOARD);
GPIO.setup(31, GPIO.OUT);
GPIO.output(31, True);
sleep(1.5);
GPIO.output(31, False);
GPIO.cleanup();
