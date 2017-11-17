import threadedServer
import turtle
from drawableTurt import DrawableTurtle
import _thread as thread
import time

turt = DrawableTurtle()

#send our turtle's data
#by updating threadedServer.coordData
def updateCoordData(event):
    if(turt.isDrawing):
        s = str(turt.pos())
        threadedServer.coordData.append(s)
        # print(len(threadedServer.coordData),"Updated coordData to",threadedServer.coordData)
turtle.getcanvas().bind('<Motion>',updateCoordData, add="+")

#receive and update other turtle's data
#threadedServer.playerX.turtle
def updatePlayerX(*args):
    while True:
        if(threadedServer.receivedData):
            coordList = eval(threadedServer.receivedData.decode())
            for v in coordList:
                x,y = eval(v)
                threadedServer.playerX.turtle.goto(x,y)
            threadedServer.receivedData = None
        time.sleep(0.3)
thread.start_new_thread(updatePlayerX, tuple())

turtle.mainloop()
