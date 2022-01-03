import socket

#instance the module
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect(("localhost", 8000))

#send message to server
my_socket.send("cliente")

#receive message from server
response = my_socket.recv(1024).decode()
print(response)

#close connection
my_socket.close()
