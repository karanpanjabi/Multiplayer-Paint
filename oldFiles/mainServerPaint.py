import threadedServer
import turtle
from drawableTurt import DrawableTurtle
import _thread as thread
import time

turt = DrawableTurtle()

#append our turtle's data
#by updating threadedServer.coordData
def updateCoordData(event):
    s = str(turt.pos())
    threadedServer.coordData.append(s)
    # print(len(threadedServer.coordData),"Updated coordData to",threadedServer.coordData)
turtle.getcanvas().bind('<Motion>',updateCoordData, add="+")

#append penup and pendown events
def appendPenUp(event):
    threadedServer.coordData.append("Up")
def appendPenDown(event):
    threadedServer.coordData.append("Down")
turtle.getcanvas().bind('<Button-1>', appendPenDown, add="+")
turtle.getcanvas().bind('<Button1-ButtonRelease>', appendPenUp, add="+")

#receive and update other turtle's data
#threadedServer.playerX.turtle
def updatePlayerX(*args):
    while True:
        if(threadedServer.receivedData):

            coordList = eval(threadedServer.receivedData.decode())
            for val in coordList:
                if(val == "Up"):
                    threadedServer.playerX.turtle.penup()
                elif(val == "Down"):
                    threadedServer.playerX.turtle.pendown()
                else:
                    x,y = eval(val)
                    threadedServer.playerX.turtle.goto(x,y)
            threadedServer.receivedData = None

        time.sleep(0.3)
thread.start_new_thread(updatePlayerX, tuple())

turtle.mainloop()
