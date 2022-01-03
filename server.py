import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.bind(('localhost', 8000))
my_socket.listen(5)

while 1:
	connection, address = my_socket.accept()

	print(address)

	request = connection.recv(1024).decode()
	print(request)

	connection.send("servidor")
	
	connection.close()
