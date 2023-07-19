# sockets and network prog
# socket : two end points in one communication in order to exchange data
# internet socket (there's also unix socket but am not working on unix now)
# this is the server part
import socket

# create a socket
# works with tcp as an internet socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# address and port
s.bind(('127.0.0.1', 55555))
# to have a server : puts socket on listening mode
s.listen()

while True:
    # a client tries to connect to the server / socket, we get the client and the address in return
    client, address = s.accept()
    print(f"connected to {address}")
    client.send("You are connected!".encode())
    client.close()
