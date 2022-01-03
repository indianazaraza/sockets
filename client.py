import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect(("localhost", 8000))

my_socket.send("cliente")
response = my_socket.recv(1024).decode()
print(response)

my_socket.close()
