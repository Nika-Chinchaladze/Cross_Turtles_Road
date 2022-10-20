from turtle import Turtle
from random import choice, randint
COLORS = ["brown", "dark green", "navy", "purple", "crimson", "dark olive green", "dim gray"]
STARTING_MOVE_DISTANCE = 5


class TurtleManager:
    def __init__(self):
        self.ninja_list = []
        self.counter = 1
        self.local_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        ninja = Turtle()
        ninja.shape("turtle")
        ninja.penup()
        ninja.color(choice(COLORS))
        ninja.setposition(300, randint(-180, 220))
        ninja.setheading(180)
        self.ninja_list.append(ninja)

    def move_forward(self):
        for item in self.ninja_list:
            item.forward(self.local_speed)
