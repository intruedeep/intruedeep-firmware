import socket
from motorController import main
from portalsfx import activeS

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('192.168.1.2', 9999))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
        connection, address = serversocket.accept()
        buf = connection.recv(4096)
        if len(buf) > 0:
		activeS.active_s('portalsfx/wavs/Turret_turret_active_2.wav')
		xy = buf.split(',')
		x = int(xy[0])
		y = int(xy[1])
                print("recieved x,y: (%d, %d)"%(x, y))
		main(x, y)
		
