import socket
import time
from ArduinoData import ArduinoData
# "192.168.137.21"
Host = "127.0.0.1"
Port = 8888
arduinos = []

def updateArduinos(arduinos, MACaddr, shutdownFlag, timer, powerData):
    if(len(arduinos) > 0):
        for ard in arduinos:
            if ard.getMAC() == MACaddr:
                ard.setPowerData(powerData)
                print(ard.getPowerData())

    else:
        arduinos.append(ArduinoData(MACaddr, shutdownFlag, timer, powerData))

def interpretData(arduinos, dataSplit):
    isProtocol = False
    if len(dataSplit) == 6:
        if(dataSplit[0] == "ARDUINO"):
            updateArduinos(arduinos, dataSplit[1], 1,dataSplit[3],1)
            isProtocol = True
    

    # print(len(dataSplit))

    return isProtocol

while True:

    time.sleep(1)
    try:
        
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((Host, Port))
        clientSocket.sendall(b"OK?0?36000\n")
        data = clientSocket.recv(1024)

        receiviedData = data.decode()
        dataSplit = receiviedData.split("?")
        for x in dataSplit:
            print(x)

        # print(dataSplit[0])
        if(interpretData(arduinos, dataSplit)):
            print("PROTOCOL: OK ")
        else:
            print("PROTOCOL: MISSMATCH ")
    
        clientSocket.close()
    except TimeoutError:
        print("Socket timeout. ")
    except ConnectionRefusedError:
        print("Connection could not be made. ")
    except:
        print("Unexpected error. ")


    


