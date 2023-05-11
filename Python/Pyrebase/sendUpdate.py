from ArduinoData import ArduinoData
def updateArduino(arduinos, index, MACaddr, shutdownFlag, powerData):
    
    try:
        # if(arduinos[index].getMAC() == MACaddr):      
        arduinos[index].setPowerData(float(powerData))
        print("Power Data recieved: ", arduinos[index].getPowerDataLatest()[0])  
            # print("AVG: ",arduinos[index].getPowerDataAvg())
        if(not arduinos[index].getIsActive()):
            arduinos[index].setIsActive(True)
        if(arduinos[index].getShutdown() != bool(shutdownFlag)):
            arduinos[index].setShutdown(bool(shutdownFlag))
    except ValueError:
        print("Could not parse number.")

    #  else:
    #     try:
    #         print("else")# arduinos.append(ArduinoData(MACaddr, bool(shutdownFlag), float(powerData)))
    #     except ValueError:
    #         print("Could not parse number.")

def interpretData(arduinos, index, dataSplit):
    isProtocol = False
    if len(dataSplit) == 5:
        if(dataSplit[0] == "ARDUINO"):
            updateArduino(arduinos,index, dataSplit[1], dataSplit[2], dataSplit[3])
            isProtocol = True

    return isProtocol
    