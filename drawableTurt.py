import turtle

class DrawableTurtle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.isDrawing = False
        self.penup()
        self.speed(0)

        canvas = turtle.getcanvas()
        canvas.bind('<Button-1>',self.onDraw)
        canvas.bind('<Button1-ButtonRelease>',self.onStopDrawing)
        canvas.bind('<Motion>',self.move)
        turtle.listen()

    def onDraw(self,event):
        self.isDrawing = True
        self.pendown()

    def onStopDrawing(self,event):
        self.isDrawing = False
        self.penup()

    def move(self,event):
        x,y = event.x, event.y
        x = ( x-turtle.window_width()/2 )
        y = -( y-turtle.window_height()/2 )
        # print(x,y)
        self.goto(x,y)
