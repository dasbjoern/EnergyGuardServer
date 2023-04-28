import socket
import time
#import ArduinoData

Host = "192.168.137.21"
Port = 8888


while True:

    time.sleep(1)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((Host, Port))
    clientSocket.sendall(b"OK?0?36000\n")
    data = clientSocket.recv(1024)

    receiviedData = data.decode()
    dataSplit = receiviedData.split("?")

    for x in dataSplit:
        print(x)

    clientSocket.close()