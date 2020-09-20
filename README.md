# rpi_motion
Raspberry pi 4 + Pir IR motion sensor + twilio.  

This script utilizies a raspberry pi 4 and a PIR IR (HC-SR501) motion sensonr.
Once motion is detected, twilio will send an sms to the target number letting the user
know that motion was detected.  Twilio account required (free account works fine) as well as 
a target sms (your twilio verified number).

The python script fetches environment variables, so you will need to export those variables in your .profile etc.
If you don't plan on publishing anything you can simplu hard code in those variables.

The pinout from the RPI to the perpherals are as follows:
PIR sensor-----GPIO 6
red LED--------GPIO 17
yellow LED-----GPIO 27
green LED -----GPIO 22


#Pinout

pinout1 - original image<br/>
  6 ![desc](https://github.com/crisischris/rpi_motion/blob/master/pinout/pinout1.png)<br/>

pinout1 - original image<br/>
  6 ![desc](https://github.com/crisischris/rpi_motion/blob/master/pinout/pinout2.png)<br/>


