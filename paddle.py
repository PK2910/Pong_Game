from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, shape="classic", undobuffersize=1000, visible=True, point=(0, 0)):
        super().__init__(shape=shape, undobuffersize=undobuffersize, visible=visible)
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(point)  # Set the initial position based on the 'point' parameter

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


