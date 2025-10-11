import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sendto is for the UDP
sock.sendto("Hello from client".encode(), ('127.0.0.1', 12345))