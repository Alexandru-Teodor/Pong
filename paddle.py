from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setposition(position)
        self.setheading(90)

    def go_up(self):
        if self.ycor() < 250:
            self.forward(50)

    def go_down(self):
        if self.ycor() > -250:
            self.backward(50)
