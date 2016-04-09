import RPi.GPIO as GPIO
import smbus
from time import sleep

GPIO.setmode(GPIO.BOARD);
GPIO.setup(33, GPIO.OUT);
GPIO.output(33, True);
sleep(1.5);
GPIO.output(33, False);
GPIO.cleanup();
