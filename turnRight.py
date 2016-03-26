import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 7

GPIO.setup(Motor1A,GPIO.OUT)

while(1):

	print "Turning motor on"
	GPIO.output(Motor1A,GPIO.HIGH)
			
	#Clockwise;
	#sleep(.00115)
	sleep(.001)

	print "Stopping motor"
	GPIO.output(Motor1A,GPIO.LOW)
	sleep(2);

 
GPIO.cleanup()


#GPIO.output(Motor1A,GPIO.HIGH)
