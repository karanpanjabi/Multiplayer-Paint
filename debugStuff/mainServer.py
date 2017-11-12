import socket
from networkStuff import client
import turtle
from drawableTurt import DrawableTurtle

turt = DrawableTurtle()

serv = socket.socket()
hostIP = "127.0.0.1"
port = 5192
serv.bind((hostIP,port))

#listenForConnections
#TODO: make this threaded
serv.listen(5)
playerX, addr = serv.accept()
print("client connected")
#TODO: assign a color and a name
playerX = client(playerX)
playerX.turtle.showturtle()


while True:
    data = playerX.sock.recv(1024)
    print(data)

    #when client disconnects lets break out of the loop
    if not data:
        break

#turtlepart
turtle.mainloop()
