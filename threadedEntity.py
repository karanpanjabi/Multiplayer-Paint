import socket
from networkEntity import Entity
import _thread as thread
from time import sleep

SERVER = False
s = input("Are you the server?\n")
if(s=="y" or s=="yes"):
    SERVER = True

hostIP = '127.0.0.1'
port = 5192
sock = socket.socket()

playerX = None
receivedData = []
coordData = []

#If I am the server, bind to an IP
if(SERVER):
    sock.bind((hostIP,port))
    sock.listen(5)

#listen for connections if I'm the server
#else just connect to the server
#assign the received socket to playerX
def Connect():
    global playerX
    if(SERVER):
        playerX, addr = sock.accept()
        playerX = Entity(playerX)
    else:
        sock.connect((hostIP,port))
        playerX = Entity(sock)
    print("Connected!")

#start a thread to connect to the other side and
#not make the importing module wait
thread.start_new_thread(Connect, tuple())

# The coordData list will be populated every 0.5s by the importing
# module and this sendData function shall cast the list
# to a string and send it through playerX socket
def sendData():
    pass

# Start a thread to call sendData so that
# the importing module doesn't wait
thread.start_new_thread(sendData, tuple())

# The receivedData list is appended every 0.5s with the data
# received from the other end
def receiveData():
    pass

# Start a thread to call receiveData so that
# the importing module doesn't wait
thread.start_new_thread(receiveData, tuple())
