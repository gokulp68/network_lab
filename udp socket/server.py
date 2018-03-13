import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=1234
hostip=socket.gethostname()
s.bind((hostip,port))
data=''
while True and data != "bye":
	data,addr=s.recvfrom(1024)
	print "client :"+str(data)
	data=raw_input('->')
	s.sendto(data,addr)