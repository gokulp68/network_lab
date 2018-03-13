import socket
from thread import *
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1234
#made a list for clients
list_of_clients=[]
#binding to the port
s.bind(('',port))
def client_thread(conn, addr):
	#recieves name from the client
	name=conn.recv(1024).decode()
	print name+" joined chat room"
	welcome="welcome to this chat room"
	data=''
	#server sends the welcome note to the client
	conn.send(welcome.encode())
	while True and data!="bye":
		try:
			#server recieves
			data=conn.recv(1024).decode()
			if not data:
				break;
			#prints on server terminal
			message=str(name)+"->"+str(data)
			print message
			#broadcasts the message
			broadcast(conn,message)
		except:
			continue
	#server sends bye to the client
	conn.send(data.encode())
	conn.close()
	list_of_clients.remove(conn)
def broadcast(conn,data):
	#iterates through all connections in list of clients
	#skips the connection which sended the message
	for connection in list_of_clients:
		if connection!=conn:
			#print "i reached broadcast"
			try:
				connection.send(data.encode())
			except:
				#if connection fails closes connection and removes collection from list
				connection.close()
				list_of_clients.remove(connection)
		else:
			continue
#main starts here
s.listen(10)
while True:
	#server accepts a connection
	conn,addr=s.accept()
	#appends to the list
	list_of_clients.append(conn)
	#starting a new thread with ths connection
	start_new_thread(client_thread,(conn,addr))
s.close()