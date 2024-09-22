#!/usr/bin/env python3
import socket
import sys
		
def serverStart():

	print("Server Starting")
	HOST = ''
	PORT = 8888
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	print("Socket created")
	s.listen(10)
	print("Now Listening")
	while 1:
		conn, addr = s.accept()
		print('Connected with ' + addr[0] + '+' + str(addr[1]))
		conn.send("HI".encode('ascii'))
		print('Client sent:', s.recv(1024).decode())
	s.close()
		
	
serverStart()
