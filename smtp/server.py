import socket
import os.path
port=1234
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',port))
s.listen(2)
while True:
	conn, addr=s.accept()
	namepass=conn.recv(1024)
	namepass=namepass+"\n"
	print str(namepass)+"\n"
	filepath = 'names'  
	fp=open(filepath,'r')  
	line = fp.readline()
	print line
	flag="0"
	while line:
		if line==str(namepass):
			flag="1"
			break
		line = fp.readline()
	conn.send(flag)
	if flag=="1":
		to=conn.recv(1024)
		content=conn.recv(1024)
		
		print str(mail)
	conn.close()

