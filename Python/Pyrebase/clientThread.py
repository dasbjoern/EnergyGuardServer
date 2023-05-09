from threading import Thread
import threading
import socket
import time
import sys
from ArduinoData import ArduinoData
import sendUpdate
# hostname = "192.168.137.94"
# port = 8888
# arduinos = []
lock = threading.Lock()

# class clientThread:
#     hostname = "192.168.137.186"
#     Port = 8888

#     def __init__(self,hostname, port):
#         self.hostname = hostname
#         self.port = port

def createThread(hostname,port,data, arduino):

    try:
        aThread = Thread(target = tcpClient, args=(hostname,port, data, arduino)).start()
        try:
            Thread.sleep(0.05)
            aThread.join()
        except:
            print("Could not join")
    except:
        print("Thread could not be created")
   
        

def tcpClient(Host, Port, senddata, arduino):
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((Host, Port))
        # protocol: OK?SHUTDOWNFLAG?TIMERSEC?.
        
        clientSocket.sendall(senddata.encode("ascii"))

        data = clientSocket.recv(1024)
        
        recvData = data.decode()
        dataSplit = recvData.split("?")
        # for x in dataSplit:
        #     print(x)

        lock.acquire()
        # print(dataSplit[0])
        if(sendUpdate.interpretData(arduino, dataSplit)):
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



        
    

