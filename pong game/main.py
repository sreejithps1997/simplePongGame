from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

screen.listen()
screen.onkey(r_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"w")
screen.onkey(l_paddle.go_up,"Up")
screen.onkey(l_paddle.go_down,"Down")

Player_1 = 0
Player_2 = 0
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    #Detect collision with the paddle
    if ball.distance(r_paddle)<50 and ball.xcor() > 340 or ball.distance(l_paddle)<50 and ball.xcor() < -340:
        ball.x_bounce()

    #r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
