import time
from Interface import LEDcontrols

class LEDtester():

    def lightsOn(self):
        LEDcontrols.LEDcontrols.greenOn()
        LEDcontrols.LEDcontrols.yellowOn()
        LEDcontrols.LEDcontrols.redOn()


    def lightsOff(self):
        LEDcontrols.LEDcontrols.greenOff()
        LEDcontrols.LEDcontrols.yellowOff()
        LEDcontrols.LEDcontrols.redOff()

    def testModes(self):
        LEDcontrols.LEDcontrols.warningMode(10)
        LEDcontrols.LEDcontrols.dangerMode(10)
        LEDcontrols.LEDcontrols.safe()

    def main(self):
        LEDtester.lightsOn()
        time.sleep(5)
        LEDtester.lightsOff()
        time.sleep(5)
        LEDcontrols.LEDcontrols.blinkLeds(LEDcontrols.LEDcontrols.leds)
        time.sleep(5)
        LEDtester.testModes()
        
LEDtester.main()