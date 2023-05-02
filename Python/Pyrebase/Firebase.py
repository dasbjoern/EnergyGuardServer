import pyrebase
from firebaseConfig import firebaseConfig
import time
from threading import Thread
import clientThread
Hostname = "192.168.137.186"
Port = 8888

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()
database = firebase.database()

db = firebase.database()
shutdownFlag = 0
while(True):
  time.sleep(1)
  sendData = "OK?"
  userData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/testflags/").get()
  for x in userData.each():
      shutdownFlag = x.val()
  
  flag = str(shutdownFlag)
  sendData = sendData + flag
  sendData = sendData + "?.\n"
  
  clientThread.createThread(Hostname, sendData)


# print(userData.key())


