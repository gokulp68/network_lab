import socket
import os.path
from thread import *
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1234
s.bind(('',port))
s.listen(2)
def clientthread(conn, s):
	data=conn.recv(1024)			#receives file name
	if os.path.isfile(str(data)):	#cjecks avaialability of file
		d="s"
		conn.send(d)				#sends to client that file is availabale
		f=open(str(data),'r')		#opening file in read mode
		data=f.read(1024)
		while data:
			conn.send(data)			#sends read dtaa
			data=f.read(1024)
		print "file send !"			#shows full file read
		f.close()					#closes file
	else:
		print "no such file exist"	#only when file not exist
		d="n"
		conn.send(d)
	conn.close()
	s.close()
while True:
	print "server is ready"
	#receives connection from clients
	conn, addr=s.accept()
	start_new_thread(clientthread,(conn,s))				#starting new thread
