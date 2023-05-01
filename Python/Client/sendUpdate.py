from ArduinoData import ArduinoData
def updateArduino(arduinos, MACaddr, shutdownFlag, timer, powerData):
    if(len(arduinos) > 0):
        for ard in arduinos:
            if ard.getMAC() == MACaddr:
                try:
                    int(timer)
                    ard.setPowerData(float(powerData))
                    print(ard.getPowerData())
                    print(bool(shutdownFlag))
                    if(ard.getShutdown() != bool(shutdownFlag)):
                        ard.setShutdown(bool(shutdownFlag))
                except ValueError:
                    print("Could not parse number.")

    else:
        try:
            arduinos.append(ArduinoData(MACaddr, bool(shutdownFlag), int(timer), float(powerData)))
        except ValueError:
            print("Could not parse number.")

def interpretData(arduinos, dataSplit):
    isProtocol = False
    if len(dataSplit) == 6:
        if(dataSplit[0] == "ARDUINO"):
            updateArduino(arduinos, dataSplit[1], dataSplit[2], dataSplit[3], dataSplit[4])
            isProtocol = True

    return isProtocol