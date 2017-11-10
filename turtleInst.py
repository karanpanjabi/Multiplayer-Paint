import turtle
class TurtleInstance(turtle.Turtle):
    def __init__(self, name="", color="black"):
        turtle.Turtle.__init__(self)
        self.setName(name)
        self.setColor(color)
        pass
    def setName(self,name):
        self.name = name
    def setColor(self,color):
        self.color = color
