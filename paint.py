import turtle
import time

import socket

serv = socket.socket()
hostIP = "127.0.0.1"
port = 5192

serv.connect((hostIP,port))

turtle.showturtle()
turtle.penup()
turtle.speed(0)

isDrawing = False

def move(event):
    x,y = event.x, event.y
    x = ( x-turtle.window_width()/2 )
    y = -( y-turtle.window_height()/2 )
    # print(x,y)
    turtle.goto(x,y)


    if(isDrawing==True):
        serv.send(bytes(str((x,y)),'UTF-8'))

def onDraw(event):
    # print("drawing")
    global isDrawing
    isDrawing = True
    turtle.pendown()

def onStopDrawing(event):
    # print("stopped")
    global isDrawing
    isDrawing = False
    turtle.penup()

canvas = turtle.getcanvas()
canvas.bind('<Button-1>',onDraw)
canvas.bind('<Button1-ButtonRelease>',onStopDrawing)
canvas.bind('<Motion>',move)


turtle.listen()
turtle.mainloop()
