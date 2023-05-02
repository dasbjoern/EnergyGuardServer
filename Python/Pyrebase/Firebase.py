import pyrebase
from firebaseConfig import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()
database = firebase.database()

db = firebase.database()
data = {
  'name':"ABC",
  'age':"12"
}
db.push(data)
print("hello")