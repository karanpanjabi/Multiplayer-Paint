import socket

serv = socket.socket()
hostIP = "127.0.0.1"
port = 5192

serv.connect((hostIP,port))

while True:
    s = input()
    serv.send(bytes(s,'UTF-8'))
    break
