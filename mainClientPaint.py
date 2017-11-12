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
        threadedClient.coordData = bytes(s,'UTF-8')
turtle.getcanvas().bind('<Motion>',updateCoordData, add="+")

#receive and update other turtle's data
#threadedClient.playerX.turtle
def updatePlayerX(*args):
    while True:
        if(threadedClient.receivedData):
            x,y = eval(threadedClient.receivedData.decode('UTF-8'))
            threadedClient.playerX.turtle.goto(x,y)
            threadedClient.receivedData = None
        time.sleep(0.1)
thread.start_new_thread(updatePlayerX, tuple())

turtle.mainloop()
