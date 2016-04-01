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

    def _getPort(self):
        '''

        :return: port
        '''
        return None


    def sendThatShit(self):
        #send the bloody distress signal
        pass