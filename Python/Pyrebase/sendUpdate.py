from ArduinoData import ArduinoData
def updateArduino(ard, MACaddr, shutdownFlag, powerData):
    
    try:
                    # int(timer)
        ard.setPowerData(float(powerData))
        print(ard.getPowerDataLatest())
        print(bool(shutdownFlag))
        print("AVG: ",ard.getPowerDataAvg())
        if(ard.getShutdown() != bool(shutdownFlag)):
            ard.setShutdown(bool(shutdownFlag))
    except ValueError:
        print("Could not parse number.")

    else:
        try:
            print("else")# arduinos.append(ArduinoData(MACaddr, bool(shutdownFlag), float(powerData)))
        except ValueError:
            print("Could not parse number.")

def interpretData(arduino, dataSplit):
    isProtocol = False
    if len(dataSplit) == 5:
        if(dataSplit[0] == "ARDUINO"):
            updateArduino(arduino, dataSplit[1], dataSplit[2], dataSplit[3])
            isProtocol = True

    return isProtocol
    