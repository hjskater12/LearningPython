# make pong you get score by hitting the ball with your square

# imports
import turtle
import random

# create 3 turtles juni = player 1 paddle, antijuni = player 2 paddle, i = ball
juni = turtle.Turtle()
antijuni = turtle.Turtle()
ball = turtle.Turtle()

# change shape of ball and increase speed and penup
ball.shape("circle")
ball.speed(0)
ball.penup()

# scoreboard
score1 = turtle.Turtle()
score2 = turtle.Turtle()
score1.color("red")
score2.color("red")
score1.hideturtle()
score2.hideturtle()

# changing turtle 1 and 2 speed
juni.speed(0)
antijuni.speed(0)

# screen settings
screen = turtle.Screen()
screen.tracer()
screen.update()
screen.bgcolor("black")
screen.register_shape("rectangle",((10,50), (10,-50), (-10,-50), (-10,50)))

# changing turtle 1 and 2 (player paddle) to square and change color
juni.shape("rectangle")
antijuni.shape("rectangle")
juni.color("purple")
antijuni.color("purple")
ball.color("blue")

# make a boundary box
juni.penup()
juni.goto(-200,200)
score1.penup()
score2.penup()
score1.goto(-200,200)
score2.goto(200,200)
score1.pendown()
score2.pendown()
juni.pendown()
for i in range(4):
  juni.forward(400)
  juni.right(90)
  
juni.penup()
juni.goto(0,0)
juni.pendown()

#make squraes go to position and penup
juni.penup()
antijuni.penup()

juni.goto(190,0)
antijuni.goto(-190,0)

# function for choosing angle for ball
def random_angle():
  if ball.xcor() >= 200 or ball.xcor() <= -200 or ball.ycor() >= 200 or ball.ycor() <= -200:
    ball.right(random.randint(180,359))
 

#set turtles up  
juni.right(90) 
antijuni.right(90)

# functions to make turtle 1 go up
def left2():
  juni.forward(7)

# function to make turtle 1 go down
def right2():
  juni.bk(7)
  
# function to make turtle 2 go up
def left():
  antijuni.forward(7)

# function to make turtle 2 go down
def right():
  antijuni.bk(7)

# checks if person is pressing the keys
screen.onkey(right,'w')
screen.onkey(left,'s')
screen.onkey(right2,'Up')
screen.onkey(left2,'Down')
screen.listen()

# initializng the score
points1 = 0
points2 = 0

# check if player 1 paddle and ball are less than 20 pixels apart you get a score

a = 0
b = 0

while True:
  ball.forward(10)

  # this if statment checks to see if ball bounces off the walls
  if ball.xcor() >= 200 or ball.xcor() <= -200 or ball.ycor() >= 200 or ball.ycor() <= -200:
    ball.right(random.randint(180,359))
    a = 0
    b = 0
    
  if ball.xcor() >= 200 or ball.xcor() <= -200:
    break
  
  if juni.ycor() >= 150:
    juni.bk(-7)
    
  if juni.ycor() <= -150:
    juni.forward(-7)
    
  if antijuni.ycor() >= 150:
    antijuni.bk(-7)
    
  if antijuni.ycor() <= -150:
    antijuni.forward(-7)


  # if a = 0 check if you score
  if a == 0:
    if abs(juni.xcor() - ball.xcor()) <= 20 and abs(juni.ycor() - ball.ycor()) <= 20:
        score2.clear()
        points2 = points2 + 1
        score2.write(points2)
        ball.right(-140)
        #make a = 1 and b = 0
        a = 1
        b = 0


    # if b = 0 check if you score
    if b == 0:
      if abs(antijuni.xcor() - ball.xcor()) <= 20 and abs(antijuni.ycor() - ball.ycor()) <= 20:
          score1.clear()
          points1 = points1 + 1
          score1.write(points1)
          ball.right(140)
          #make b = 1 and a = 0 
          b = 1
          a = 0