from turtle import Screen, Turtle

screen =Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

score_a = 0
score_b = 0
screen.tracer(0)
paddle= Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

left_paddle =Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350,0)
# scoreboard
pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0 Player B:0", align= "center", font= ("Courier", 24, "normal"))
def go_up():
    y =paddle.ycor() 
    if y is not None:
        paddle.sety(y + 20)

def go_down():
      y =paddle.ycor() 
      if y is not None:
        paddle.sety(y - 20)

def left_up():
    y = left_paddle.ycor()
    if y is not None:
        left_paddle.sety(y + 20)

def left_down():
    y = left_paddle.ycor()
    if y is not None:
        left_paddle.sety(y - 20)


screen.listen()
screen.onkeypress(go_up, "p")
screen.onkeypress(go_down, "l")

screen.onkeypress(left_up,"w")
screen.onkeypress(left_down, "s")

import time
ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
print("Ball position:",ball.xcor(), ball.ycor())

ball.dx = 1
ball.dy = 1

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*= -1

    # Right paddle bounce
    if ball.xcor() > 320 and ball.xcor() < 350 and ball.distance(paddle) < 50:
        print("Hit paddle")
        ball.setx(320)
        ball.dx *= -1
        

    # Left paddle bounce
    if ball.xcor() < -330 and ball.xcor() > -350 and ball.distance(left_paddle) < 50:
        print("Hit left paddle")
        ball.setx(-330)
        ball.dx = abs(ball.dx)

    # Missed right paddle
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}, Player B: {score_b}", align="Center", font=("Courier", 24,"normal"))

    # Missed left paddle
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = abs(ball.dx)
        ball.dy = 0.5
        score_b += 1
        pen.clear()
        pen.write(f"player A; {score_a}, Player B: {score_b}", align = "Center", font = ("Courier", 24, "normal"))                                                            
screen.exitonclick()
