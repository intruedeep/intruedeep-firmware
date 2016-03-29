import RPi.GPIO as GPIO
import smbus
from time import sleep

GPIO.setmode(GPIO.BOARD);
GPIO.setup(11, GPIO.OUT);
GPIO.output(11, True);
sleep(5);
GPIO.output(11, False);
GPIO.cleanup();
