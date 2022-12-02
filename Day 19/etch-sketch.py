from turtle import Turtle, Screen

DEFAULT_SPEED = 10


def move_up():
    tim.setheading(90)
    tim.forward(DEFAULT_SPEED)


def move_left():
    tim.setheading(180)
    tim.forward(DEFAULT_SPEED)


def move_right():
    tim.setheading(0)
    tim.forward(DEFAULT_SPEED)


def move_down():
    tim.seth(270)
    tim.forward(DEFAULT_SPEED)


def clear_screen():
    tim.clear()


tim = Turtle()
screen = Screen()


screen.listen()
tim.speed("fast")
screen.onkeypress(key="Up", fun=move_up)
screen.onkeypress(key="Left", fun=move_left)
screen.onkeypress(key="Right", fun=move_right)
screen.onkeypress(key="Down", fun=move_down)
screen.onkeypress(key="space", fun=clear_screen)
screen.exitonclick()
