from datetime import datetime

class ArduinoData:

    MACAddress = "NoMAC"
    shutdown = False
    powerData = []
    timer = 0
    powerDataAvg = 0
    (ip, port) = ("LOCALHOST",8888)

    def __init__(self, MACaddr, shutdown, powerData):
        self.MACAddress = MACaddr
        self.shutdown = shutdown
        self.powerData.append(powerData)

        # self.setEnergyData(powerData)
    def getMAC(self):
        return self.MACAddress  
    
    def setPowerData(self, powerData):
        if(len(self.powerData) == 10):
            self.setPowerDataAvg()
            self.powerData.clear()
            self.powerData.append(powerData)
        else:
            self.powerData.append(powerData)
        # currentTime = datetime.datetime.now()
        # timeStamp = currentTime.timestamp()
        # dateTime = datetime.fromtimestamp(timeStamp)
        # self.myMap.put(dateTime, powerData)
        
    def setPowerDataAvg(self):
        sum = 0
        for x in self.powerData:
            sum = sum + x
        self.powerDataAvg = sum/10
    def getPowerDataAvg(self):
        return self.powerDataAvg
    def getPowerData(self):
        return self.powerData
    def setShutdown(self, shutdown):
        self.shutdown = shutdown
    def getShutdown(self):
        return self.shutdown
    def setTimer(self, time):
        self.timer= time
    def getTimer(self):
        return self.timer
    def setAddr(self, ip, port=8888):
        self.ip = ip
        self.ip = port
    def getAddr(self):
        return (self.ip, self.port)

# arduino = ArduinoData(1,1,1,1)
# print(arduino.energyData[0])
# print()