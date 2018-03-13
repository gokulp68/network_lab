import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=1234
hostip=socket.gethostname()
data=''
while True and data != "bye":
	data=raw_input('->')
	s.sendto(data,(hostip,port))
	data,addr=s.recvfrom(1024)
	print "server : "+str(data)