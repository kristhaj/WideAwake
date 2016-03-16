import time
import LEDcontrols

class LEDtester():

    controls = LEDcontrols.LEDcontrols(False)
    leds = controls.leds

    def lightsOn(self):
        LEDtester.controls.greenOn()
        LEDtester.controls.yellowOn()
        LEDtester.controls.redOn()


    def lightsOff(self):
        LEDtester.controls.greenOff()
        LEDtester.controls.yellowOff()
        LEDtester.controls.redOff()

    def testModes(self):
        LEDtester.controls.warningMode(4)
        LEDtester.controls.dangerMode(4)
        LEDtester.controls.safe()

    def main(self):
        LEDtester.lightsOn(self)
        time.sleep(5)
        LEDtester.lightsOff(self)
        time.sleep(5)
        LEDtester.controls.blinkLeds(LEDtester.leds)
        time.sleep(5)
        LEDtester.testModes(self)
        time.sleep(5)
        LEDtester.controls.shutdown()
        
x = LEDtester()
x.main()
