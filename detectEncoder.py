import smbus
import time
bus = smbus.SMBus(1)
address = 0x30

def bearing1():
        bear = bus.read_byte_data(address, 64)
        return bear

def bearing2():
        bear = bus.read_byte_data(address, 65)
        return bear

def bearing3():
        bear = bus.read_byte_data(address, 66)
        return bear

def bearing4():
        bear = bus.read_byte_data(address, 67)
        return bear

while True:
        bear1 = bearing1()  
        bear2 = bearing2()  
        bear3 = bearing3()  
        bear4 = bearing4()  
        print str(bear1) + "  " + str(bear2) + "  " +  str(bear3) + "  " + str(bear4)
        time.sleep(.1)
