import socket
from turtleInst import TurtleInstance

class Entity():
    def __init__(self, sock):
        self.sock = sock
        self.turtle = TurtleInstance()
        pass
