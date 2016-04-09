from PIL import Image
import sys
import os
import time
import numpy as np
from subprocess import call

imageArray = [[0 for x in range(40)] for x in range(40)]

def takeImage():
	command = "fswebcam -r 1280x720 --no-banner --jpeg 100 -D 3 -S 13 image.jpg"
	call(command.split(), shell=False)

	print "Finished"
	

# Returns (tile indexed) (x,y) tuple
def findCenter():
	#TODO Luke

takeImage();
im = Image.open("image.jpg")
