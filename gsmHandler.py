'''
@author: Sigve Skaugvoll and Martin Bjerke
'''

import sys, logging
import gsmmodem
import serial
from gsmmodem.modem import GsmModem, SentSms
from gsmmodem.exceptions import TimeoutException, PinRequiredError, IncorrectPinError


class GSMHandler(object):
    def __init__(self):
        self.port = self.getPort()
        self.baud = 115200
        self.pin = 1235
        self.deliver = False

        if self.port == None:
            raise PinRequiredError("getPort did not find a used port")


    def _getPort(self):
        '''

        :return: port
        '''
        port = None


        """
        Search for ports using a regular expression. Port name, description and
        hardware ID are searched. The function returns an iterable that returns the
        same tuples as comport() would do.

        r = re.compile(regexp, re.I)
        for info in comports():
            port, desc, hwid = info
            if r.search(port) or r.search(desc) or r.search(hwid):
                yield info
        """
        return port


    def sendThatShit(self):
        #send the bloody distress signal
        pass