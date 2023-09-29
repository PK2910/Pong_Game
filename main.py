from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen=Screen()
screen.title("PONG")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
l1=Paddle(point=(-350,0))
r1=Paddle(point=(350,0))
b=Ball()
s=Scoreboard()
screen.onkey(fun=r1.up, key='Up')
screen.onkey(fun=r1.down, key='Down')
screen.onkey(fun=l1.up, key='w')
screen.onkey(fun=l1.down, key='s')
screen.listen()
game=True
while game:
    time.sleep(b.drive)
    screen.update()
    b.move()
    #detecting collision of the ball and the wall
    if b.ycor()>280 or b.ycor()<-280:
        #ball should bounce
        b.bounce_y()
    #detecting collision of the ball and the paddle
    if b.distance(r1)<50 and b.xcor()>320 or b.distance(l1)<50 and b.xcor()<-320:
        b.bounce_x()
        b.drive*=0.9
    #ball gliding past the  right paddle
    if b.xcor()>380:
        b.centre()
        b.drive=0.1
        b.bounce_x()
        s.l_point()
    if b.xcor()<-380:
        b.centre()
        b.bounce_x()
        s.r_point()
screen.exitonclick()