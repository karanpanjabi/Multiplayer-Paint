import socket
from turtleInst import TurtleInstance

class Entity():
    def __init__(self, sock):
        self.sock = sock
        self.turtle = TurtleInstance()
        pass

if __name__=='__main__':
    ob = Entity("abc")
    ob.turtle.forward(50)
    while True:
        pass
