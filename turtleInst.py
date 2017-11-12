import turtle
class TurtleInstance(turtle.Turtle):
    def __init__(self, name="", color="black"):
        turtle.Turtle.__init__(self)
        self.setName(name)
        self.setColor(color)
        self.speed(0)
        pass
    def setName(self,name):
        self.name = name
    def setColor(self,color):
        self.color = color
