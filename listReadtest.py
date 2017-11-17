import turtle

turtle.showturtle()
turtle.penup()
f = open("coordDebug.txt","r")

for line in f:
    line = line.rstrip()
    l = eval(line)
    for val in l:
        if(val=="Up"):
            turtle.penup()
        elif(val=="Down"):
            turtle.pendown()
        else:
            x,y = eval(val)
            turtle.goto(x,y)
f.close()

turtle.mainloop()
