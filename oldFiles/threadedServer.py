import _thread as thread
import socket
from networkStuff import client
import time

serv = socket.socket()
hostIP = '127.0.0.1'
port = 5192
serv.bind((hostIP,port))
serv.listen(5)

playerX = None
receivedData = None
coordData = []

def listenForConnection(*args):
    global playerX
    playerX, addr = serv.accept()
    playerX = client(playerX)
    print("connected")

thread.start_new_thread(listenForConnection, tuple())

def updateReceivedData(*args):
    global receivedData
    while True :
        if(playerX is not None and type(playerX)==client):
            receivedData = playerX.sock.recv(1024)
            if not receivedData:
                break
            # print(receivedData)
        time.sleep(0.5)
thread.start_new_thread(updateReceivedData, tuple())

def sendData(*args):
    global coordData
    while True:
        if len(coordData)>0 and playerX is not None:
            coordData = bytes(str(coordData),'UTF-8')
            playerX.sock.send(coordData)
            coordData = []
        time.sleep(0.5)
thread.start_new_thread(sendData, tuple())

if __name__ == '__main__':
    while True:
        pass
