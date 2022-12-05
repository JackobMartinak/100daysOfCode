from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_x, start_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=4)
        self.penup()
        self.goto(start_x, start_y)
        self.setheading(90)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
