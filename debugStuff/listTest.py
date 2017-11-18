import turtle, time
from drawableTurt import DrawableTurtle
import _thread as thread

turt = DrawableTurtle()

coordData = []

coordDebug = open("coordDebug.txt","w")

def updateCoordData(event):
    s = str(turt.pos())
    coordData.append(s)
    # print(len(threadedServer.coordData),"Updated coordData to",threadedServer.coordData)
turtle.getcanvas().bind('<Motion>', updateCoordData, add="+")

def appendPenUp(event):
    coordData.append("Up")
def appendPenDown(event):
    coordData.append("Down")
turtle.getcanvas().bind('<Button-1>', appendPenDown, add="+")
turtle.getcanvas().bind('<Button1-ButtonRelease>', appendPenUp, add="+")

def writeToFile():
    global coordData
    while True:
        if(len(coordData)>0):
            coordDebug.write(str(coordData)+"\n")
            coordData = []
        time.sleep(0.5)
thread.start_new_thread(writeToFile, tuple())

turtle.mainloop()
coordDebug.close()
