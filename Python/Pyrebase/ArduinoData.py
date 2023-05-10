from datetime import datetime
import time
import math

class ArduinoData:

    MACAddress = "NoMAC"
    deviceID = 0
    shutdown = False
    powerData = []
    timer = False
    timerTime = 0
    isActive = False
    powerDataAvg = 0
    consumptionIndex = 0
    ip = "NoIP"

    def __init__(self, MACaddr, deviceID, shutdown,consumptionIndex, timer, timerTime):
        self.MACAddress = MACaddr
        self.deviceID = deviceID
        self.shutdown = shutdown
        self.consumptionIndex = consumptionIndex
        self.timer = timer
        self.timerTime = timerTime
        # self.isActive = isActive
        # self.powerData.append([powerData,math.trunc(time.time()*1000)])

        # self.setEnergyData(powerData)
    def getMAC(self):
        return self.MACAddress  
    def setMAC(self, mac):
        self.MACAddress = mac
    def getDeviceID(self):
        return self.deviceID
    def setDeviceID(self, id):
        self.deviceID = id
    def getIsActive(self):
        return self.isActive
    def setIsActive(self, active):
        self.isActive = active
    def setPowerData(self, powerData):
        if(len(self.powerData) == 10):
            # self.setPowerDataAvg()
            self.powerData.clear()
            self.powerData.append([powerData,math.trunc(time.time()*1000)])
        else:
            self.powerData.append([powerData,math.trunc(time.time()*1000)])
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
    def getPowerDataLatest(self):
        length = len(self.powerData)
        # print(length)

        return self.powerData[length-1]
    def setShutdown(self, shutdown):
        self.shutdown = shutdown
    def getShutdown(self):
        return self.shutdown
    def getConsumptionIndex(self):
        return self.consumptionIndex
    def setConsumptionIndex(self, index):
        self.consumptionIndex = index
    def setTimer(self, time):
        self.timer= time
    def getTimer(self):
        return self.timer
    def getTimerTime(self):
        return self.timerTime
    def setTimerTime(self, time):
        self.timerTime = time
    def setIP(self, ip):
        self.ip = ip
    def getIP(self):
        return self.ip
    def getAddr(self):
        return (self.ip,8888)

# arduino = ArduinoData(1,1,1,1)
# print(arduino.energyData[0])
# print()