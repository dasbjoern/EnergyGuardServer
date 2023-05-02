import pyrebase
from firebaseConfig import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()
database = firebase.database()

db = firebase.database()
userData = db.child("users/rh9hxkJsnhRVqWYZfqUi6mEWAAx1/testflags/").get()
shutdown = userData[0].val()

print(shutdown)


