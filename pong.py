import turtle

win = turtle.Screen()
win.title("my paint")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# racket
racket_left = turtle.Turtle()
racket_left.speed(0)
racket_left.shape("square")
racket_left.color("blue")
racket_left.shapesize(stretch_len=1,stretch_wid=5)
racket_left.penup()
racket_left.goto(-350,0)

racket_right = turtle.Turtle()
racket_right.speed(0)
racket_right.shape("square")
racket_right.color("yellow")
racket_right.shapesize(stretch_len=1,stretch_wid=5)
racket_right.penup()
racket_right.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 | Player B: 0",align="center",font=("Verdana", 22,"normal"))
score_a = 0
score_b = 0
# Func
def racket_left_up():
    y = racket_left.ycor()#ycor возвр коорд y
    y += 20
    racket_left.sety(y)#зафиксировали
# Func
def racket_left_down():
    y = racket_left.ycor()#ycor возвр коорд y
    y -= 20
    racket_left.sety(y)#зафиксировали
# Func
def racket_right_up():
    y = racket_right.ycor()#ycor возвр коорд y
    y += 20
    racket_right.sety(y)#зафиксировали
# Func
def racket_right_down():
    y = racket_right.ycor()#ycor возвр коорд y
    y -= 20
    racket_right.sety(y)#зафиксировали
          
# keyboard
win.listen()
win.onkeypress(racket_left_up,"w")
win.onkeypress(racket_left_down,"s")
win.onkeypress(racket_right_up,"Up")
win.onkeypress(racket_right_down,"Down")

while True:
    win.update()
    #Движение мяча
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1 
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1 
        pen.write()
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1  
    
    if ball.xcor() > 340 and ball.ycor() < racket_right.ycor() + 50 and ball.ycor() > racket_right.ycor() -50:
        ball.dx *=-1
    if ball.xcor() > -340 and ball.ycor() < racket_left.ycor() + 50 and ball.ycor() > racket_left.ycor() -50:
       ball.dx *=-1