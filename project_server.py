import sqlite3
import threading # two things happening at once
import sqlite3
import hashlib
import socket # used to establish the connection between client and server


try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, connection oriented protocol (TCP)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ("localhost", 9998)
ss.bind(server_binding)
ss.listen()


def start_connection(c): # taking client as parameter
    msg = "Please enter your username: "
    c.send(msg.encode())

    response = c.recv(1024).decode() # 1024 bytes tells us the size / buffer of the content we are recieving so that the socket knows how much to expect
    print("[S]: Data received from client: " + response)
    # Connect to the SQLite database
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM username WHERE username = ?", (response,))
    #cursor.execute('select (?) from db', 'username') #% response
    enteredName = cursor.fetchone() # returns a booolean not a string
    if enteredName:
        print("Correct")
    else:
        print("Incorrect")

    msg2 = "Please enter your password: "
    c.send(msg2.encode())
    response = c.recv(1024).decode()
    print("[S]: Data received from client: " + response)
    cursor.execute("SELECT * FROM username WHERE password = ?", (response,))
    enteredPassword = cursor.fetchone()
    if enteredPassword:
        print("Correct")
    else:
        print("Incorrect")


"""
# DO IN GROUPS INDEPENDENTLY
    
    # make own riddle / joke & respond with answer

    msg = "Enter your password: "
    c.send(msg.encode())

    response = c.recv(1024).decode()
    print("[S]: Data received from client: " + response)    

    # use loop to send 1, 2, 3, 4, 5 to client --> you can only send strings 

    count = 0
    while(count < 5): # use loop to send 1, 2, 3, 4, 5 to client --> you can only send strings 
        c.send(str(count).encode())
        response = c.recv(1024).decode()
        print("[S]: Data received from client: " + response)
        count+=1

    print("Done")
"""

while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()

    # Close the server socket
    ss.close()
    exit()


# -----------------------------------------------------------
'''
cursor.execute('select %s from db') % response
enteredName = cursor.fetchone()
if enteredName == response:
        cursor.execute('select %s from db') % password
        enteredPass = cursor.fetchone()
        if enteredPass == password:
            msg = "Login Successful"
            c.send(msg.encode())

        else:
            msg = "Password is incorrect"
            c.send(msg.encode())


    else:
        msg = "Username doesn't exist"
        c.send(msg.encode())



'''