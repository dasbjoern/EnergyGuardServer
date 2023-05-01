import socket
import time
import sys
# from ArduinoData import ArduinoData
import sendUpdate


# "192.168.137.21"
Host = "127.0.0.1"
Port = 8888
arduinos = []

#ADD PORT VIA COMMANDLINE: python TCPClient.py <port>
if len(sys.argv) > 1:
    # print(str(sys.argv[1]))
    try:
        Port = int(sys.argv[1])
        print("Connecting to port:", Port)
    except ValueError:
        print("Not a number: Default port set to 8888") 
    except:
        print("Unexpected error. ")
# code start

while True:

    time.sleep(1)
    try:

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((Host, Port))
        # protocol: OK?SHUTDOWNFLAG?TIMERSEC?DATA.
        clientSocket.sendall(b"OK?0?36000?.\n")
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


    


