from ArduinoData import ArduinoData
from firebaseConfig import firebaseConfig
import pyrebase

def PowerCalc(Sec, arduino):
    i = 0
    PowerkWh = 0

    # db = firebase.database() 

    while i < Sec:
        if arduino.getPowerData() < 0:
            arduino.setPowerData(0)

        PowerkWh += arduino.getPowerDataLatest()
        # arduino.popPowerData()
        i += 1
    return PowerkWh
    print(PowerkWh + "Wh")
    # length = len(db.child("/Energyconsumption-kWh/").get().val())
    # db.child("/Energyconsumption-kWh/").child(length).set(PowerkWh, Sec)