from turtle import RawTurtle, TurtleScreen
class DrawableTurtle(RawTurtle):
    def __init__(self, cv):
        ts = TurtleScreen(cv)
        RawTurtle.__init__(self, ts)
        # self.turtleRef = turt
        self.ts = ts
        ts.listen()

        self.isDrawing = False
        self.penup()
        self.speed(0)
        canvas = cv
        canvas.bind('<Button-1>',self.onDraw)
        canvas.bind('<Button1-ButtonRelease>',self.onStopDrawing)
        canvas.bind('<Motion>',self.move)
        # turtle.listen()

        # print(turt.window_width(), turt.window_height())

    def onDraw(self,event):
        self.isDrawing = True
        self.pendown()

    def onStopDrawing(self,event):
        self.isDrawing = False
        self.penup()

    def move(self,event):
        x,y = event.x, event.y
        # x = ( x-self.turtleRef.window_width()/2 )
        # y = -( y-self.turtleRef.window_height()/2 )

        x = ( x-self.ts.window_width()/2 )
        y = -( y-self.ts.window_height()/2 )

        # print(x,y)
        self.goto(x,y)

    def getLastPos(self):
        return self.pos()

if __name__ == '__main__':
    import turtle
    t = DrawableTurtle(turtle.getcanvas())
    turtle.mainloop()
