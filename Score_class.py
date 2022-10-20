from turtle import Turtle
FONT_1 = ("Courier", 18, "normal")
FONT_2 = ("Courier", 16, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.setposition(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT_1)

    def write_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER, You've Just Killed The Turtle", align="center", font=FONT_2)
