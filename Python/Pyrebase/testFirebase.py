import pyrebase
from firebaseConfig import firebaseConfig
import time
from threading import Thread
import clientThread
import TCPClient
import math
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
# array = [["E",2, 3], ["F", 2,3]]
if(True):
  print("...// Gathering data from Firebase. //...")
  try:
    userData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/mac_address").get()
    macip = userData.val()
    print(len(macip))
    arr = []
    for x in userData.each():
      arr.append([x.key(),x.val()])
      print(x.key())
      print(x.val())
    print(arr[0])
    # print(macip[str(x)])
    # macip[0]
    # print(userData.val()[0])
    # userData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/").get().val()

    # consumptionIndex = userData['consumptionIndex']
    # print("isActive: ",userData['isActive'])
    # print("consumptionIndex: ",userData['consumptionIndex'])
    # print("isTurnedOn: ",userData['isTurnedOn'])
    # print("timer: ",userData['timer']) #0
    # timeEnd = userData['timerEndDate']
    # print("timerEndDate: ",timeEnd)
    # current = time.time()
    # print(current)

    # print(current*1000)
    # print(math.trunc(current*1000))
    # print(time.localtime(timeEnd/1000))
    # db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/0/").child('consumptionIndex').set(2)

    # userData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/consumption/value/0/values").child(consumptionIndex).set([1,2])
  except:
    print("crash")
  # for user in userData.val()[1]:
    # print(user)
  # data =  db.child("/Energyconsumption/").get()
  # print(len(data.val()))
  # array = userData.val()
  # print(array[0])
  # print(userData.val())
  # print(array.get())
  # print(array[0])
  # for x in array.each():
    # print(x)
   
        
  


# print(userData.key())


