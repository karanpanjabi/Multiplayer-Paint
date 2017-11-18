import socket

serv = socket.socket()
hostIP = "127.0.0.1"
port = 5192

serv.connect((hostIP,port))
l = [4,5,6]
while True:
    s = input()
    serv.send(bytes(s,'UTF-8'))
    # serv.send(bytes(l))
    if(s=='q'):
        break
