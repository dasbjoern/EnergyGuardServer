import socket

port = 8888
ip = "127.0.0.1"
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((ip,port))
print("Server started on port %s", port)
while True:
    try:
        serverSocket.listen()
        clientSocket, clientAddress = serverSocket.accept()
        print("connected with", clientAddress)

        data = clientSocket.recv(1024)
        print(data.decode())
    

        clientSocket.sendall(b"ARDUINO?MAC?0?TIMER?DATA?.")

        clientSocket.close()
    except:
        print("Unexpected error. ")

