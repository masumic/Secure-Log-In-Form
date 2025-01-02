import sqlite3
import threading
import socket

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()


try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET --> types of address your program can work with
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# connect to the server on local machine
server_binding = ("localhost", 9998)
cs.connect(server_binding)

# recieve data from server: Welcome to Blueprint  
data_from_server=cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)    
cs.send(input("Response here: ").encode())

data_from_server=cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)    
cs.send(input("Response here: ").encode())

# IN GROUPS
"""
# receive data from server: How are you
data_from_server=cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)    
cs.send(input("Response here: ").encode())

count = 0
while(count < 5): # use loop to send 1, 2, 3, 4, 5 to client
    response = cs.recv(1024).decode()
    print("[C]: Data received from server: " + response)
    response = "Acknowledging " + str(count)
    cs.send(response.encode())
    count+=1

    print("Done")
"""
# close the client sockets
cs.close()
exit()