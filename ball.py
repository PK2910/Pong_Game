from turtle import Turtle
class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.shape("circle")
        self.x_cor=10
        self.y_cor=10
        self.drive=0.1
    def move(self):
        new_x=self.xcor()+self.x_cor
        new_y=self.ycor()+self.y_cor
        self.penup()
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_cor*=-1
    def bounce_x(self):
        self.x_cor*=-1
    def centre(self):
        self.goto(x=0,y=0)
