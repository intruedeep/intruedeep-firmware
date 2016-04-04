import math;
#From what I measured this weeked, the board length was 71 inches, and when the board was in the complete view of the camera, the camera was 53.25 inches away from the board.
#We should be able to just replace these variables with whatever we measure for doing up and down
boardLength = 71
boardDistance = 53.25
tileLength = boardLength  * 1.0 / 40;

#tileDegrees will hold 40 indexes with the degrees needed to move the camera from each of those tiles.
tileDegrees = [];
midPoint = 20 * tileLength;

for tileIndex in range(0, 40):
#Used to calculate hypotnuses of right triangles
	lengthOfTiles = midPoint - (tileIndex * tileLength + tileLength / 2);
	if(lengthOfTiles < 0):
		lengthOfTiles *= -1;

	#It's hard to describe in text, but basically for each tile, there's 3 sides. The tile lenght, and the line that connects from the left side of the tile to the camera and the line that connects from the right side of the tile to the camera. These 2 lines are setting up those sides

	sideA = math.sqrt((lengthOfTiles - tileLength) * (lengthOfTiles - tileLength) + boardDistance * boardDistance);
	sideB = math.sqrt(lengthOfTiles * lengthOfTiles + boardDistance * boardDistance);
	
	#Law of SSS for finding angles
	#Cos A = (b^2 + c^2 - a^2) / 2bc
	#In this case, A is the tileLength side and sideA and B are the other sides
	angle = math.degrees(math.acos((sideB * sideB + sideA * sideA - tileLength * tileLength) / (2 * sideB * sideA)));


	tileDegrees.append(angle);


print tileDegrees;


print "Average degrees needed = " + str(sum(tileDegrees) / len(tileDegrees));
