# "turtle" module lets you input graphics
# a simpler alternitve to the "pygame" module
import turtle

# Here we create a window using the name "wn" 
# and the turtle.Screen() function/method
wn = turtle.Screen()
wn.title("Pong Clone")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # .tracer() stops wn (window) from automatically updating,
# this lets us speed up the games by quite a bit or else it would run
# much slower

# Paddle A
paddle_a = turtle.Turtle() # small t is module name, and capital T is class name
paddle_a.speed(0) # speed of animation set to max otherwise to would be very slow
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # 20px x 20px by default. no 100px x 20px
paddle_a.penup() # by default turtle wants to draw a line so penup prevents that
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup() 
paddle_b.goto(350,0) # +350 to get a paddle on the other side

# Ball
ball = turtle.Turtle() 
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup() 
ball.goto(0,0)

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # tells program to listen for keyboard events
wn.onkeypress(paddle_a_up, "w") # when keyboard "w" is pressed, call function paddle_a_up()
wn.onkeypress(paddle_a_down, "s") # when keyboard "s" is pressed, call function paddle_a_down()

wn.onkeypress(paddle_b_up, "Up") # when keyboard "w" is pressed, call function paddle_a_up()
wn.onkeypress(paddle_b_down, "Down") # when keyboard "s" is pressed, call function paddle_a_down()



# Main game loop
while True:
    wn.update()