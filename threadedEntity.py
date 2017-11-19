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

# This will store a reference to the player on the other side
playerX = None

# The receivedData is a list having data received from the other end.
# The data is not just the coordinates of the other turtle
# but also the information of whether the other player is actually drawing
# or just moving the mouse.
# The receivedData looks something like this [ "['(x,y)', '(x,y)', 'Down', '(x,y)', '(x,y)', '(x,y)', ..., 'Up']", "[ same instructions ]", ... ]
# Note that receivedData list contains multiple strings. This is because we want to be sure that every command that is being sent
# from the other side is executed and we don't get jagged curves instead of proper curves.
# So to sum it up receivedData is a list of strings. Every string contains a list with instructions.
receivedData = []

# The coordData that we're gonna send is again not just coordinate data of our turtle
# but also the penup and pendown events.
# The coordData looks something like this [ '(x,y)', '(x,y)','Down', '(x,y)', '(x,y)', '(x,y)', ..., 'Up' ]
# Each element in above list has been taken as a string because this helps us to use the eval function directly
# after checking for 'Up' and 'Down' events
# Note the difference between receivedData list and the coordData list.\
# The coordData list is just like one string element from the receivedData list.
coordData = []


#listen for connections if I'm the server
#else just connect to the server
#assign the received socket to playerX
def Connect():
    global playerX
    if(SERVER):
        sock.bind((hostIP,port))
        sock.listen(5)
        playerX, addr = sock.accept()
        playerX = Entity(playerX)
    else:
        sock.connect((hostIP,port))
        # sock.send(bytes("Connectino",'UTF-8'))
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
