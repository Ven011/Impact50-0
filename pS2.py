import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.4"
port = 8888
print (host)
print (port)
serversocket.bind((host, port))

class client(Thread):
	def __init__(self, socket, address):
		Thread.__init__(self)
		self.sock = socket
		self.addr = address
		self.start()
		
	def run(self):
		alive = True
		while alive:
			try:
				temp = self.sock.recv(1024).decode()
				self.sock.send(b'Oi you sent something to me')
				if(temp):
					print('Client sent:',temp)
				
			except:
				print('Client Ded')
				alive = False
serversocket.listen(5)
print ('server started and listening')
while 1:
	clientsocket, address = serversocket.accept()
	client(clientsocket, address)