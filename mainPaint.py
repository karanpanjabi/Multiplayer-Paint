import turtle, time
from drawableTurt import DrawableTurtle
import _thread as thread
from time import sleep


#Creating our turtle
turt = DrawableTurtle(turtle.getcanvas())

import threadedEntity

#Append our turtle's data to
#threadedEntity.coordData
def updateCoordData(event):

    #cast the coord tuple (x,y) to str
    #so that we can use eval(str) directly
    if(turt.isDrawing):
        s = str(turt.pos())
        threadedEntity.coordData.append("goto"+s)

#Bind the mouse motion to the above function
turtle.getcanvas().bind('<Motion>', updateCoordData, add = "+")

#append penup and pendown events
def appendPenUp(event):
    threadedEntity.coordData.append("penup()")
def appendPenDown(event):
    #So as to move the turtle to the last position for the player on the other side
    threadedEntity.coordData.append("goto"+str(turt.getLastPos()))
    threadedEntity.coordData.append("pendown()")
turtle.getcanvas().bind('<Button-1>', appendPenDown, add="+")
turtle.getcanvas().bind('<Button1-ButtonRelease>', appendPenUp, add="+")


otherTurtleRefStr = "threadedEntity.playerX.turtle."
#Update the other player's (playerX) position on our screen every 0.5s
def updatePlayerX():
    while True:
        #Check if we've received any data
        if(len(threadedEntity.receivedData) > 0):
            # For reference receivedData looks like
            # [ "['(x,y)', '(x,y)', 'Down', '(x,y)', '(x,y)', '(x,y)', ..., 'Up']", "[ same instructions ]", ... ]
            # So we have to first extract every string, then do eval(string) so we get a list
            # Then iterate over that list, check for 'Up' and 'Down' and finally update, playerX's turtle's position
            for l in threadedEntity.receivedData:
                l = eval(l)
                for inst in l:
                    #inst -> instruction
                    try:
                        inst = otherTurtleRefStr+inst
                        # print(inst)
                        eval(inst)

                    except Exception as e:
                        print(e)

            #Flush out the receivedData list so that its not executed again
            threadedEntity.receivedData = []

        #To reduce stress on the CPU
        sleep(0.5)

thread.start_new_thread(updatePlayerX, tuple())

turtle.mainloop()
