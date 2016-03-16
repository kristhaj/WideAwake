#requires the GPIO library to be setup on the Pi
#GPIO setup guide @ http://www.thirdeyevis.com/pi-page-1.php#gpio-setup

import time
import RPi.GPIO as GPIO #library for controlling the Pis I/O pins

class LEDcontrols:

    greenLED = 17 #pin number of green LED
    redLED = 22 #pin number of red LED
    yellowLED = 27 #Pin number of yellow LED
    internetConnection = True
    leds = [greenLED, yellowLED, redLED]


    def __init__(self,connection):
        self.internetConnection = connection;
        self.setUpLeds([17, 22, 27])

    def safe(self):
        if (self.internetConnection):
            self.greenOn()
            self.yellowOff()
            self.redOff()

        else:
            self.yellowOn()
            self.greenOff()
            self.redOff()


    def setUpLeds(self,leds):
        GPIO.setmode(GPIO.BCM)#enables board pin numbering
        for led in leds:
            GPIO.setup(led, GPIO.OUT)

    def blinkLeds(self,leds): #Can be run if you want to see if all the LEDS are working

        for led in leds:
            GPIO.output(led, True)
            time.sleep(1)
            GPIO.output(led, False)



    def warningMode(self, numberOfSeconds): #Enter warning mode (yellow blinking) for the desired number of seconds
        self.greenOff()
        self.yellowOff()
        self.redOn()
        time.sleep(numberOfSeconds)



    def dangerMode(self, numberOfSeconds): #Enter danger mode (red blinking) for numberOfSeconds
        self.yellowOff()
        self.greenOff()
        for i in range(0, numberOfSeconds):
            self.redOn()
            time.sleep(0.5)
            self.redOff()
            time.sleep(0.5)



    def greenOn(self):
        GPIO.output(self.greenLED, True)#Turns on green LED, signaling OK road

    def greenOff(self):
        GPIO.output(self.greenLED, False) #Turns off green LED

    def redOn(self):
        GPIO.output(self.redLED, True)#Turns on red LED, signaling slippery road
    def redOff(self):
        GPIO.output(self.redLED, False)#Turns off red LED

    def yellowOn(self): #Turns on yellow LED, signalling that the driver is approaching a slippery road
        GPIO.output(self.yellowLED, True)
    def yellowOff(self): #Turns off yellow LED
        GPIO.output(self.yellowLED, False)

    def boot(self):
        self.blinkLeds(self.redLED, self.yellowLED, self.greenLED)


    def shutdown(self): #Turns off power to our pins and cleans up the ports (sets them to INPUT to protect the circuit)
        print ("Shutting down..")
        GPIO.cleanup()



