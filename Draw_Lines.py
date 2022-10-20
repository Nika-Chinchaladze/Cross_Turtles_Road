from turtle import Turtle


class Painter(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(-275, 250)
        self.setheading(0)

    def draw_finish(self):
        self.stamp()
        for i in range(54):
            self.forward(10)
            if i % 2 == 0:
                self.color("royal blue")
            else:
                self.color("white")
            self.stamp()

    def draw_start(self):
        self.color("saddle brown")
        self.setposition(-275, -205)
        self.setheading(0)
        self.stamp()
        for j in range(54):
            self.forward(10)
            if j % 2 == 0:
                self.color("misty rose")
            else:
                self.color("saddle brown")
            self.stamp()
