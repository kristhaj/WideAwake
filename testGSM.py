from gsmmodem.modem import GsmModem


def main():
    modem = GsmModem("/dev/ttyAMA0")
    modem.connect(None)

main()