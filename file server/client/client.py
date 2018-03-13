import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1234
host='127.0.0.1'
s.connect((host,port))
data=raw_input('enter file name :')
s.send(data)			#sending file name
d=s.recv(1024)			#receives acknowledgment
if str(d)!="n":
	f=open(data,'w')	#opens same file in write mode
	data=s.recv(1024)	#
	while data:
		f.write(data)
		data=s.recv(1024)
	f.close()
	print "file recieved"
else:
	print "no such file in server"