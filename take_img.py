from subprocess import call
command = "fswebcam -r 1280x720 --no-banner --jpeg 100 -D 3 -S 13 image.jpg"
call(command.split(), shell=False)

