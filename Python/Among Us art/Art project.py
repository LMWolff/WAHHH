#Among Us Mk 2
import turtle

t=turtle.Pen()
t.color('#1d1d1f')
t.width(10000)
t.forward(0)

wn = turtle.getscreen ()
sus = turtle.Turtle ()
wn.setup (width= 600, height = 600)

color = 'orange'
eye_color = '#92D3E4'
star_color = 'white'

    #makin the body 
def body():
    """draws the body"""
    sus.pensize(20)
    sus.speed (0)
    sus.fillcolor(color)
    sus.begin_fill()

    #makin right side
    sus.right (90)
    sus.forward(50)
    sus.right(180)
    sus.circle (40, -180)
    sus.right(180)
    sus.forward(200)

    # zee head
    sus.right(180)
    sus.circle(100, -180)

    #left side
    sus.backward(20)
    sus.left(15)
    sus.circle(500, -20)
    sus.backward(20)

    sus.circle (40, -180)
    sus.left (7)
    sus.backward(50)

    #heep
    sus.up()
    sus.left(90)
    sus.forward(10)
    sus.right(90)
    sus.down()
    sus.right(240)
    sus.circle(50, -70)

    sus.end_fill()

    #eye glass
def glass():
    sus.up()
    sus.right(230)
    sus.forward(100)
    sus.left(90)
    sus.forward(20)
    sus.right(90)

    sus.down()
    sus.fillcolor(eye_color)
    sus.begin_fill()

    sus.right(150)
    sus.circle(90,-55)

    sus.right(180)
    sus.forward(1)
    sus.right(180)
    sus.circle(10,-65)
    sus.right (180)
    sus.forward(110)
    sus.right(180)

    sus.circle (50, -190)
    sus.right (170)
    sus.forward(80)
    
    sus.right(180)
    sus.circle(45, -30)
    
    sus.end_fill()
    sus.up()
    sus.goto(-80,0)

    #backpack
def backpack():
   sus.right (180)

   sus.fillcolor(color)
   sus.begin_fill()

   sus.down()
   sus.forward(30)
   sus.right(225)

   sus.circle(300,-30)
   sus.right(260)
   sus.forward (30)

   sus.end_fill()

s = turtle.Pen()
s.up()
s.goto(-180,180)
s.speed (0)
s.width (10)

s.fillcolor(star_color)
s.begin_fill()

    #drawing 4 pretty stars
def draw_star(size, points):
     angle = 360 / points
     for x in range(0, points):
         s.forward(size)
         s.left(180 - angle)
         s.forward(size)
         s.right(180-(angle * 2))
        

        #numbers can be adjusted if wanted
draw_star(10,20)
s.end_fill()
s.up()
s.goto (-180,-150)

s.fillcolor(star_color)
s.begin_fill()
draw_star(20,30)

s.end_fill()
s.up()
s.goto (200,-150)       

s.fillcolor(star_color)
s.begin_fill()
draw_star(20,30)

s.end_fill()
s.up()
s.goto (200,150)    

s.fillcolor(star_color)
s.begin_fill()
draw_star(20,30)
s.end_fill()

s.up()
s.goto (300,0)       

s.fillcolor(star_color)
s.begin_fill()
draw_star(20,30)

s.end_fill()

s.up()
s.goto (-300,0)       

s.fillcolor(star_color)
s.begin_fill()
draw_star(20,30)

s.end_fill()
body()
glass()
backpack()

sus.hideturtle()
s.hideturtle()

turtle.done()

