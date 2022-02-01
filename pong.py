import turtle

# https://almettkidscoding.github.io/basics/turtle_programming/

score_a = 0
score_b = 0
Button_x = -100
Button_y = 0
Button_x1 = 100
Button_y1 = 0
ButtonLength = 100
ButtonWidth = 50

"""
--------
|screen|
--------
+title
+background color
+setup

"""
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("blue")
screen.setup(width=800, height=600)
screen.tracer(0)

pen1 = turtle.Turtle()
pen1.hideturtle()
pen1.pencolor('#111111')
pen1.fillcolor('white')
loop = False


def draw_rect_button(pen2, x, y, message):
    pen2.penup()
    pen2.begin_fill()
    pen2.goto(x, y)
    pen2.goto(x + ButtonLength, y)
    pen2.goto(x + ButtonLength, y + ButtonWidth)
    pen2.goto(x, y + ButtonWidth)
    pen2.goto(x, y)
    pen2.end_fill()
    pen2.goto(x + 15, y + 15)
    pen2.write(message, font=('Arial', 15, 'normal'))


def button_click(x, y):
    global score_b, score_a
    if Button_x <= x <= Button_x + ButtonLength:
        if Button_y <= y <= Button_y + ButtonWidth:
            score_a = 0
            score_b = 0
            pen1.clear()
            game()

    elif Button_x1 <= x <= Button_x1 + ButtonLength:
        if Button_y1 <= y <= Button_y1 + ButtonWidth:
            exit(0)


"""
----------
|paddle A|
----------

+speed
+shape
+color
+shape size
+pen up
+go to

"""
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

"""
----------
|paddle B|
----------

+speed
+shape
+color
+shape size
+pen up
+go to

"""
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

"""
----------
|Ball|
----------

+speed
+shape
+color
+pen up
+go to
+X move
+Y move

"""
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

"""
Pen is the object to record scores that gained by 
Paddle A and B
"""
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))

"""
-------------
|paddle_a_up|
-------------
+get Y coordinate of paddle A
+add 30 to Y coordinate
+set Y coordinate to new Y coordinate
"""


def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)


"""
-------------
|paddle_a_down|
-------------
+get Y coordinate of paddle A
+subtract 30 from Y coordinate
+set Y coordinate to new Y coordinate

"""


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)


"""
-------------
|paddle_b_up|
-------------
+get Y coordinate of paddle B
+add 30 to Y coordinate
+set Y coordinate to new Y coordinate

"""


def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)


"""
-------------
|paddle_b_down|
-------------
+get Y coordinate of paddle B
+subtract 30 from Y coordinate
+set Y coordinate to new Y coordinate

"""


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)


"""
-----------------
|keyboard binding|
-----------------
+bind key up to paddle_a_up "w"
+bind key down to paddle_a_down "s"
+bind key up to paddle_b_up "Up"
+bind key down to paddle_b_down "Down"


"""
screen.listen()
screen.onkeypress(paddle_a_up, "Up")
screen.onkeypress(paddle_a_down, "Down")
screen.onkeypress(paddle_b_up, "w")
screen.onkeypress(paddle_b_down, "s")

"""
workflow

"""
winner = 'a'


def game():
    global score_b, score_a, winner
    while True:
        screen.update()
        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # border checking
        if ball.ycor() > 280:
            ball.sety(280)
            ball.dy *= -1

        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1

        # left and right
        if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            score_a += 1
            pen.clear()
            pen.write("player a: {} player b: {}".format(score_a, score_b), align="center",
                      font=("courier", 20, "normal"))
        if ball.xcor() > 380:
            score_a = 0
            pen.clear()
            pen.write("player a: {} player b: {}".format(score_a, score_b), align="center",
                      font=("courier", 20, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            score_b += 1
            pen.clear()
            pen.write("player a: {} player b: {}".format(score_a, score_b), align="center",
                      font=("courier", 20, "normal"))
        if ball.xcor() < -380:
            score_b = 0
            pen.clear()
            pen.write("player a: {} player b: {}".format(score_a, score_b), align="center",
                      font=("courier", 20, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        # paddle and ball collisions
        if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            print("hit paddle b")

        if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            print("hit paddle a")

        # ai for paddle b
        if paddle_b.ycor() < ball.ycor():
            paddle_b_up()
        if paddle_b.ycor() > ball.ycor():
            paddle_b_down()
        # game over
        if ball.ycor() > 280 or ball.ycor() < -280 and ball.xcor() > 340 or ball.xcor() < -340:
            ball.goto(0, 0)
            ball.dx *= -1
            break
    if score_a > score_b:
        winner = 'player A'
    else:
        winner = 'player B'
    draw_rect_button(pen1, -100, 0, "continue")
    draw_rect_button(pen1, 100, 0, "exit")
    pen1.goto(0, 100)
    pen1.write(' {player} won the game you want to continue? '.format(player=winner), align="center",
               font=("Courier", 17, "bold"))
    score_a = 0
    score_b = 0
    pen.clear()
    pen.write("player a: {} player b: {}".format(score_a, score_b), align="center",
              font=("courier", 20, "normal"))
    screen.onclick(button_click)
    turtle.done()


game()
