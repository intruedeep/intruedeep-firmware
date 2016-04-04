import RPi.GPIO as GPIO
import smbus
from time import sleep

GPIO.setmode(GPIO.BOARD);
GPIO.setup(13, GPIO.OUT);
GPIO.output(13, True);
sleep(.8);
GPIO.output(13, False);
GPIO.cleanup();
