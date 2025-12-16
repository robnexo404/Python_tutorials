#What is a socket?
# A socket 1 of 2 of the endpoint of a communication channels
# These sockets arent limited to a network. They can be used anywhere in the world
import socket
# We need to answer 4 questions:
#1.Are we using an internet or unix socket?
#2.Are we using TCP or UDP?   (TCP is secure and connection-oriented but slow, UDP is unsecure and connectionless but fast)
#3.Which ip are we using or hosting from?
#4.Which port are we using?

#lets create a socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # we are using internet and using TCP 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#SOCK_DGR = UDP
s.bind(('127.0.0.1', 55555))  #the host and what port we want our socket to run on
s.listen() #listening mode socket

while True:
    client, address = s.accept()
    print(f"Connected to {address}")
    client.send("You are connected!".encode()) #you have to encode in TCP
    client.close()

#Now, lets create a new python file for the client