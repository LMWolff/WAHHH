from tkinter import *
from PIL import Image
import math, io, time #skimage.io as ski_io
from io import BytesIO

fname = input('enter a name for file: ')

cw = 1800
ch = 900



tk = Tk()
width = 20

myCanvas = Canvas(tk, bg="white", height=ch, width=cw)

color = "black"
px, py = (-1, -1)

def paint(event):
    global px, py
    x1, y1 = (event.x - width/2), (event.y - width/2)
    x2, y2 = ( event.x + width/2), (event.y + width/2)
    myCanvas.create_oval(x1, y1, x2, y2, fill = color, outline= color)

    if(px == -1):
        px = event.x
        py = event.y
    myCanvas.create_line(px, py, event.x, event.y, fill = color, width = width)
    px = event.x
    py = event.y

def pStop(e):
    global px, py
    px, py = (-1, -1)

def mwheel(e):
    global width
    if e.delta > 0:
        width = min(400, width+1)
    if e.delta < 0:
        width = max(1, width-1)
    
def saves():
    global fname, w
    eps = myCanvas.postscript(colormode='color')
    # Save canvas as "in-memory" EPS and pass to PIL without writing to disk
    im = Image.open(BytesIO(bytes(eps,'ascii')))
    im.save(fname + '.png')

def ClearCanvas():
    global color
    myCanvas.delete('all')
    color = 'black'

colors = ['black', 'red', 'blue', 'orange', 'green', 'pink', 'purple', 'brown', 'yellow', 'white']

# def rainbow():
#     global colors, color
#     index = 0
#     while True:
#         color = colors[index]
#         index+=1
#         if(index>len(colors)-1):
#             index = 0
#         time.sleep(1)
        
def keyPress(e):
    global color
    if (e.keysym == '1'):
        color = 'red'
    if (e.keysym == '2'):
        color = 'blue'
    if (e.keysym == '3'):
        color = 'orange'
    if (e.keysym == '4'):
        color = 'green'
    if (e.keysym == '5'):
        color = 'pink'
    if (e.keysym == '6'):
        color = 'purple'
    if (e.keysym == '7'):
        color = 'brown'
    if (e.keysym == '8'):
        color = 'cyan'
    if (e.keysym == '9'):
        color = 'yellow'
    if (e.keysym == '0'):
        color = 'black'
    if (e.keysym == 'q'):
        color = 'white'
    # if (e.keysym == 'w'):
    #     rainbow()
    if (e.keysym == 's'):
        saves()
    if (e.keysym == 'r'):
        ClearCanvas()

tk.bind("<KeyPress>", keyPress)
tk.bind("<ButtonRelease>", pStop)
tk.bind_all("<MouseWheel>", mwheel)

myCanvas.pack(expand = YES, fill = BOTH)
myCanvas.bind("<B1-Motion>", paint)
mainloop()
