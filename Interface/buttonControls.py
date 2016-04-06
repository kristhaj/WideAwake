import RPi.GPIO as GPIO #library for controlling the Pis I/O pins
import time
from Interface import LEDcontrols

class buttonControls:

    ledcontrols = LEDcontrols.LEDcontrols

    offlineButton = 18
    onlineState = True

    distressButton = 14
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

    def getMode(self):
        self.getButtonState()
        return self.onlineState


    def distressSignal(self):
        self.getButtonState()
        return self.distressState