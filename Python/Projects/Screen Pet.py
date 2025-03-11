from tkinter import HIDDEN, NORMAL, Tk,Canvas
import random
from P_Simple import *

def change_color():
    pet_colors = ['red','orange','blue','green','yellow','#ffdafa','purple']
    ear_colors= ['black','grey','brown']
    c.ear_inside = random.choice(ear_colors)
    c.body_color = random.choice(pet_colors)
    c.itemconfigure(body, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(ear_left, outline=c.body_color)
    c.itemconfigure(ear_right, outline=c.body_color)
    c.itemconfigure(foot_left, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(foot_right, outline=c.body_color, fill=c.body_color)
    root.after(2000, change_color)

def toggle_eyes():
    current_color=c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state=c.itemcget(pupil_left,'state')
    new_state = NORMAL if current_state == 'hidden' else 'hidden'
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left,fill=new_color)
    c.itemconfigure(eye_right,fill=new_color)

def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)

def toggle_left_eye():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state=c.itemcget(pupil_left,'state')
    new_state = NORMAL if current_state == 'hidden' else 'hidden'
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(eye_left,fill=new_color)

def wink (event):
    toggle_left_eye()
    root.after(250, toggle_left_eye)



def show_happy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(left_cheek, state= NORMAL)
        c.itemconfigure(right_cheek, state= NORMAL)
        c.itemconfigure(mouth_happy, state= NORMAL)
        c.itemconfigure(mouth_normal, state= HIDDEN)
        c.itemconfigure(mouth_sad, state= HIDDEN)
        c.happy_level = 10
    return

def hide_happy (event):
    c.itemconfigure(left_cheek, state= HIDDEN)
    c.itemconfigure(right_cheek, state= HIDDEN)
    c.itemconfigure(mouth_happy, state= HIDDEN)
    c.itemconfigure(mouth_normal, state= NORMAL)
    c.itemconfigure(mouth_sad, state= HIDDEN)
    return

def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state = HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1
    root.after(4000, sad)

def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_tip, state = NORMAL)
        c.itemconfigure(mouth_main, state = NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.itemconfigure(mouth_main, state=HIDDEN)
        c.tongue_out=False

def toggle_pupils():
    if not c.eyes_crossed:
        c.move(pupil_left, 10,-5)
        c.move(pupil_right, -10,-5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10,5)
        c.move(pupil_right, 10,5)
        c.eyes_crossed = False

def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1000,toggle_tongue)
    root.after(1000, toggle_pupils)
    return


root=Tk()
c = Canvas(root, width=400, height=400)

#inspired by jigglypuff

c.body_color = '#ffdafa'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color,fill= c.body_color)
ear_left = c.create_polygon(85, 70, 75, 10, 125, 40, outline=c.body_color,fill='black',width= 5)
ear_right = c.create_polygon(275, 45, 335, 10, 320, 79, outline=c.body_color,fill='black',width=5)

foot_left = c.create_oval (65, 320, 145, 360, outline=c.body_color,fill= c.body_color)
foot_right = c.create_oval (250, 320, 330, 360, outline=c.body_color,fill= c.body_color)
# eye_left =c.create_oval (130, 110, 160, 170, outline='black', fill='white')
# eye_right =c.create_oval (230, 110, 260, 170, outline='black', fill='white')
eye_left =c.create_oval (120, 110, 170, 170, outline='black', fill='white')
eye_right =c.create_oval (220, 110, 270, 170, outline='black', fill='white') #to make eyes bigger
#both pupils are Dark Cyan
# pupil_left = c.create_oval(140, 145, 150, 155, outline="black", fill="#008393")
# pupil_right =c.create_oval(240, 145, 250, 155, outline="black", fill="#008393")
pupil_left = c.create_oval(135, 125, 155, 155, outline="black", fill="#008393")
pupil_right =c.create_oval(235, 125, 255, 155, outline="black", fill="#008393") #makes pupils bigger
mouth_normal =c.create_line(140, 250, 260, 250, smooth=1, width=2, state=NORMAL, fill="black")
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN, fill="black")
mouth_sad =c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN, fill="black")
left_cheek =c.create_oval(70, 180, 120, 230,outline='#ff70ed',fill='#ff70ed',state=HIDDEN)
right_cheek =c.create_oval(280, 180, 330, 230,outline='#ff70ed',fill='#ff70ed',state=HIDDEN)
mouth_main = c.create_rectangle(170, 250, 230, 290, outline='red',fill= '#FBAED2',state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='#FBAED2',state=HIDDEN)


#background color is based off of a pokemon card with jigglypuff
c.configure(bg='#9966CC',highlightthickness=0)
c.pack()
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>',cheeky)
c.bind('<Button-3>',wink)
c.happy_level= 10
c.eyes_crossed = False
c.tongue_out = False
root.after(1000, blink)
root.after(4000, sad)
root.after(2000, change_color)
root.mainloop()

clear()