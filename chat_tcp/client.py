import socket
import thread
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1234
hostname='127.0.0.1'
def listening(server):
	data=''
	while True and data!='bye':
		#print "i reached listening"
		data=server.recv(1024).decode()
		print data
	quit()
s.connect((hostname,port))
name=raw_input('name:')
s.send(name.encode())
data=s.recv(1024).decode()
print "server:"+data
thread.	start_new_thread(listening,(s,))
while True:
	data=raw_input()
	s.send(data.encode())
s.close()
quit()