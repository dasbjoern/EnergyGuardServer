import pyrebase
from firebaseConfig import firebaseConfig
import time
from threading import Thread
import clientThread
import TCPClient
import timerStatus
Hostname = "192.168.137.15"
# Hostname = "127.0.0.1"
Port = 8888
arduinos = []

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
timer = 0
timerStart = 0
timerFinished = True
shutdownFlag = 0
timeLoop = time.time()
while(True):
  # time.sleep(1)
  if(time.time() - timeLoop >= 1):
    # print(time.time())
    print(round(time.time() - timeLoop))
    timeLoop = time.time()
    sendData = "OK?"
    # print("...// Gathering data from Firebase. //...")
    try:
      userData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/devicelist/value/0/isTurnedOn/value").get()
      # userData.val()
      # print("PRINT: ", userData.val())
      # for x in userData:
      # print(x.val())
      shutdownFlag = userData.val()
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
        timer = db.child("/Timer/").get().val()
        print("TIME", timer)

  #     if type(timer) == str:
  #       timer = int(timer)
        if timer != 0 and timerFinished == True:
          timerStart = time.time()
          timerFinished = False
        if(timerStart != 0  and timerFinished == False):
          timerFinished = timerStatus.timerStatus(timer, timerStart)
          if timerFinished:
            shutdownFlag = 0
            timerFinished = True
            db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/devicelist/value/0/isTurnedOn/value").set(False)
            db.child("/Timer/").set(0)

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
  # clientThread.createThread(Hostname, sendData)
  


# print(userData.key())


