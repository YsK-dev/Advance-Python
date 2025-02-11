import socket

PORT=12345
SERVER=socket.gethostbyname(socket.gethostname())
ADDRESS=(SERVER, PORT)
FORMAT="utf-8"
BYTESIZE=1024
DISCONNECT_MESSAGE="quit"

server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

server.bind(ADDRESS)
server.listen()
print("Server is working")

clientSocket, clientAddress =server.accept()

clientSocket.send("Server connection successfuly made\n".encode(FORMAT))

while True:
    message = clientSocket.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        clientSocket.send("quit".encode(FORMAT))
        print("time to say GOOD BYE")
    else:
        print(f"{message}\n")
        message=input("Your message: ")
        clientSocket.send(message.encode(FORMAT))

server.close()