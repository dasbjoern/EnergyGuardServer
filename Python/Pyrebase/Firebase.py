import pyrebase
from ArduinoData import ArduinoData
from firebaseConfig import firebaseConfig
import time
from threading import Thread
import clientThread
import TCPClient
import timerStatus
import math
def findIP(arduinos,userid, db):
  # db = firebase.database() 
  macaddressData = db.child("users/"+ userid +"/mac_address").get()
  macArr = []
  for x in macaddressData.each():
    macArr.append([x.key(),x.val()])
  # print(macArr[0])
  temp = []
  for i in range(len(macArr)):
    temp = macArr.pop()
    for j in range(len(arduinos)):
      if temp[0] == arduinos[j].getMAC():
        arduinos[j].setIP(temp[1])
        temp[0] = "found"
        if(temp[1]=="NoIP"):
          arduinos[j].setIsActive(False)
        else:  
          arduinos[j].setIsActive(True)
    # if(temp[0] != "found"):
      # print("unkown device")
  for i in range(len(arduinos)):
    print(arduinos[i].getIP())


# Hostname = "192.168.137.94"
# Hostname = "127.0.0.1"
energyHubID = "energyguard"
Port = 8888
arduinos = []

firebase = pyrebase.initialize_app(firebaseConfig)

# INITIALIZE
db = firebase.database()
userid = db.child("hubID/"+ energyHubID + "/").get().val()

while(userid == None):
  userid = db.child("hubID/"+ energyHubID + "/").get().val()

db = firebase.database()
 

devices = db.child("users/"+ userid +"/status/").get()
macaddressData = db.child("users/"+ userid +"/mac_address").get()

arr = []
for x in devices.each():
  arr.append(x.val())
  # print(x.val())


  # {'consumptionIndex': 103, 'id': 1, 'isActive': True, 'isTurnedOn': False,
  #  'name': 'Lamp', 'timer': False, 'timerEndDate': 0}
  #(self, MACaddr, deviceID, shutdown,consumptionIndex, timer, timerTime):
for i in range(len(arr)):
  arduinos.append(ArduinoData(arr[i]['macAddr'],arr[i]['id'], arr[i]['isTurnedOn'],arr[i]['consumptionIndex']))
  # print(arduinos[i].getMAC())
  # print(arduinos[i].getDeviceID())
  # print(arduinos[i].getShutdown())
  # print(arduinos[i].getConsumptionIndex())
  # print(arduinos[i].getTimer())
  # print(arduinos[i].getTimerTime())
# macaddress = userData.val()

# CREATE FUNC TO CALL DURING LOOP / EVERY MINUTE
findIP(arduinos,userid, db)
# Hostname = macArr[0][1]
# print(Hostname)
timer = 0
timerStart = 0
timerFinished = True
# shutdownFlag = 0
timeLoop = time.time()
consumptionIndex = 0
deviceID = 0
timeRescan = time.time()
timePowerData = time.time()
sendPowerDataInterval = 10
#todo read in all devices FIREBASE
statusPathDb = "users/"+ userid +"/status/"
consumptionPathDb = "users/"+ userid +"/consumption/"

while(True):
  # time.sleep(1)
  if(time.time() - timeLoop >= 1):
    db = firebase.database()  
    # print(time.time())
    # print(round(time.time() - timeLoop))
    timeLoop = time.time()
    # sendData = "OK?"
    # print("...// Gathering data from Firebase. //...")
    try:
      # userData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/isTurnedOn/value").get()
      statusData = db.child(statusPathDb).get().val()
      for status in statusData:
        # status = statusData.pop()
        for ard in arduinos:
          # print(ard.getMAC())
          if(status['macAddr'] == ard.getMAC()):
            ard.setShutdown(status['isTurnedOn'])
            ard.setConsumptionIndex(status['consumptionIndex'])
            ard.setLimit(status['powerLimit'])



      # isActive = statusData['isActive']
      # consumptionIndex = statusData['consumptionIndex']
      # shutdownFlag = statusData['isTurnedOn']
      # timer = statusData['timer']
      # timerEndDate = statusData['timerEndDate']

    except:
      print("pyrebase error shutdown.")
  
    try:
        for i in range(len(arduinos)):
          if(arduinos[i].getIsActive() == True):
            timer = db.child(statusPathDb + str(i) +"/" + "timer").get().val()
            if(timer):
              if(not arduinos[i].getTimer()):
                timerEndTime = db.child(statusPathDb + str(i) +"/" + "timerEndDate").get().val()
                timerEndTime = timerEndTime/1000
                arduinos[i].setTimer(timer)
                arduinos[i].setTimerTime(timerEndTime)
              
              if(arduinos[i].getTimer()):
                if(timerStatus.timerStatus(arduinos[i].getTimerTime())):
                  # print("timer 4", timerStatus.timerStatus(arduinos[i].getTimerTime()))
                  db.child(statusPathDb + str(i) +"/" + "timer").set(False)
                  db.child(statusPathDb + str(i) +"/" + "isTurnedOn").set(not arduinos[i].getShutdown())
                  arduinos[i].setTimer(False)
    except:
      print("pyrebase error timer.")
    
  

    # Check for renewed ips
    if(time.time() - timeRescan >= 60):
      findIP(arduinos, userid, db)
      timeRescan=time.time()

    for i in range(len(arduinos)):
      if(arduinos[i].getIP() != "NoIP"):
        try:
          TCPClient.tcpClient(arduinos[i].getIP(), Port, arduinos, i)
          # time.sleep(0.05)
        except:
          print("Firebase.py: connection failed with IP: ", arduinos[i].getIP())
    
    try:
      for i in range(len(arduinos)):
        if(arduinos[i].getIsActive() == True):
          if(arduinos[i].getShutdown() == True):
            if(arduinos[i].powerLimit() == False):
              db.child(statusPathDb + str(i) +"/" + "powerLimit").set(0)
              db.child(statusPathDb + str(i) +"/" + "isTurnedOn").set(False)
    except:
      print("pyrebase error power limit")

    for i in range(len(arduinos)):
      if(arduinos[i].getIsActive() == True):
      # print(arduinos[i].getConsumptionIndex())
        # db = firebase.database()
        db.child(statusPathDb + str(i) +"/").child('isActive').set(True)
        if(round(time.time()-timePowerData >= sendPowerDataInterval)):
          if(len(arduinos[i].getPowerData()) >= 10):
            db.child(consumptionPathDb + str(i) + "/values").child(arduinos[i].getConsumptionIndex()).set(arduinos[i].PowerCalc(sendPowerDataInterval))
            db.child(statusPathDb + str(i) +"/").child('consumptionIndex').set(arduinos[i].getConsumptionIndex()+1)
            timePowerData = time.time()
      else:
        db.child(statusPathDb + str(i) +"/").child('isActive').set(False)

# print(userData.key())


