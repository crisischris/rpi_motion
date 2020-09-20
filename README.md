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
  6 ![desc](https://images.squarespace-cdn.com/content/v1/5cc0708db10f257f085020f4/1567281818366-YCG8DOC0JET2YLL1BDD6/ke17ZwdGBToddI8pDm48kL5vtkVmuF_T    fVXAjoajrn8UqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKcGQLJLq7bbn0dtpDTIRzKAA4rdzrVEJ6L0zdRX09DaLA9JivhSP    EF_ntuZ80V9KbO/change2.png?format=500w)<br/>
