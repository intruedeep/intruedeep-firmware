from PIL import Image
#
import sys
import os
import time
import numpy as np
from subprocess import call

imageArray = [[0 for x in range(40)] for x in range(40)]

def takeImage():
	command = "fswebcam -r 1280x720 --no-banner --jpeg 100 -D 3 -S 13 image.jpg"
	call(command.split(), shell=False)

def tile():
		height = 18
		width = 32;
		im = Image.open("image.jpg")
		imgwidth, imgheight = im.size
		counter = 0
		for i in range(0, imgheight, height):
				for j in range(0, imgwidth, width):
						box = (j, i, j+width, i+height)
						a = im.crop(box)
						a.save('tiles/tile' + str(counter) + '.jpg')
                                                a.close()
						counter += 1
                im.close()

def findRed(pil_img):
	red_thresh = 140
	green_thresh = 80
	blue_thresh = 80
	pixel_thresh = 50
	pixel_count = 0
	window = np.array(pil_img)
	imgHeight = window.shape[0]
	imgWidth = window.shape[1]
	for i in range(0, imgHeight):
		for j in range(0, imgWidth):
			if ( window[i][j][0] > red_thresh and window[i][j][1] < green_thresh and window[i][j][2] < blue_thresh ):
			    pixel_count += 1

	return pixel_count > pixel_thresh

def createImageArray():
	img_directory = 'tiles/'
	img_Name = 'tile';
	tileCounter = 0;

	for tileCounterX in range(0, 40):
		print tileCounterX;
		for tileCounterY in range(0, 40):
			il_img = Image.open(img_directory + img_Name + str(tileCounter) + ".jpg")
			rv = findRed(il_img);
			if(rv):
				imageArray[tileCounterX][tileCounterY] = 1; 
			else:
				imageArray[tileCounterX][tileCounterY] = 0; 
			tileCounter += 1;

	print "Finished"
	

#The goal of this function is to find the approximate center of a group of 1's
def findCenter():
	leftMost = 2000; #More than the max
	rightMost = -1; #Lower than the least possible value
	topMost = -1;
	bottomMost = 2000;

	#I ignore the outside most boundary, since this doesn't have to return the exact center. Just something close. I do this to avoid out of bounds errors
	for i in range(1, 39):
		for j in range(1, 39):
			#I ensure that each surrounding tile is 1, so that I will reduce the likelyhood of false positives. This may affect if I get the exact center, but that doesn't matter
			if(imageArray[i + 1][j] == 1 and imageArray[i - 1][j] == 1 and imageArray[i][j + 1] == 1 and imageArray[i][j - 1] == 1):
				if(i < leftMost):
					leftMost = i;
				if(i > rightMost):
					rightMost = i;
				if(j < bottomMost):
					bottomMost = j;
				if(j > topMost):
					topMost = j;

	if(leftMost == 2000 or bottomMost == 2000 or topMost == -1 or rightMost == -1):
		print "couldn't find center"
		return -1, -1;
	
	if(((leftMost + rightMost) / 2) % 2 == 1):
		leftMost += 1;

	if(((topMost + bottomMost) / 2) % 2 == 1):
		topMost += 1;

	return (leftMost + rightMost) / 2, (topMost + bottomMost) / 2;

def printImageArray():
	for i in range(0, 40):
		print;
		print imageArray[i]


takeImage();
print "Running tile";
tile();
print "Creating Image Array"
createImageArray();
printImageArray();
print "Finding Center";
x, y = findCenter();
print x
print y;
