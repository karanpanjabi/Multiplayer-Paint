import threadedClient
import turtle
from drawableTurt import DrawableTurtle
import _thread as thread
import time

turt = DrawableTurtle()

#append our turtle's data
#threadedClient.coordData
def updateCoordData(event):
    s = str(turt.pos())
    threadedClient.coordData.append(s)
turtle.getcanvas().bind('<Motion>',updateCoordData, add="+")

#append penup and pendown events
def appendPenUp(event):
    threadedClient.coordData.append("Up")
def appendPenDown(event):
    threadedClient.coordData.append("Down")
turtle.getcanvas().bind('<Button-1>', appendPenDown, add="+")
turtle.getcanvas().bind('<Button1-ButtonRelease>', appendPenUp, add="+")

#receive and update other turtle's data
#threadedClient.playerX.turtle
def updatePlayerX(*args):
    while True:
        if(threadedClient.receivedData):

            coordList = eval(threadedClient.receivedData.decode())
            for val in coordList:
                if(val == "Up"):
                    threadedClient.playerX.turtle.penup()
                elif(val == "Down"):
                    threadedClient.playerX.turtle.pendown()
                else:
                    x,y = eval(val)
                    threadedClient.playerX.turtle.goto(x,y)
            threadedClient.receivedData = None

        time.sleep(0.3)
thread.start_new_thread(updatePlayerX, tuple())

turtle.mainloop()
