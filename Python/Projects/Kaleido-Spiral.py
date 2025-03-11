import turtle as t
from itertools import cycle

colors= cycle (['red','orange','yellow','green','blue','purple','pink','brown'])

def draw_shape (size,angle,shift,shape):
    #t.bgcolor(next(colors))
    t.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
        t.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range (4):
            t.forward (size * 2)
            t.left(90)
        next_shape = 'circle'
    t.right(angle)
    t.forward(shift)
    draw_shape(size + 1, angle +1, shift +1, next_shape)

t.bgcolor('black')
t.speed(0)
t.pensize()
draw_shape(30,0,1,'circle')



'''def draw_circle (size, angle,shift):
    #t.bgcolor(next(colors))
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 5, angle +1, shift +1)



t.speed(0)
t.pensize(4)

draw_circle(30,0,1)'''