import socket


# Socket is created here
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF -> Address family;  INET(Internet) -> IPv4
# SOCK_STREAM -> TCP

interface = "127.0.0.1"
PORT = 12345

# Binding happens here
sock.bind((interface, PORT))
# Why we are adding IP address and Port
 # IP address -> Address of the machine
 # Port -> Application running on the machine

print(f"Socket is bound to the port {PORT}")

# Listening happens here
sock.listen() # Optional parameter can be passed to specify number of connections
print("Socket is listening")


# Accepting connections
conn, addr = sock.accept()
# connection object (returned) is another socket object which is used to communicate

# Why two socket objects?
# 1. The original socket (sock) is used to accept incoming connections. (Free to accept more connections)
# 2. The new socket (conn) is used to communicate with the connected client.
print(f"Got connection from client: {addr}")

data = conn.recv(1024) # Buffer size can be passed as an argument (Maximum size it can accept at a time)
print(f"Data from client = {data.decode()}")
# Decoding bytes to string

# Close the connections (Good practice)
conn.close()
sock.close()