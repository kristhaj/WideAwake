'''
@author: Sigve Skaugvoll and Martin Bjerke

Thought of mind is that when initializing a instance of GSMHandler, the modem port will be found and used to connect
modem. After this, the modem will be unlocked, the modem will check if there is any network coverage.

This cleans up the sending sms code alot. It encurrages to using the GSMHandler as a object with states, that need to be set, before use
instead of setting and checking for valid state everytime the GSMHandler object is to be used.
'''

import sys, logging
import gsmmodem
import serial
from gsmmodem.modem import GsmModem, SentSms
from gsmmodem.exceptions import TimeoutException, PinRequiredError, IncorrectPinError


class GSMHandler(object):
    '''
    This is a class that sets up the connection to the GSM module, and unlocks the sim.
    This handler will handle the send distress signal.

    '''
    def __init__(self):
        '''
        This tries to find the port, at which the gsm modem is inserted to.
        sets the baud rate, pin, deliveryRaport status and destination number.
        Tries to connect to modem on found port
        Tries to unlock modem with pin, and checks if there is network coverage.
        If something goes wrong, exceptions is printed, and variable/object is set to False.
        :return: None
        '''
        self.port = self.getPort() # find the mort where the modem is connected.
        self.baud = 115200 # modem baud rate
        self.pin = 1235 # sim-pin
        self.deliver = False # if we want to wait for a deliveryReport
        self.destination = "0047"
        self.modem = self.connectToModem() # connect to the modem at the given port.
        self.unlocked = self._unlockModem() # unlocks the modem with the given sim-pin
        self.networkCoverage = self.networkCoverage()
        self.sms = None

    def _getPort(self):
        '''
        if self.port == None:
            raise PinRequiredError("getPort did not find a used port")
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


    def _connectToModem(self):
        '''
        Tries to connect to the modem on the found port.
        handles exception if modem not found or couldn't connect.
        :return: True if connection successfull, else: False
        '''
        try:
            self.modem = GsmModem(self.port,self.baud)
            print("Connecting to GSM modem on " + str(self.port))
            #too see what the modem is doing, uncomment next line:
            #logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
            return True
        except Exception as e:
            print("Something went wrong when trying to connect/find the modem to the modem " + str(e))
            return False

    def _unlockModem(self):
        '''
        This tries to unlock the modem and simcard with the pin code.
        checks for excpetions and handles them.
        Prints what went wrong.
        :return: True if unlock successfull, False else.
        '''
        try:
            self.modem.connect(self.pin)
            return True
        except PinRequiredError as perr:
            print("PinReqiredError: " + str(perr))
            return False
        except IncorrectPinError as ierr:
            print("IncorrectPinError: " + str(ierr))
            return False
        except Exception as e:
            print("Something went wrong when trying to unlock the modem" + str(e))
            return False


    def networkCoverage(self):
        '''
        This takes max five seconds to check if the modem has networkcoverages.
        :return: True if networkCoveragage, else: False
        '''
        try:
            self.networkCoverage = self.modem.waitForNetworkCoverage(5)
            return True
        except TimeoutException as terr:
            print("TimeoutException: " + str(terr))
            return False


    def closeModem(self):
        '''
        Closes the modem. Needs to close the port aswell, bjerke fix
        :return: True if closed properly, else: False
        '''
        try:
            self.modem.close()
            return True
        except Exception as cerr:
            print("Closing the modem: " + str(cerr))
            return False


    def sendThatShit(self, msg):
        '''
        To use this we know that there is created a instance of the GSMHandler.
        When there's created a instance of GSMHandler, the __init__ makes sure/ tries to
        find modem port, connect to the modem, and unlocks the modem.

        :return:
        '''
        #Check if connections and stuff is ready to send SMS.
        if(self.port == False or self.modem == False or self.unlocked == False):
            print("Something is wrong with : ")
            if(self.port == False):
                print("port, ")
            if(self.modem == False):
                print("modem, ")
            if(self.unlocked == False):
                print("unlocked")
            return False

        try:
            if(self._networkCoverage() == False):
                print("Network signal strength is not sufficient.")
                return False

            else:
                try:
                    self.sms = self.modem.sendSms(self.destination, msg, waitForDeliveryReport=self.deliver)
                    if(self.sms.report):
                        if(SentSms.DELIVERED):
                            return True #if the delivered report is True
                        else:
                            return False #if delivered report is False
                    return True
                except TimeoutException as tSMSerr:
                    print("timeoutException when sending sms: " + str(tSMSerr))

        except Exception as exception:
            print("Some unexpected error happen, while trying to send SMS: " + str(exception))