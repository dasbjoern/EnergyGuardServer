import socket
import time
import sys
# from ArduinoData import ArduinoData
import sendUpdate

# port = 8888
arduinos = []
#ADD PORT VIA COMMANDLINE: python TCPClient.py <port>
if len(sys.argv) > 1:
    # print(str(sys.argv[1]))
    try:
        port = int(sys.argv[1])
        print("Connecting to port:", port)
        if len(sys.argv) > 2:
            try:
                host = sys.argv[2]
            except:
                print("System argument HOST Error.")
    except ValueError:
        print("Not a number: Default port set to 8888") 
    except:
        print("Unexpected error. ")
# code start

def tcpClient(host="127.0.0.1", port = 8888, sendData=""):
    # "192.168.137.21"
    # Host = "192.168.137.210"
    # Port = 8888
    
    shutdownFlag = 0

    while True:
        time.sleep(1)
        try:

            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect((host, port))
        # protocol: OK?SHUTDOWNFLAG?TIMERSEC?DATA.
            # sendData = "OK?"
            # flag = str(shutdownFlag)
            # sendData = sendData + flag
            # sendData = sendData + "?.\n"

            # sendData.concat("?.\n")

            print(sendData)

            clientSocket.sendall(sendData.encode("ascii"))
            shutdownFlag = (shutdownFlag +1)%2
            data = clientSocket.recv(1024)

            receiviedData = data.decode()
            dataSplit = receiviedData.split("?")
            for x in dataSplit:
                print(x)
            # print(dataSplit[0])
            if(sendUpdate.interpretData(arduinos, dataSplit)):
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


    


