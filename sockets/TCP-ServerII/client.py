import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 8080))

while True:
    msg = input("Enter message to send to server (type 'exit' to quit): ")
    sock.send(msg.encode())
    if msg == 'exit':
        break

sock.close()