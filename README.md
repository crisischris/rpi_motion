# Raspberry pi motion detector with SMS alerts.
Raspberry pi 4 + Pir IR motion sensor + twilio.  

This script utilizes a raspberry pi 4 and a PIR IR (HC-SR501) motion sensor.
Once motion is detected, Twilio will send an SMS message to the target number letting the user
know that motion was detected.  A Twilio account is required (free account works fine) as well as 
a target number (your twilio verified number).

The Python script fetches secret environment variables from the .profile file.
If you don't plan on publishing anything simply hard coding in those variables is fine.


# Pinout<br/>
The pinout from the Pi to the perpherals are as follows:<br/>
PIR sensor-----GPIO 6<br/>
red LED--------GPIO 17<br/>
yellow LED-----GPIO 27<br/>
green LED -----GPIO 22<br/>

pinout<br/>
   ![desc](https://github.com/crisischris/rpi_motion/blob/master/IMGs/pinout1.png)<br/>

pinout<br/>
   ![desc](https://github.com/crisischris/rpi_motion/blob/master/IMGs/pinout2.png)<br/>

message<br/>
<img src="https://github.com/crisischris/rpi_motion/blob/master/IMGs/message.jpeg" width="277" height="600">



