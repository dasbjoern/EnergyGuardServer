import pyrebase
from ArduinoData import ArduinoData
from firebaseConfig import firebaseConfig
import time
from threading import Thread
import clientThread
import TCPClient
import timerStatus
import math


# Hostname = "192.168.137.94"
Hostname = "127.0.0.1"
Port = 8888
arduinos = []

firebase = pyrebase.initialize_app(firebaseConfig)

# INITIALIZE
db = firebase.database() 

devices = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/").get()
macaddressData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/mac_address").get()

arr = []
for x in devices.each():
  arr.append(x.val())
  print(x.val())


  # {'consumptionIndex': 103, 'id': 1, 'isActive': True, 'isTurnedOn': False,
  #  'name': 'Lamp', 'timer': False, 'timerEndDate': 0}
  #(self, MACaddr, deviceID, shutdown,consumptionIndex, timer, timerTime):
for i in range(len(arr)):
  arduinos.append(ArduinoData(arr[i]['macAddr'],arr[i]['id'], arr[i]['isTurnedOn'],arr[i]['consumptionIndex'], arr[i]['timer'], arr[i]['timerEndDate']))
print(arduinos[0].getMAC())
print(arduinos[0].getDeviceID())
print(arduinos[0].getShutdown())
print(arduinos[0].getConsumptionIndex())
print(arduinos[0].getTimer())
print(arduinos[0].getTimerTime())
# macaddress = userData.val()

# CREATE FUNC TO CALL DURING LOOP / EVERY MINUTE
macArr = []
for x in macaddressData.each():
  macArr.append([x.key(),x.val()])
print(macArr[0])
temp = []
for i in range(len(macArr)):
  temp = macArr.pop()
  for j in range(len(arduinos)):
    if temp[0] == arduinos[j].getMAC():
      arduinos[j].setIP(temp[1])
for i in range(len(arduinos)):
  print(arduinos[i].getIP())

# Hostname = macArr[0][1]
# print(Hostname)
timer = 0
timerStart = 0
timerFinished = True
shutdownFlag = 0
timeLoop = time.time()
consumptionIndex = 0
deviceID = 0
#todo read in all devices FIREBASE

while(True):
  db = firebase.database()  
  # time.sleep(1)
  if(time.time() - timeLoop >= 1):
    # print(time.time())
    print(round(time.time() - timeLoop))
    timeLoop = time.time()
    sendData = "OK?"
    # print("...// Gathering data from Firebase. //...")
    try:
      # userData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/isTurnedOn/value").get()

      statusData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/").get().val()
      print(consumptionIndex)

      isActive = statusData['isActive']
      consumptionIndex = statusData['consumptionIndex']
      shutdownFlag = statusData['isTurnedOn']
      timer = statusData['timer']
      timerEndDate = statusData['timerEndDate']

      # userData.val()
      # print("PRINT: ", userData.val())
      # for x in userData:
      # print(x.val())
      print(shutdownFlag)
      if(shutdownFlag == False):
        shutdownFlag = 0
      else:
        shutdownFlag = 1
      print("shutdownFlag: ", shutdownFlag)
      if len(arduinos):
        arduinos[0].setShutdown(shutdownFlag)
    except:
      print("pyrebase error shutdown.")
  
    try:
        timer = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/timerEndDate").get().val()
        timer = timer/1000
        print("TIME", timer)

  #     if type(timer) == str:
  #       timer = int(timer)
        if timer != 0 and timerFinished == True:
          timerStart = time.time()
          timerFinished = False
        if(timerStart != 0  and timerFinished == False):
          timerFinished = timerStatus.timerStatus(timer)
          if timerFinished:
            shutdownFlag = 0
            timerFinished = True
            db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/").child('isTurnedOn').set(False)
            db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/").child('timerEndDate').set(0)

  #     # print("TIMER: ")
    except:
      print("pyrebase error timer.")
    
    if len(arduinos):
      arduinos[0].setTimer(timer)
      # print(arduinos[0].getTimer())
    
    if(shutdownFlag == True):
      shutdownFlag = 1
    else:
      shutdownFlag = 0
    flag = str(shutdownFlag)
    sendData = sendData + flag
    sendData = sendData + "?.\n"

    # arduinos[0].setIP("NoIP") # REMOVE !!!!

    for i in range(len(arduinos)):
      if(arduinos[i].getIP() != "NoIP"):
        try:
          TCPClient.tcpClient(arduinos[i].getIP(), Port+i, sendData, arduinos[i])
          time.sleep(0.02)
        except:
          print("connection failed with IP: ", arduinos[i].getIP)
          arduinos[i].setIP("NoIP")
          # arduinos[i].setIsActive(False)
        # print("... Sending data to arduino: ", arduinos[i].getIP(),":",Port, " ...")
        # clientThread.createThread(arduinos[i].getIP(),Port+i, sendData, arduinos[i])
    # db.child("/Energyconsumption/").child(0).set([0,0])
    # length = len(db.child("/Energyconsumption/").get().val())
    # print("length:", length)
    # print(arduinos[0].getPowerDataLatest())
    
    # UPLOAD POWERDATA change child(1) to child(length)
    db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/consumption/value/0/values").child(consumptionIndex).set(arduinos[0].getPowerDataLatest())
    # consumptionIndex = consumptionIndex +1
    db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/").child('consumptionIndex').set(consumptionIndex+1)
  


# print(userData.key())


