from turtle import Screen
from time import sleep
from Player_class import Player
from Turtle_class import TurtleManager
from Score_class import ScoreBoard
from Draw_Lines import Painter

# prepare screen
screen = Screen()
screen.addshape("racer.gif")
screen.bgcolor("khaki")
screen.setup(width=600, height=600)
screen.tracer(0)

# create player
player = Player()
ninja = TurtleManager()
board = ScoreBoard()
painter = Painter()
painter.draw_finish()
painter.draw_start()

try_again = True
while try_again:

    screen.listen()
    screen.onkey(player.move_north, "w")
    screen.onkey(player.move_south, "s")

    play = True
    while play:
        sleep(0.1)
        screen.update()
        # define when to generate new cars:
        ninja.counter += 1
        if ninja.counter % 10 == 0:
            ninja.create_car()
        ninja.move_forward()
        # check about collision
        for machine in ninja.ninja_list:
            if player.distance(machine) < 25:
                board.write_over()
                play = False
        # check about crossing finish line
        if player.ycor() > 270:
            board.level += 1
            board.write_level()
            player.return_back()
            ninja.local_speed += 5

    will = screen.textinput(title="end/continue", prompt="Do You Want to Try Again? Yes/No ").lower()
    if will == "no":
        try_again = False
    else:
        board.clear()
        board.level = 1
        board.write_level()
        ninja.local_speed = 5
        player.return_back()

screen.exitonclick()
