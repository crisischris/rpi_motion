#author: Chris Nelson
#This script utilizies a raspberry pi 4 and a PIR motion infrared motion sensonr.
#Once motion is detected, twilio will send an sms to the target number letting the user
#know that motion was detected.  Twilio account required (I have the free account) as well as 
#a target sms (your number).

#python3

import os
import sys
from time import sleep
from gpiozero import LED
from gpiozero import MotionSensor
from twilio.rest import Client

#fetch our pre-defined twilio account sid, twilio auth token, our number 
#and our twilio assigned number as environment variables
SID = os.environ['twilio_cred']
AUTH = os.environ['twilio_auth']
MY_NUMBER = os.environ['my_number']
TWILIO_NUMBER = os.environ['twilio_number']

#define globals
cooldown = 60
red = LED(17)
yellow = LED(27)
green = LED(22)
pir = MotionSensor(6)
message = "Motion was detected in the ______"

#turn all lights off
def allOff ():
    red.off()
    yellow.off()
    green.off()
    
#light dance while booting
def lightDance ():
    red.on()
    sleep(.5)
    red.off()
    yellow.on()
    sleep(.5)
    yellow.off()
    green.on()
    sleep(.5)
    green.off()

#debug line for GUI testing 
print("booting up...")

#LED indicator of bootup
for i in range(0,3):
	lightDance()

#make our client 
client = Client(SID, AUTH)

#to prevent massive sms spam, I'm putting a 'cooldown' in the form of sleep
#after motion was detected
while True:
	pir.wait_for_motion()
	
	#send the twilio message
	client.messages.create(to=MY_NUMBER, from_=TWILIO_NUMBER, body=message)
	
	#debug output for GUI testing
	print("Motion Detected")
	
	green.on()
	pir.wait_for_no_motion()
	
	#debug output for GUI testing
	print("Motion Off")
	sleep(cooldown)
	allOff()
