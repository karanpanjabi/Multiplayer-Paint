import turtle
class TurtleInstance(turtle.Turtle):
    def __init__(self, name="", color="black"):
        turtle.Turtle.__init__(self)
        self.setName(name)
        self.setColor(color)
        self.speed(0)
        self.penup()
        pass
    def setName(self,name):
        self.name = name
    def setColor(self,color):
        self.pencolor(color)

if __name__ == '__main__':
    t = TurtleInstance()
    t.forward(50)
    turtle.mainloop()
