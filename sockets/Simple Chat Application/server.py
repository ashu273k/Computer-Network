import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

localHost = '127.0.0.1'
PORT = 12345

sock.bind((localHost, PORT))
sock.listen()

conn, addr = sock.accept()
while True:
    data = conn.recv(1024).decode()
    if not data or data.strip().lower() == 'exit':
        break
    print("Message from client: ", data)
    message = input("Enter message to send to client: ")
    conn.sendall(message.encode())

conn.close()
sock.close()