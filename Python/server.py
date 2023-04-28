import socket

port = 8080
ip = "192.168.137.26"
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((ip,port))
print("Server started on port %s", port)
while True:
    serverSocket.listen()
    clientSocket, clientAddress = serverSocket.accept()
    print("connected with", clientAddress)

    data = clientSocket.recv(1024)
    print(data.decode())
    

    clientSocket.sendall(b"HELLO?THERE.")

    clientSocket.close()


