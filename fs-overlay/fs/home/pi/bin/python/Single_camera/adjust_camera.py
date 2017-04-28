import RPi.GPIO as GPIO
import argparse
import sys
from time import sleep

PWM_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setwarnings(False)
pwm = GPIO.PWM(PWM_PIN, 500)


#def setup():
#	pwm.start(25)

def main():
	print("\nput in a value between 0 and 10\n")
	duty_cycle = 10
	dataint = map(int, sys.argv[1:])
	duty_cycle = (dataint[0] * 3) + 30
	pwm.start(duty_cycle)
	sleep(.5)

main()
GPIO.cleanup()
