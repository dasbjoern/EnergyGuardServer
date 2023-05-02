from threading import Thread
import threading
import socket
import time
import sys
from ArduinoData import ArduinoData
import sendUpdate
Hostname = "192.168.137.186"
Port = 8888
arduinos = []
lock = threading.Lock()

def createThread(Hostname,data):


    try:
        i = 0
        aThread = Thread(target = tcpClient, args=(Hostname,8888, data)).start()


        aThread.join()
        Thread.sleep(10)
    except:
        print("Thread could not be created")
   
        

def tcpClient(Host, Port, senddata):
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((Host, Port))
        # protocol: OK?SHUTDOWNFLAG?TIMERSEC?.
        clientSocket.sendall(senddata.encode("ascii"))
        data = clientSocket.recv(1024)
        recvData = data.decode()
        dataSplit = recvData.split("?")
        for x in dataSplit:
            print(x)

        lock.acquire()
        # print(dataSplit[0])
        if(sendUpdate.interpretData(arduinos, dataSplit)):
            print("PROTOCOL: OK ")
        else:
            print("PROTOCOL: MISSMATCH ")
        clientSocket.close()
        lock.release()
    
    except TimeoutError:
        print("Socket timeout. ")
        if lock.locked():
            lock.release()
    except ConnectionRefusedError:
        print("Connection could not be made. ")
        if lock.locked():
            lock.release()
    except:
        print("Unexpected error. ")
        if lock.locked():
            lock.release()
    

# def run(self):
    # protocol: OK?SHUTDOWNFLAG?TIMERSEC?.
    
    
    # self.sendall(b"OK?0?36000?.\n")

    # data = self.recv(1024)

    # print(data.decode())



        
    

