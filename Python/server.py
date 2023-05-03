import socket
import sys

port = 8888
ip = "127.0.0.1"
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) > 1:
    try:
        port = int(sys.argv[1])
        print("Connecting to port:", port)
    except ValueError:
        print("Not a number: Default port set to 8888") 
    except:
        print("Unexpected error. ")

serverSocket.bind((ip,port))
print("Server started on port %s", port)
while True:
    try:
        serverSocket.listen()
        clientSocket, clientAddress = serverSocket.accept()
        print("connected with", clientAddress)

        data = clientSocket.recv(1024)
        print(data.decode())
    

        clientSocket.sendall(b"ARDUINO?MAC?0?412?.")

        clientSocket.close()
    except:
        print("Unexpected error. ")

