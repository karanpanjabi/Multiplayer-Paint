import turtle

turtle.listen()
def onclick(event):
    print("clicked")

turtle.getcanvas().bind('<Button-1>',onclick)

turtle.mainloop()
