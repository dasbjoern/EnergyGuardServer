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
    
    # devices = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/").get()
    # macaddr = "ec:62:60:81:14:a8"

    db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/mac_address/").child("ab:62:60:81:14:e3").set("127.0.0.1")
    db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/mac_address/").child("dc:62:60:81:14:a2").set("127.0.0.1")
    # db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/1/").child("macAddr").set("ab:62:60:81:14:e3")
    # db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/2/").child("macAddr").set("dc:62:60:81:14:a2")
    # db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/3/").child("macAddr").set("e4:62:60:81:14:b4")
    # db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/status/value/4/").child("macAddr").set("ae:62:60:81:14:8a")
  #   arr = []
  #   for x in devices.each():
  #     arr.append(x.val())
  #     print(x.val())
  #   print(len(arr))
  # # {'consumptionIndex': 103, 'id': 1, 'isActive': True, 'isTurnedOn': False,
  # #  'name': 'Lamp', 'timer': False, 'timerEndDate': 0}
  #   print(arr[0]['isActive'])
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


