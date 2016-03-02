#requires the GPIO library to be setup on the Pi
#GPIO setup guide @ http://www.thirdeyevis.com/pi-page-1.php#gpio-setup

import time
import RPi.GPIO as GPIO #library for controlling the Pis I/O pins

greenLED = 17 #pin number of green LED
redLED = 27 #pin number of red LED
yellowLED = 29 #Pin number of yellow LED

GPIO.setmode(GPIO.BCM)#enables board pin numbering
GPIO.setup(greenLED, GPIO.OUT)#sets which pin is to be used as output
GPIO.setup(redLED, GPIO.OUT)

def 

def greenLEDon():
    GPIO.output(greenLED, True)#Turns on green LED, signaling OK road

def redLEDon():
    GPIO.output(redLED, True)#Turns on red LED, signaling slippery road

def main(startingUp, delay, slipperyStatus): #startingUp is a boolean that changes when the Pi is ready, slipperyStatus is a boolean telling which LED to light after start up
    while startingUp: #amount of blinks
        GPIO.output(greenLED, True)#lights LED
        time.sleep(delay)#pause
        GPIO.output(greenLED, False)#turns LED off
        time.sleep(delay)#pause
    if not slipperyStatus: #checks status of road
        greenLEDon()
    else:
        redLEDon()

    GPIO.cleanup()





