# this is the client part
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server
s.connect(('127.0.0.1', 55555))
# recieve the message
message = s.recv(1024)  # specifiy the number of bytes you want to recieve
s.close()

print(message.decode())
