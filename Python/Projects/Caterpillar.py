import random
import turtle as t
from Simple import *

t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('orange')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

caterpillar2 = t.Turtle()
caterpillar2.shape('square')
caterpillar2.color('pink')
caterpillar2.speed(0)
caterpillar2.penup()
caterpillar2.hideturtle()

leaf = t.Turtle()
leaf_shape = (0,0),(14,2),(18,6),(20,20),(6,18),(2,14)
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False
text_turtle = t.Turtle()
text_turtle.write ('Press SPACE to start', align='center', font=('Arial',16,'bold'))
text_turtle.hideturtle()
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window(caterpillar):
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2 
    (x,y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside
    

def game_over ():
    caterpillar.color ('grey')
    caterpillar2.color('yellow')
    leaf.color ('grey')
    t.penup()
    t.hideturtle()
    t.write ('Gamer Over :(', align='center', font=('Arial',30, 'normal'))

def display_score (current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y= (t.window_height ()/ 2) - 50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

def place_leaf ():
    leaf.ht()
    leaf.setx(random.randint(-200,200))
    leaf.sety(random.randint(-200,200))
    leaf.st()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()
    
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    caterpillar2.shapesize(1, caterpillar_length, 1)
    caterpillar2.setheading(180)
    caterpillar2.showturtle()
    display_score(score)
    place_leaf()
    
    while True:
        caterpillar.forward(caterpillar_speed)
        caterpillar2.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20 or leaf.distance(caterpillar2) < 20:
            place_leaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar2.shapesize(1, caterpillar_length, 1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 1
            display_score(score)
        if outside_window(caterpillar) or outside_window(caterpillar2):
            game_over()
            break



def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

def move_up2():
    if caterpillar2.heading() == 0 or caterpillar2.heading() == 180:
        caterpillar2.setheading(90)

def move_down2():
    if caterpillar2.heading() == 0 or caterpillar2.heading() == 180:
        caterpillar2.setheading(270)

def move_left2():
    if caterpillar2.heading() == 90 or caterpillar2.heading() == 270:
        caterpillar2.setheading(180)

def move_right2():
    if caterpillar2.heading() == 90 or caterpillar2.heading() == 270:
        caterpillar2.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_up2, 'w')
t.onkey(move_right2, 'd')
t.onkey(move_down2, 's')
t.onkey(move_left2, 'a')
t.listen()
t.mainloop()

clear()