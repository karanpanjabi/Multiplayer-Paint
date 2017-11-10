"""
listenForConnections() callback ->
co
"""

import socket
from turtleInst import TurtleInstance

class client():
    def __init__(self, sock):
        self.sock = sock
        self.turtle = TurtleInstance()
        pass
