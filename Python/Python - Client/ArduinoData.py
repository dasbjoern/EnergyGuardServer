from datetime import datetime

class ArduinoData:

    MACAddress = "NoMAC"
    shutdown = False
    timer = 0
    energyData[100] = {0}

    def __init__(self, MACaddr, shutdown, timer, powerData):
        self.MACAddress = MACaddr
        self.shutdown = shutdown
        self.timer = timer
        self.setEnergyData(powerData)
        
    
    def setEnergyData(self, powerData):
        currentTime = datetime.datetime.now()

        timeStamp = currentTime.timestamp()
        dateTime = datetime.fromtimestamp(timeStamp)
        self.energyData.put(dateTime, powerData)
    
    



