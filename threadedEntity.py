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
    #to modify coordData
    global coordData
    while True:
        #Check if we are connected and there is data to send
        #Empty out coordData once the data is sent
        if( playerX is not None and len(coordData)>0 ):
            data = bytes(str(coordData),'UTF-8')
            playerX.sock.send(data)
            coordData = []
        sleep(0.5)

# Start a thread to call sendData so that
# the importing module doesn't wait
thread.start_new_thread(sendData, tuple())

# The receivedData list is appended every 0.5s with the data
# received from the other end
def updateReceivedData():
    #to modify receivedData
    global receivedData
    while True:
        #Check if we're connected and the object is of type Entity
        # and then receive the data
        if(type(playerX) == Entity):
            data = playerX.sock.recv(1024)
            data = data.decode()
            #Exit out of the loop if the other side disconnects
            if(not data):
                break
            receivedData.append(data)
        sleep(0.5)

# Start a thread to call receiveData so that
# the importing module doesn't wait
thread.start_new_thread(updateReceivedData, tuple())

if __name__ == '__main__':
    while True:
        print(receivedData)
        sleep(2)
