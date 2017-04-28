#!/usr/bin/python

import os
import sys
import time
import argparse						#parsing arguments to customize the angle to see
import RPi.GPIO as GPIO
from decimal import Decimal


######################################################################################################
#defining the names for each of the gpiopins that are going to be used
######################################################################################################

clock = 21
#if high data will be read
PIL   = 20	
#specifies the mode that the data is for
PIH   = 26	
#specifies the mode that the data is for

data1 = 19							#MSB
data2 = 13 							#
data3 = 6							#
data4 = 5							#LSB


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#setting all the lines to outputs


GPIO.setup(clock,GPIO.OUT)			#A0
GPIO.setup(PIL,GPIO.OUT)			#A1
GPIO.setup(PIH,GPIO.OUT)			#A2
GPIO.setup(data1,GPIO.OUT)			#D1
GPIO.setup(data2,GPIO.OUT)			#D2
GPIO.setup(data3,GPIO.OUT)			#D3
GPIO.setup(data4,GPIO.OUT)			#D4





######################################################################################################
# function for setting up the data lines(aka gpio pins)
######################################################################################################

def feed_data(feed_datain, mode):
	#first set of data is is going to be the camerabearingin

	#have problems here with feeding in data
	ints =  [int(d) for d in str(bin(feed_datain))[2:]]


	while(len(ints) < 4):
		ints = [0] + ints

	print ints
	

######################################################################################################
## Mode lines: PiLB and PiHB
######################################################################################################
	if(mode == 00):
		GPIO.output(PIH,GPIO.LOW)
		GPIO.output(PIL,GPIO.LOW)
	elif(mode == 01):
		GPIO.output(PIH,GPIO.LOW)
		GPIO.output(PIL,GPIO.HIGH)
	elif(mode == 10):
		GPIO.output(PIH,GPIO.HIGH)
		GPIO.output(PIL,GPIO.LOW)
	elif(mode == 11):
		GPIO.output(PIH,GPIO.HIGH)
		GPIO.output(PIL,GPIO.HIGH)
	else:
		print"why are you here"							#shouldn't ever reach here, all base cases have been covered

######################################################################################################
## DATALINES
######################################################################################################

	if(ints[0] == 1):									# MSB	->0000
		GPIO.output(data1, GPIO.HIGH)		
	else:
		GPIO.output(data1, GPIO.LOW)

	if(ints[1] == 1):
		GPIO.output(data2, GPIO.HIGH)
	else:
		GPIO.output(data2, GPIO.LOW)

	if(ints[2] == 1):
		GPIO.output(data3, GPIO.HIGH)
	else:
		GPIO.output(data3, GPIO.LOW)

	if(ints[3] == 1):									# LSB	  0000<-
		GPIO.output(data4, GPIO.HIGH)
	else:
		GPIO.output(data4, GPIO.LOW)





######################################################################################################
# at this point the data is on all the lines so the clock goes high for processor to read in
######################################################################################################	
	GPIO.output(clock,GPIO.HIGH)

	time.sleep(1)	
        #this is to give the processor plenty of time to read the data in
	if(mode == 01):
		time.sleep(9)
	#this if statement if for when the servos are adjusting position
        #giving them time to settle before they are turned off.
		
######################################################################################################
#toggle the clock low so the processor does not read in data from pins
######################################################################################################	
	GPIO.output(clock,GPIO.LOW)
	
	time.sleep(1)	
	if(mode == 01):
		time.sleep(9)
	
		
	#end of function





















######################################################################################################
## arguments are parsed here EX. python octaplexer.py 5 5 0 0
######################################################################################################

dataint = map(int,sys.argv[1:])			#converts the arguments from strings to integers
										#first argument is the name of the python file being run

databin = map(bin,dataint)				#converts the integers to binary without padded zeros

										#first argument is camerabearing which is a value between 0 and 15
										#second argument is cameratilt which is a value between 0 and 15
										#third argument is a bit that will disable the IMU if not 0
										#fourth argument is a bit that will shutter camera if not 0


#splitting up the list into variables to hold the values										
dataint1 = dataint[0]
databin1 = str('{:004b}'.format(dataint1))		#the syntax format converts the int to a binary that has 4 bits no matter what EX. 0 -> 0000
dataint2 = dataint[1]
databin2 = str('{:004b}'.format(dataint2))
dataint3 = dataint[2]
databin3 = str('{:004b}'.format(dataint3))
dataint4 = dataint[3]
databin4 = str('{:004b}'.format(dataint4))



feed_data(dataint1,00)					#feed the data in for the camera bearing
feed_data(dataint3,10)					#feed the data in for the IMU check should be 0
feed_data(dataint4,11)					#feed the data in for the Shutter check, should be 0 for normal operation
feed_data(dataint2,01)					#feed the data in for the Camera Tilt, this will take 10 seconds.



print("The initiazation process is now done.")
