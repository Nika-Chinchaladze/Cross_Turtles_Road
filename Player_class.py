from turtle import Turtle
STARTING_POSITION = (0, -250)
NORMAL_SPEED = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("racer.gif")
        self.penup()
        self.color("maroon")
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def move_north(self):
        self.forward(NORMAL_SPEED)

    def move_south(self):
        self.backward(NORMAL_SPEED)

    def return_back(self):
        self.setposition(STARTING_POSITION)
        self.setheading(90)
