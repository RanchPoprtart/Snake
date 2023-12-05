import turtle
import random

direction = 90
score = 0

win = turtle.Screen()
win.title("snake")

scorelabel = turtle.Turtle()
scorelabel.hideturtle()
scorelabel.penup()
scorelabel.goto(-250, 160)
scorelabel.write("Score: " + str(score), font=("Arial", 24, "bold"))

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-250, 250)
pen.down()
for i in range(4):
    pen.forward(500)
    pen.right(90)

pen.hideturtle()

snake = []
x = 0

for i in range(3):
    snake.append(turtle.Turtle("square"))
    snake[i].penup()
    snake[i].setx(x)
    x += 24

def key_left():
    global direction
    direction -= 90
    if direction < 0:
        direction = 270
    print(direction)

def key_right():
    global direction
    direction += 90
    if direction == 360:
        direction = 0
    print(direction)

win.onkeypress(key_left, "Left")
win.onkeypress(key_right, "Right")
win.listen()

food = turtle.Turtle("square")
food.hideturtle()
food.speed(0)
food.penup()
food.color("red")

def place_food():
    food.hideturtle()
    x = random.randint(-10, 10) * 24
    y = random.randint(-10, 10) * 24
    food.goto(x, y)
    food.showturtle()
 
place_food()
done = False

while not done:
    i = len(snake)
    snake.append(turtle.Turtle())
    snake[i].hideturtle()
    snake[i].shape("square")
    snake[i].penup()
    snake[i].speed(0)

    if direction == 0:
        snake[i].setx(snake[i - 1].xcor())
        snake[i].sety(snake[i - 1].ycor() + 24)
    elif direction == 90:
        snake[i].goto(snake[i - 1].xcor() + 24, snake[1 - 1].ycor())
    elif direction == 180:
        snake[i].goto(snake[i - 1].xcor(), snake[1 - 1].ycor() - 24)
    else:
        snake[i].goto(snake[i - 1].xcor() - 24, snake[i - 1].ycor())

    snake[i].showturtle()
    if snake[i].position == food.position:
        place_food()
        score += 1
        scorelabel.clear()
        scorelabel.write("Score: " + str(score), font=("Arial", 24, "bold"))
    else:
        snake[0].hideturtle()
        snake.pop(0)
        i -= 1

    for j in range(0, i - 1):
        if snake[i].position() == snake[j].position():
            done = True
            break

    if snake[i].xcor() > 250 or snake[i].xcor() < -250 or snake[i].ycor() > 250 or snake[i].ycor() < -250:
        done = True


turtle.exitonclick()