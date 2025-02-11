import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostbyname(socket.gethostname())
PORT = 50545

clientSocket.connect((HOST, PORT))
# Now use send()/recv() to communicate
clientSocket.sendall(b"Hello, Server I am client :) ")
# The "b" before the message means we're sending it in a special format (bytes).
data = clientSocket.recv(1024)
print("hurreyy Received !!!", data.decode())
clientSocket.close()
