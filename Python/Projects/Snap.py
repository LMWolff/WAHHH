import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL,CHORD,ARC
# from P_Simple import *

root=Tk()
root.title('Snap')

c= Canvas(root, width=400, height= 400)

shapes = []

circle = c.create_oval(35,20,365,350, outline='black',fill='black', state= HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20,365,350, outline='red',fill='red', state= HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20,365,350, outline='green',fill='green', state= HIDDEN)
shapes.append(circle)
circle = c.create_oval(35,20,365,350, outline='blue',fill='blue', state= HIDDEN)
shapes.append(circle)

rectangle = c.create_rectangle (35, 100, 365, 270, outline='black',fill='black',state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle (35, 100, 365, 270, outline='red',fill='red',state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle (35, 100, 365, 270, outline='green',fill='green',state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle (35, 100, 365, 270, outline='blue',fill='blue',state=HIDDEN)
shapes.append(rectangle)

square = c.create_rectangle (35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle (35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle (35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle (35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
shapes.append(square)

triangle = c.create_polygon(35,200,365,200,200,35, outline='blue',fill='blue',state=HIDDEN)
shapes.append(triangle)
triangle = c.create_polygon(35,200,365,200,200,35, outline='red',fill='red',state=HIDDEN)
shapes.append(triangle)
triangle = c.create_polygon(35,200,365,200,200,35, outline='green',fill='green',state=HIDDEN)
shapes.append(triangle)
triangle = c.create_polygon(35,200,365,200,200,35, outline='black',fill='black',state=HIDDEN)
shapes.append(triangle)

arc = c.create_arc (-235, 120, 365, 370, outline = 'black', fill = 'black', state = HIDDEN)
shapes.append(arc)
arc = c.create_arc (-235, 120, 365, 370, outline = 'red', fill = 'red', state = HIDDEN)
shapes.append(arc)
arc = c.create_arc (-235, 120, 365, 370, outline = 'green', fill = 'green', state = HIDDEN)
shapes.append(arc)
arc = c.create_arc (-235, 120, 365, 370, outline = 'blue', fill = 'blue', state = HIDDEN)
shapes.append(arc)
c.pack()

random.shuffle(shapes)

shape = None
previous_color = 'a' #Stops from cheating
current_color = 'b'
player1_score = 0
player2_score = 0

def next_shape():
    global shape
    global previous_color
    global current_color

    previous_color = current_color

    c.delete(shape)
    if len(shapes) > 0:
        shape = shapes.pop()
        c.itemconfigure(shape, state = NORMAL)
        current_color = c.itemcget(shape, 'fill')
        root.after(1000, next_shape)
    else:
        c.unbind('q')
        c.unbind('p')
        if player1_score > player2_score:
            c.create_text (200, 200, text='Winner: Player 1')
        elif player2_score > player1_score:
            c.create_text (200, 200, text='Winner: Player 2')
        else:
            c.create_text (200,200, text='Draw')
        c.pack()

def snap(event):
    global shape
    global player1_score
    global player2_score
    global previous_color
    valid = False

    c.delete(shape)

    if previous_color == current_color:
        valid = True
    
    if valid:
        if event.char == 'q':
            player1_score = player1_score + 1
            shape = c.create_text(200,200, text='Snape! Player 1 score 1 point')#Unique dialog
        else:
            player2_score= player2_score + 1
            shape = c.create_text(200,200, text='Snape! Player 2 score 1 point')
        
    else:
        if event.char == 'q':
            player1_score = player1_score - 1
            shape = c.create_text (200,200, text='Wrong! Player 1 lose 1 point')#Unique dialog
        else:
            player2_score = player2_score - 1
            shape = c.create_text (200,200, text='Wrong! Player 2 lose 1 point')
        
    previous_color = ''
    c.pack()
    root.update_idletasks()
    time.sleep(1)



root.after(3000, next_shape)
c.bind('q',snap)
c.bind('p',snap)
c.focus_set()

root.mainloop()
# clear()