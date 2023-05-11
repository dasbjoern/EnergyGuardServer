import socket
import time
import sys
# from ArduinoData import ArduinoData
import sendUpdate

# port = 8888

# arduinos = []
#ADD PORT VIA COMMANDLINE: python TCPClient.py <port>

# code start

def tcpClient(host, port, arduinos, index):
    print("... Sending data to arduino: ", host,":",port, " ...")
    # "192.168.137.21"
    # Host = "192.168.137.210"
    # Port = 8888

    #time.sleep(1)
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # clientSocket.setblocking(False)
        
        clientSocket.settimeout(0.5) #test

        clientSocket.connect((host, port))
        # protocol: OK?SHUTDOWNFLAG?TIMERSEC?DATA.
            # sendData = "OK?"
            # flag = str(shutdownFlag)
            # sendData = sendData + flag
            # sendData = sendData + "?.\n"

            # sendData.concat("?.\n")
      # print(arduinos[0].getTimer())
        shutdownFlag = 0
        sendData = "OK?"
        # print("TCP: shut", arduino.getShutdown())
        if(arduinos[index].getShutdown() == True):
            shutdownFlag = 1
        else:
            shutdownFlag = 0
        flag = str(shutdownFlag)
        sendData = sendData + flag
        sendData = sendData + "?.\n"

        print(sendData)
        clientSocket.sendall(sendData.encode("ascii"))
        # shutdownFlag = (shutdownFlag +1)%2
        data = clientSocket.recv(1024)

        receiviedData = data.decode()
        
        print(receiviedData)
        dataSplit = receiviedData.split("?")
        # for x in dataSplit:
            # print(x)
        # print(dataSplit[0])
        if(sendUpdate.interpretData(arduinos, index, dataSplit)):
            print("PROTOCOL: OK ")
        else:
            print("PROTOCOL: MISSMATCH ")
        clientSocket.close()
    except TimeoutError:
        clientSocket.close()
        arduinos[index].setIP("NoIP")
        arduinos[index].setIsActive(False)
        print("Socket timeout. ")
    except ConnectionRefusedError:
        clientSocket.close()
        arduinos[index].setIP("NoIP")
        arduinos[index].setIsActive(False)
        print("Connection could not be made. ")
    except:
        clientSocket.close()
        print("TCPClient.py: Connection Unexpected error, wrong IP: ", arduinos[index].getIP())
        arduinos[index].setIP("NoIP")
        arduinos[index].setIsActive(False)
        # arduino.setIsActive(False)


    


