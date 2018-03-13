import socket
#creating socket AF_INET stands for ipv4 and other one is standing for tcp connection
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#defiingng port
port=1234
#binding server with the port
s.bind(('',port))
#makes upto 2 connectiions wait
s.listen(2)
#accepting connection from client
conn,addr=s.accept()
print "got connection :",addr
while True:
	#receing data from the client
	data=conn.recv(1024).decode()
	#print type(data)
	if not data:
		break;
	print "client :"+str(data)
	data=raw_input('->')
	#sending data to the client
	conn.send(data.encode())
conn.close()
