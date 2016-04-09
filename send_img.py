import socket
from subprocess import call


def takeImage():
	command = "fswebcam -r 1280x720 --no-banner --jpeg 100 -D 3 -S 13 image.jpg"
	call(command.split(), shell=False)

def main():	
        takeImage()
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect(('192.168.1.3', 8888))
	fh = open('image.jpg', 'r')
	data = fh.read()
	print(len(data))
	clientsocket.sendall(data)
	clientsocket.close()


main()
