#Among Us Mk 3
import turtle 

t=turtle.Pen()
t.color('#94918e')
t.width(10000)
t.forward(0)

wn = turtle.getscreen ()
crew =turtle.Turtle ()
wn.setup (width= 600, height = 600)

color = 'pink'
glass = '#92D3E4'
shiny = 'white'

def body():
    crew.pensize(20)
    crew.speed (0)
    crew.fillcolor(color)
    crew.begin_fill()

    #makin right side
    crew.right (90)
    crew.forward(50)
    crew.right(180)
    crew.circle (40, -180)
    crew.right(180)
    crew.forward(200)

    # zee head
    crew.right(180)
    crew.circle(100, -180)

    #left side
    crew.backward(20)
    crew.left(15)
    crew.circle(500, -20)
    crew.backward(20)

    crew.circle (40, -180)
    crew.left (7)
    crew.backward(50)

    #heep
    crew.up()
    crew.left(90)
    crew.forward(10)
    crew.right(90)
    crew.down()
    crew.right(240)
    crew.circle(50, -70)

    crew.end_fill()

def eye():
    crew.up()
    crew.right(230)
    crew.forward(100)
    crew.left(90)
    crew.forward(20)
    crew.right(90)

    crew.down()
    crew.fillcolor(glass)
    crew.begin_fill()

    crew.right(150)
    crew.circle(90,-55)

    crew.right(180)
    crew.forward(1)
    crew.right(180)
    crew.circle(10,-65)
    crew.right (180)
    crew.forward(110)
    crew.right(180)

    crew.circle (50, -190)
    crew.right (170)
    crew.forward(80)
    
    crew.right(180)
    crew.circle(45, -30)
    
    crew.end_fill()
    crew.up()
    crew.goto(-80,0)

def backpack():
   crew.right (180)

   crew.fillcolor(color)
   crew.begin_fill()

   crew.down()
   crew.forward(30)
   crew.right(225)

   crew.circle(300,-30)
   crew.right(260)
   crew.forward (30)

   crew.end_fill()

g= turtle.Pen()
g.up()
g.goto (-400,-100)
floor = '#f0ba78'
def ground():

    g.down()
    g.fillcolor(floor)
    g.begin_fill()

    g.forward (800)
    g.right(90)
    g.forward(200)

    g.right (90)
    g.forward (800)
    g.right(90)
    g.forward(200)

    
    g.end_fill()


body()
eye()
backpack()
ground()

crew.hideturtle()
turtle.done()