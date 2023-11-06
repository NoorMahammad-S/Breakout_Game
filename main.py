import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

for y in range(5):
    for x in range(8):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[y])
        brick.penup()
        brick.goto(-350 + x * 100, 200 - y * 20)
        bricks.append(brick)

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 350:
        x = 350
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -350:
        x = -350
    paddle.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.ycor() > -240) and (ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Ball and brick collisions
    for brick in bricks:
        if brick.distance(ball) < 25:
            brick.goto(1000, 1000)  # Move the brick out of the screen
            ball.dy *= -1

    # Check if all bricks are destroyed
    if all(brick.ycor() > 1000 for brick in bricks):
        wn.bgcolor("black")
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0
        paddle.goto(0, -250)
        wn.update()
        break
