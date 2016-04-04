#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	pinMode(18,PWM_OUTPUT);
	pwmSetClock(2);
	pwmSetRange(10);
	pwmWrite(18, 50);

}
