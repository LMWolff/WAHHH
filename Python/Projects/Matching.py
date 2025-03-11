import random
import time
from tkinter import Tk,Button,DISABLED,messagebox
from P_Simple import *


# x and y tells which button was pressed
def show_symbol(x,y):
    global first # this variable is to check if the button was the first pressed
    global previousX, previousY #keeps track of which buttons were pushed
    global moves # how many moves were done
    global pairs #number of pairs found
    buttons[x, y]['text']= button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        previousX = x
        previousY = y #if it is the first turn then the code remebers the x and y coordinates
        first = False
        moves = moves +1
    elif previousX != x or previousY !=y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previousX, previousY]['text'] = ''
            buttons[x, y]['text'] = ''
            #lets players time to see the symbol before hiding them
        else:
            buttons[previousX, previousY]['command']= DISABLED
            buttons[x, y]['command']= DISABLED
            pairs = pairs + 1
        if pairs == len(buttons)/2: #shows box with the number of moves
            messagebox.showinfo('Matching', 'Number of Moves: ' + str(moves))
            root.quit()
        first= True
            


root = Tk()
root.title('Matching')
root.resizable(width=False, height= False)

buttons = {} #a diction of buttons
first = True #Check if symbol if first in the match
previousX = 0 # both previous X and Y keeps tract of las button pressed 
previousY= 0
moves = 0 #number of moves to start out with
pairs = 0 # number of pairs at the beginning
button_symbols= {}#symbol of each button is stored in this diction
# list of symbols: scissors, Green check mark, heart, X, Pen, Black check mark,Sparkles,airplane,💀, curly loop,fist,hand,🌒,ℹ️,🤖
symbols = [u'\u2702',u'\u2702', u'\u2705',u'\u2705',u'\u2764',u'\u2764',
           u'\u2716',u'\u2716',u'\u2712',u'\u2712',u'\u2714',u'\u2714',
           u'\u2728',u'\u2728',u'\u2708',u'\u2708','💀','💀',
           u'\u27B0',u'\u27B0',u'\u270A',u'\u270A',u'\u270B',u'\u270B',
           '🌒','🌒','ℹ','ℹ','🤖','🤖',]

random.shuffle(symbols) #mixes up shapes

# Building the grid
for x in range (6): # number of rows
    for y in range (5): # number of columns (needs to change depeding on number of columns in symbols list)
        button= Button(command=lambda x=x, y=y: show_symbol(x,y), # creates buttons and set it's size and actoin
                        width=8, height= 7)
        button.grid(column=x, row=y)
        buttons[x, y]= button #saves each button in the buttons diction
        button_symbols[x, y] = symbols.pop() #sets button's symbol line

root.mainloop() #keeps window open and listens for buttons pressed

clear()
