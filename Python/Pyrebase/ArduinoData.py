from datetime import datetime
import time
import math

class ArduinoData:

    MACAddress = "NoMAC"
    deviceID = 0
    shutdown = False
    powerData = []
    limit = 0
    powerLimitCalc = 0
    timer = False
    timerTime = 0
    isActive = False
    powerDataAvg = []
    consumptionIndex = 0
    ip = "NoIP"

    def __init__(self, MACaddr, deviceID, shutdown,consumptionIndex):
        self.MACAddress = MACaddr
        self.deviceID = deviceID
        self.shutdown = shutdown
        self.consumptionIndex = consumptionIndex
        # self.timer = timer
        # self.timerTime = timerTime
        # self.isActive = isActive
        # self.powerData.append([powerData,math.trunc(time.time()*1000)])

        # self.setEnergyData(powerData)
    def powerLimit(self):
        
        if self.limit > 0 and self.powerLimitCalc < self.limit:
            self.powerLimitCalc += self.getPowerDataLatest()[0]
        elif self.limit != 0 and self.powerLimitCalc >= self.limit:
            self.shutdown = False
            self.limit = 0
            self.powerLimitCalc = 0
            # self.getShutdown()
        else:
            self.powerLimitCalc = 0
        return self.shutdown
    
    def PowerCalc(self, sec):
        i = 0
        PowerkWh = 0

        while i < sec:
            
            powerData = self.getPowerDataPopFirst()
            if(powerData[0] < 0):
                powerData[0]=0
            PowerkWh = PowerkWh + powerData[0]
        # arduino.popPowerData()
            i = i + 1
        print(PowerkWh + "Wh")

        self.setPowerDataAvg(PowerkWh, sec)
        return self.getPowerDataAvg()
    def getLimit(self):
        return self.Limit
    def setLimit(self, limit):
        self.limit = limit
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
        if(powerData < 0):
            powerData = 0
        self.powerData.append([powerData,math.trunc(time.time()*1000)])
        # currentTime = datetime.datetime.now()
        # timeStamp = currentTime.timestamp()
        # dateTime = datetime.fromtimestamp(timeStamp)
        # self.myMap.put(dateTime, powerData)
        
    def setPowerDataAvg(self, powerData, sec):
        print("POWER DATA: ", round(powerData/sec, 2))
        self.powerDataAvg = [round(powerData/sec, 2),math.trunc(time.time()*1000)]
    def getPowerDataAvg(self):
        return self.powerDataAvg
    def getPowerData(self):
        return self.powerData
    def getPowerDataLatest(self):
        length = len(self.powerData)
        # print(length)
        return self.powerData[length-1]
    def getPowerDataPopFirst(self):
        return self.powerData.pop(0)
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