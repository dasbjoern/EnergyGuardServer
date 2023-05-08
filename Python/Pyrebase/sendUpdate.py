from ArduinoData import ArduinoData
def updateArduino(arduinos, MACaddr, shutdownFlag, powerData):
    if(len(arduinos) > 0):
        for ard in arduinos:
            if ard.getMAC() == MACaddr:
                try:
                    # int(timer)
                    ard.setPowerData(float(powerData))
                    print(ard.getPowerData())
                    print(bool(shutdownFlag))
                    print("AVG: ",ard.getPowerDataAvg())
                    if(ard.getShutdown() != bool(shutdownFlag)):
                        ard.setShutdown(bool(shutdownFlag))
                except ValueError:
                    print("Could not parse number.")

    else:
        try:
            arduinos.append(ArduinoData(MACaddr, bool(shutdownFlag), float(powerData)))
        except ValueError:
            print("Could not parse number.")

def interpretData(arduinos, dataSplit):
    isProtocol = False
    if len(dataSplit) == 5:
        if(dataSplit[0] == "ARDUINO"):
            updateArduino(arduinos, dataSplit[1], dataSplit[2], dataSplit[3])
            isProtocol = True

    return isProtocol
    