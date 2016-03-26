import smbus
import time
bus = smbus.SMBus(1)
address = 0x30
regCounter = 0;

print(bus.read_byte_data(address, 0))
while(1):
	try:
		print(bus.read_byte_data(address, regCounter))
		print "Reg = " + hex(regCounter);
		time.sleep(1)
	except:
		print "Problem on addres " + hex(myAddress);
		time.sleep(1)
	
	regCounter += 1;
		
