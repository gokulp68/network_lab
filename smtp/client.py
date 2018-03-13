import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1234
s.connect(('127.0.0.1',port))
message=raw_input('username:password')
s.send(message)
data=s.recv(1024)
print data
if str(data)!="0":
	print "login success"
	to=raw_input("To:\n")
	content=raw_input('body:')
	s.send(to)
	s.send(mail)
else:
	print "errror"
s.close()