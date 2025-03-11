import turtle as t

from random import randint, random



def draw_star (point,size,col,x,y):
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    angle= 180- (180/point)
    t.color (col)
    t.begin_fill()
    for i in range (point):
        t.forward (size)
        t.right (angle)
    t.end_fill()

#main code
t.Screen().bgcolor('black')

while True:
    ranPts = randint (2,5) * 2 + 1
    ranSize = randint (10,50)
    ranCol = (random(), random(),random())
    ranX = randint (-950, 900)
    ranY = randint (-950,950)
    draw_star(ranPts,ranSize,ranCol, ranX,ranY)





