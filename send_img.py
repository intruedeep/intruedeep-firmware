import socket
from subprocess import call
from middle import moveServo
import RPi.GPIO as GPIO
import smbus
import sys
import time

GPIO.setmode(GPIO.BOARD)

def takeImage():
	command = "fswebcam -r 1280x720 --no-banner --jpeg 100 -D 3 -S 13 image.jpg"
	call(command.split(), shell=False)

def main():

	moveLocation = 18;
	servo = 35;
        frequency = 200;

        GPIO.setup(servo, GPIO.OUT);

        pwm = GPIO.PWM(servo, frequency);

        Pos = 1.22 + ((float(moveLocation)) * .0075)

        msPerCycle = 1000 / frequency;

        dutyCycle = Pos * 100 / msPerCycle;
        pwm.start(dutyCycle);



        takeImage()
        time.sleep(2);

	pwm.stop()
        GPIO.cleanup()

        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect(('192.168.1.3', 8888))
	fh = open('image.jpg', 'r')
	data = fh.read()
	print(len(data))
	clientsocket.sendall(data)
	clientsocket.close()


main()




