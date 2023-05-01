from datetime import datetime

class ArduinoData:

    MACAddress = "NoMAC"
    shutdown = False
    timer = 0
    powerData = []
    myMap: map

    def __init__(self, MACaddr, shutdown, timer, powerData):
        self.MACAddress = MACaddr
        self.shutdown = shutdown
        self.timer = timer
        self.powerData.append(powerData)
        # self.setEnergyData(powerData)
    def getMAC(self):
        return self.MACAddress  
    
    def setPowerData(self, powerData):
        self.powerData.append(powerData)
        # currentTime = datetime.datetime.now()
        # timeStamp = currentTime.timestamp()
        # dateTime = datetime.fromtimestamp(timeStamp)
        
        # self.myMap.put(dateTime, powerData)
    def getPowerData(self):
        return self.powerData
    def setShutdown(self, shutdown):
        self.shutdown = shutdown
    def getShutdown(self):
        return self.shutdown



# arduino = ArduinoData(1,1,1,1)
# print(arduino.energyData[0])
# print()