import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostbyname(socket.gethostname())
PORT = 50545

serverSocket.bind((HOST, PORT))
serverSocket.listen()  # Now the socket is listening for incoming connections

print(f"Server listening on {HOST}:{PORT}")  
clientSocket, addr = serverSocket.accept()# like When someone calls, pick up the phone.
print("Connected by", addr)  # Say who called you (their address).

data = clientSocket.recv(1024)  # Listen to their message. 1024 is the maximum number of letters (bytes) you can hear at once.

clientSocket.sendall(data)  # Say the same message back to them like a mirror .


clientSocket.close() 
serverSocket.close()  

