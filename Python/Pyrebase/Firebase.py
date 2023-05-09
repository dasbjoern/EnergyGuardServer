import pyrebase
from firebaseConfig import firebaseConfig
import time
from threading import Thread
# import clientThread
import TCPClient
import timerStatus
import math


# Hostname = "192.168.137.94"
Hostname = "127.0.0.1"
Port = 8888
arduinos = []

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database() 
macaddressData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/mac_address").get()
# macaddress = userData.val()

macArr = []
for x in macaddressData.each():
  macArr.append([x.key(),x.val()])

Hostname = macArr[0][1]
print(Hostname)
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
    print("... Sending data to arduino: ", Hostname,":",Port, " ...")
    TCPClient.tcpClient(Hostname, Port, sendData, arduinos)
    # db.child("/Energyconsumption/").child(0).set([0,0])
    length = len(db.child("/Energyconsumption/").get().val())
    print("length:", length)
    # print(arduinos[0].getPowerDataLatest())
    
    # UPLOAD POWERDATA change child(1) to child(length)
    db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/consumption/value/0/values").child(consumptionIndex).set(arduinos[0].getPowerDataLatest())
    # consumptionIndex = consumptionIndex +1
    db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/").child('consumptionIndex').set(consumptionIndex+1)
  # clientThread.createThread(Hostname, sendData)
  


# print(userData.key())


