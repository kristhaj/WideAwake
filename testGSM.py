from gsmmodem.modem import GsmModem


def main():
    modem = GsmModem("/dev/ttyAMA0")
    modem._unlockSim(None)

main()