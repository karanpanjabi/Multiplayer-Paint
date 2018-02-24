Multiplayer LAN Paint is small fun project that's made to show the graphical and the networking capabilities of the python programming language. In this project, one user starts the main file (mainPaint.py) and assumes himself as the server while the other user also starts the main file (mainPaint.py) and assumes himself as the client that's going to connect to the server. The client and the server exchange the data to and fro such as the turtle’s position and respective mouse clicks. In order for the project to work on LAN, both the players have to be connected to the same network and the player who’ll assume the role of the server has to put his local IP in threadedEntity.py.



On starting the mainPaint.py file, a turtle canvas is created and a DrawableTurtle is placed on it by instantiating an object of the DrawableTurtle class. DrawableTurtle is a class that represents a turtle which can be used to draw via a mouse. Then the network code is initiated that prompts the player to indicate whether he is the server or the client. If he answers yes, the socket is bound to the local IP specified and the server starts listening for connections. If he answers no, the socket tries to connected to the specified IP on which the server is running. Once the connection is made, the socket object is encapsulated in another class Entity which also instantiates an object of TurtleInstance class. This TurtleInstance class represents “the turtle of the player on the other side” on our turtle’s screen. Once all the network is set up, the data is updated, sent, and received via separate threads so that our main turtle window isn’t blocked.


The project is based on many concepts and tools such as object oriented programming, sockets, threads and the turtle graphics library.


For now, for a player the color of own pen is black and the pen color of the other is red to keep the code as simple as possible.
