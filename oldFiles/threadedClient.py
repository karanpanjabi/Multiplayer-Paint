import socket
import _thread as thread
import time
from networkStuff import client

serv = socket.socket()
hostIP = "127.0.0.1"
port = 5192

serv.connect((hostIP,port))
playerX = client(serv)

receivedData = None
coordData = []

def updateReceivedData(*args):
    global receivedData
    while True:
        receivedData = serv.recv(1024)
        # print(receivedData)
        if not receivedData:
            break
        time.sleep(0.5)
thread.start_new_thread(updateReceivedData, tuple())

def sendData(*args):
    global coordData
    while True:
        if len(coordData)>0:
            coordData = bytes(str(coordData),'UTF-8')
            serv.send(coordData)
            coordData = []
        time.sleep(0.5)

thread.start_new_thread(sendData, tuple())

if __name__ == '__main__':
    while True:
        s = input()
        coordData = bytes(s,'UTF-8')
