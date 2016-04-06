import RPi.GPIO as GPIO #library for controlling the Pis I/O pins
import time
from Interface import LEDcontrols

class buttonControls:

    ledcontrols = LEDcontrols.LEDcontrols

    offlineButton = 0
    onlineState = True

    distressButton = 1
    distressState = True

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def getButtonState(self):
        if GPIO.input(self.offlineButton):
            self.onlineState = False
        if GPIO.input(self.distressButton):
            self.distressState = False

    def setMode(self):
        if self.onlineState:
            self.ledcontrols.safe(True)
        else:
            self.ledcontrols.safe(False)


    def distressSignal(self):
        return self.distressState