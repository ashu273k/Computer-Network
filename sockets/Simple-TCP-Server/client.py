import socket

# Socket is created here
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF -> Address family; INET -> IPV4
# SOCK_STREAM -> TCP

# Connect to the server
sock.connect(("127.0.0.1", 12345))

sock.send("Hello from client".encode())