import socket

TCP_IP = '192.168.1.4'
TCP_PORT = 8888
BUFFER_SIZE = 1024
MESSAGE = "1000"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode('utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()
print("received data:", data)