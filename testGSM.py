from gsmmodem.modem import GsmModem


def main():
    modem = GsmModem()
    modem._unlockSim()

main()