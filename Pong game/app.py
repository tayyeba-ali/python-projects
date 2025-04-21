import turtle
import time
import winsound

# Setup window
wn = turtle.Screen()
wn.title("Pong by @tayyeba-ali")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score variables
score_a = 0
score_b = 0
max_score = 5

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.2  # Slightly faster speed
ball.dy = 1.2

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Sound function
def play_sound():
    try:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    except:
        pass

# Paddle controls
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        paddle_b.sety(y - 20)

# Key bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
game_running = True
while game_running:
    wn.update()
    time.sleep(0.01)  # Control overall game speed

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        play_sound()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        play_sound()

    # Right border - Player A scores
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = -1.2
        ball.dy = 1.2
        play_sound()

        if score_a == max_score:
            pen.goto(0, 0)
            pen.write("🎉 Game Over! Player A Wins 🎉", align="center", font=("Courier", 24, "bold"))
            game_running = False

    # Left border - Player B scores
    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = 1.2
        ball.dy = 1.2
        play_sound()

        if score_b == max_score:
            pen.goto(0, 0)
            pen.write("🎉 Game Over! Player B Wins 🎉", align="center", font=("Courier", 24, "bold"))
            game_running = False

    # Paddle collision - B
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        play_sound()

    # Paddle collision - A
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        play_sound()

# Keep window open
wn.mainloop()
