#requires the GPIO library to be setup on the Pi
#GPIO setup guide @ http://www.thirdeyevis.com/pi-page-1.php#gpio-setup

import time
import RPi.GPIO as GPIO #library for controlling the Pis I/O pins

class LEDcontrols:

    greenLED = 17 #pin number of green LED
    redLED = 22 #pin number of red LED
    yellowLED = 27 #Pin number of yellow LED
    leds = [greenLED, yellowLED, redLED]


    def __init__(self):
        self.setUpLeds([17, 22, 27])

    def safe(self, connection): #Set interface to a safe-mode. Connection is a boolean indicating whether the system is in an offline or online state

        self.dangerMode(False)
        if (connection): #I.E. online -> green light on 
            self.greenOn()
            self.yellowOff()
            self.redOff()

        else: #I.E. offline -> yellow light on
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



    def warningMode(self): #Enter warning mode (redLED on) for the desired number of seconds
        self.dangerMode(False)
        self.greenOff()
        self.yellowOff()
        self.redOn()



    def dangerMode(self, bool): #Enter danger mode (red blinking) for numberOfSeconds
        self.yellowOff()
        self.greenOff()
        while True:
            if (bool):
                self.redOn()
                time.sleep(0.5)
                self.redOff()
                time.sleep(0.5)
            else:
                break



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
        self.blinkLeds(self.leds)


    def shutdown(self): #Turns off power to our pins and cleans up the ports (sets them to INPUT to protect the circuit)
        print ("Shutting down..")
        GPIO.cleanup()



