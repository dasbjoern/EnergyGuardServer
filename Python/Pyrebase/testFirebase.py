import pyrebase
from firebaseConfig import firebaseConfig
import time
from threading import Thread
import clientThread
import TCPClient
Hostname = "192.168.137.152"
# Hostname = "127.0.0.1"
Port = 8888
arduinos = []

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
timer = 0
timerStart = 0
timerCount = 1
shutdownFlag = 0
array = [["E",2, 3], ["F", 2,3]]
if(True):
  print("...// Gathering data from Firebase. //...")
  userData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/testdata/").get()
  array = userData.val()
  print(array[0])
  # print(userData.val())
  # print(array.get())
  # print(array[0])
  # for x in array.each():
    # print(x)
   
        
  


# print(userData.key())


