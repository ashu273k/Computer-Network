import socket

# Socket creation
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8080
# Binding the socket to the host and port
sock.bind((host, port))

# Listening for incoming connections by default it listen for 1 connection
sock.listen()
print(f"Server started listening on {host}:{port}")

# Accepting a connection
conn, addr = sock.accept()
print(f"Connection established with {addr}")
while True:
    # Receiving data from the client
    data = conn.recv(1024)
    if not data:
        break
    print(f"Received from client: {data.decode()}")
    
conn.close()
sock.close()