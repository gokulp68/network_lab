import socket
port=1234
hostname='127.0.0.1'
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print "sending time request\n"
message="give time"
s.sendto(message,(hostname,port))
message,addr=s.recvfrom(1024)
print "time is :"+str(message)