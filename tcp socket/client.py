import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1234
s.connect(('127.0.0.1',port))
data = ""
while True and str(data) != "bye":
	data=raw_input('->')
	s.send(data.encode())
	data=s.recv(1024).decode()
	print "server : "+str(data)
s.close()