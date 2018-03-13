import socket
import datetime
from thread import *
import time
port=1234
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))
def sendtime(sock, addr):
	print "u reached send time"
	time.sleep(8)
	tim=datetime.datetime.now()
	sock.sendto(str(tim),addr)

	return
while True:
	print "Server is ready \n"
	message,addr=s.recvfrom(1024)
	start_new_thread(sendtime,(s,addr))