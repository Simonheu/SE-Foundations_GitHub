### adapted from https://github.com/realpython/materials/tree/master/python-sockets-tutorial
## more resources in server.py

import socket

HOST = "172.20.10.9"  # The server's hostname or IP address
port_number = 65432  # The port used by the server




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as aSocket:
   aSocket.connect((HOST, port_number)) # connect the socket to a host and port
   while True:
       msg = input("Enter a message: ")
       aSocket.sendall(msg.encode()) # send your message with utf-8 encoding
       data = aSocket.recv(1024) # wait for a response
       print("server: ", data.decode()) #print response