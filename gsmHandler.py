'''
@author: Sigve Skaugvoll and Martin Bjerke

Thought of mind is that when initializing a instance of GSMHandler, the modem port will be found and used to connect
modem. After this, the modem will be unlocked, the modem will check if there is any network coverage.

This cleans up the sending sms code alot. It encurrages to using the GSMHandler as a object with states, that need to be set, before use
instead of setting and checking for valid state everytime the GSMHandler object is to be used.

pip install python-gsmmodem
pip install pyserial
'''


from UnusableSystemException import UnusableSystemException
import serial
import time

class GSMHandler(object):
    '''
    This is a class that sets up the connection to the GSM module. #sim cannot have pin activated.
    This handler will handle the send distress signal.

    '''
    def __init__(self):

        try:
            self.modem = serial.Serial(port='/dev/ttyAMA0', baudrate=115200, timeout=3.0) #connet to the modme
            self.open = self.modem.isOpen() #get the state of the modem
            self.modem.write(b'AT\r\n') #set synchronization between modem and serial
            print(self.modem.read(10))  # read if synchronization is good
            self.modem.write(b'AT+CMGF=1\r\n')  #make modem ready for sms-action
            print(self.modem.read(20))
            self._setSMSValidation()
        except Exception as e:
            #print(str(e))
            raise e



    def _setSMSValidation(self):
        self.modem.write(b'AT+CSMP=17,0,0,16\r\n')
        print(self.modem.read(20))



    def closeModem(self):
        try:
            self.modem.close()
            return True
        except Exception as cerr:
            print("Closing the modem: " + str(cerr))
            return False


    def sendThatShit(self, msg):

        try:
            self.modem.write(b'AT+CMGS="+4790909909"\r\n')
            time.sleep(5)
            print(self.modem.read(2))
            self.modem.write(bytes(msg,'utf-8') + bytes('\x1A\r\n','utf-8'))
            time.sleep(10)
            print(self.modem.read(60))
        except Exception as e:
            raise UnusableSystemException(str(e))

