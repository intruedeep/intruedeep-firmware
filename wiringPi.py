import wiringpi2
wiringpi.piBoardRev()

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, 0)
wiringpi.pullUpDnControl(18, 1)
