import threadedServer
import turtle
from drawableTurt import DrawableTurtle
import _thread as thread
import time

turt = DrawableTurtle()

#send our turtle's data
def updateCoordData(event):
    s = str(turt.pos())
    coordData = bytes(s,'UTF-8')
turtle.getcanvas().bind('<Motion>',updateCoordData, add="+")

#receive and update other turtle's data
#threadedServer.playerX.turtle
def updatePlayerX(*args):
    while True:
        if(threadedServer.receivedData):
            x,y = eval(threadedServer.receivedData.decode('UTF-8'))
            threadedServer.playerX.turtle.goto(x,y)
            threadedServer.receivedData = None
        time.sleep(0.1)
thread.start_new_thread(updatePlayerX, tuple())

turtle.mainloop()
