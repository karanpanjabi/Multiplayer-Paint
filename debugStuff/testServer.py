import socket

serv = socket.socket()
hostIP = '127.0.0.1'
port = 5192
serv.bind((hostIP,port))
serv.listen(5)

client, addr = serv.accept()
print("connected")

l = client.recv(1024)
print(l)

client.close()
serv.close()
