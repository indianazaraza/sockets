import socket

#instance the module
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind to port from localhost
my_socket.bind(('localhost', 8000))
#listen five request
my_socket.listen(5)

while 1:
	#accept request from client
	connection, address = my_socket.accept()

	print(address)
	
	#receive message from client
	request = connection.recv(1024).decode()
	print(request)
	
	#send message to client
	connection.send("servidor")
	
	connection.close()
