from turtle import RawTurtle, TurtleScreen
class DrawableTurtle(RawTurtle):
    def __init__(self, turt):
        # ts = TurtleScreen(cv)
        RawTurtle.__init__(self, turt.getscreen())
        self.isDrawing = False
        self.penup()
        self.speed(0)
        self.turtleRef = turt
        canvas = turt.getcanvas()
        canvas.bind('<Button-1>',self.onDraw)
        canvas.bind('<Button1-ButtonRelease>',self.onStopDrawing)
        canvas.bind('<Motion>',self.move)
        # turtle.listen()

        print(turt.window_width(), turt.window_height())

    def onDraw(self,event):
        self.isDrawing = True
        self.pendown()

    def onStopDrawing(self,event):
        self.isDrawing = False
        self.penup()

    def move(self,event):
        x,y = event.x, event.y
        x = ( x-self.turtleRef.window_width()/2 )
        y = -( y-self.turtleRef.window_height()/2 )
        # print(x,y)
        self.goto(x,y)
