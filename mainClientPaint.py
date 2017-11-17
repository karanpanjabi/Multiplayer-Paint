import threadedClient
import turtle
from drawableTurt import DrawableTurtle
import _thread as thread
import time

turt = DrawableTurtle()

#send our turtle's data
#threadedClient.coordData
def updateCoordData(event):
    if(turt.isDrawing):
        s = str(turt.pos())
        threadedClient.coordData.append(s)
turtle.getcanvas().bind('<Motion>',updateCoordData, add="+")

#receive and update other turtle's data
#threadedClient.playerX.turtle
def updatePlayerX(*args):
    while True:
        if(threadedClient.receivedData):
            coordList = eval(threadedClient.receivedData.decode())
            for v in coordList:
                x,y = eval(v)
                threadedClient.playerX.turtle.goto(x,y)
            threadedClient.receivedData = None
        time.sleep(0.3)
thread.start_new_thread(updatePlayerX, tuple())

turtle.mainloop()
