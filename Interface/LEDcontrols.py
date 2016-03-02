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
GPIO.setup(yellowLED, GPIO.OUT)


def safeMode(): #Enter safe mode (constant green LED)
    yellowOff()
    redOff()
    greenOn()

def warningMode(numberOfSeconds): #Enter warning mode (yellow blinking) for the desired number of seconds
    greenOff()
    redOff()
    for i in range(0, numberOfSeconds): #Run loop numberOfSeconds times
        yellowOn()
        time.sleep(0.9)
        yellowOff()
        time.sleep(0.1)


def dangerMode(numberOfSeconds): #Enter danger mode (red blinking) for numberOfSeconds
    yellowOff()
    greenOff()
    for i in range(0, numberOfSeconds):
        redOn()
        time.sleep(0.7)
        redOff()
        time.sleep(0.3)



def greenOn():
    GPIO.output(greenLED, True)#Turns on green LED, signaling OK road

def greenOff():
    GPIO.output(greenLED, False) #Turns off green LED

def redOn():
    GPIO.output(redLED, True)#Turns on red LED, signaling slippery road
def redOff():
    GPIO.output(redLED, False)#Turns off red LED

def yellowOn(): #Turns on yellow LED, signalling that the driver is approaching a slippery road
    GPIO.output(yellowLED, True)
def yellowOff(): #Turns off yellow LED
    GPIO.output(yellowLED, False)

def main(startingUp): #startingUp is a boolean that changes when the Pi is ready

    while startingUp: #amount of blinks
        yellowOn()
        time.sleep(0.4)#pause
        greenOn()
        time.sleep(0.4)
        yellowOff()
        greenOff()
        time(0.4)
    greenOn()

def shutdown(): #Turns off power to our pins and cleans up the ports (sets them to INPUT to protect the circuit)
    yellowOff()
    greenOff()
    redOff()
    GPIO.cleanup()


main()
time.sleep(2)
shutdown()


