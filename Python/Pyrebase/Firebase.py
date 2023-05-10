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
# Hostname = "127.0.0.1"
Port = 8888
arduinos = []

firebase = pyrebase.initialize_app(firebaseConfig)

# INITIALIZE
db = firebase.database() 

devices = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/").get()
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
  # print(arduinos[i].getMAC())
  # print(arduinos[i].getDeviceID())
  # print(arduinos[i].getShutdown())
  # print(arduinos[i].getConsumptionIndex())
  # print(arduinos[i].getTimer())
  # print(arduinos[i].getTimerTime())
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
      if(temp[1]=="NoIP"):
        arduinos[j].setIsActive(False)
      else:  
        arduinos[j].setIsActive(True)
for i in range(len(arduinos)):
  print(arduinos[i].getIP())

# Hostname = macArr[0][1]
# print(Hostname)
timer = 0
timerStart = 0
timerFinished = True
# shutdownFlag = 0
timeLoop = time.time()
consumptionIndex = 0
deviceID = 0
timeMinute = time.time()
#todo read in all devices FIREBASE
statusPathDb = "users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/"
consumptionPathDb = "users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/consumption/"
while(True):
  db = firebase.database()  
  # time.sleep(1)
  if(time.time() - timeLoop >= 1):
    # print(time.time())
    # print(round(time.time() - timeLoop))
    timeLoop = time.time()
    # sendData = "OK?"
    # print("...// Gathering data from Firebase. //...")
    try:
      # userData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/isTurnedOn/value").get()
      statusData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/").get().val()
      for status in statusData:
        # status = statusData.pop()
        for ard in arduinos:
          # print(ard.getMAC())
          if(status['macAddr'] == ard.getMAC()):
            ard.setShutdown(status['isTurnedOn'])
            ard.setConsumptionIndex(status['consumptionIndex'])
            # print("consindex:",ard.getConsumptionIndex(), ard.getMAC())
            ard.setTimer(status['timer'])
            ard.setTimerTime(status['timerEndDate'])

      # for ard in arduinos:
      #   print(ard.getMAC(), ard.getShutdown())
      #   print(ard.getConsumptionIndex())
      # # time.sleep(10)
      # statusData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/0/").get().val()
      # print(consumptionIndex)

      # isActive = statusData['isActive']
      # consumptionIndex = statusData['consumptionIndex']
      # shutdownFlag = statusData['isTurnedOn']
      # timer = statusData['timer']
      # timerEndDate = statusData['timerEndDate']

    except:
      print("pyrebase error shutdown.")
  
  #   try:
  #       for i in range(len(arduinos)):
  #         if(arduinos.getIsActive == True):
  #           timer = db.child(statusPathDb + str(i) +"/" + "timerEndDate").get().val()
  #           timer = timer/1000
  #           print("TIME", timer)

  # #     if type(timer) == str:
  # #       timer = int(timer)
  #           if timer != 0 and timerFinished == True:
  #             timerStart = time.time()
  #             timerFinished = False
  #           if(timerStart != 0  and timerFinished == False):
  #             timerFinished = timerStatus.timerStatus(timer)
  #           if timerFinished:
  #             shutdownFlag = 0
  #             timerFinished = True
  #             db.child(statusPathDb + str(i) +"/").child('isTurnedOn').set(False)
  #             db.child(statusPathDb + str(i) +"/").child('timerEndDate').set(0)

  # #     # print("TIMER: ")
  #   except:
  #     print("pyrebase error timer.")
    
  

    # arduinos[0].setIP("NoIP") # REMOVE !!!!

  for i in range(len(arduinos)):
    if(arduinos[i].getIP() != "NoIP"):
      try:
        TCPClient.tcpClient(arduinos[i].getIP(), Port, arduinos, i)
        time.sleep(0.05)
      except:
        print("Firebase.py: connection failed with IP: ", arduinos[i].getIP())
          # arduinos[i].setIP("NoIP")
  for i in range(len(arduinos)):
    if(arduinos[i].getIsActive() == True):
      print(arduinos[i].getConsumptionIndex())
      db.child(consumptionPathDb + str(i) + "/values").child(arduinos[i].getConsumptionIndex()).set(arduinos[i].getPowerData())
      db.child(statusPathDb + str(i) +"/").child('consumptionIndex').set(arduinos[i].getConsumptionIndex()+1)
  


# print(userData.key())


