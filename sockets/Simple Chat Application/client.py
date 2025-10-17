import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

localhost = '127.0.0.1'

sock.connect((localhost, 12345))

while True:
    message = input('Enter message to send to server: ')
    if message.strip().lower() == 'exit':
        break
    sock.sendall(message.encode())

    data = sock.recv(1024).decode()
    if (not data or data.strip().lower() == 'exit'):
        break
    print("Message from server: ", data)

sock.close()
    