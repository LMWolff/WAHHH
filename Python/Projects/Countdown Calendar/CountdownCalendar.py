from P_Simple import *
from tkinter import *
from datetime import datetime

import holidays
import json

clear()

class Colors:
    background = '#F8F8F8' #Light Gray
    foreground = '#333333' #Dark Gray
    tilte = '#ff9e1e' # Orange
    today = '#bf3219' #Darker red


def get_events():
    #Get the event from the JSOn File
    with open ('D:\Logan 2023-24\Python\Projects\Countdown Calendar/events.json') as file:
        list_events = json.load(file)
    return list_events

#print(get_events()["My Birthday"])

def day_between_dates(date1, date2):
    #Subtract the two dates
    difference = date1 - date2
    return difference.days

def parse_events(events, today):
    date_times = {}
    for key, value in events.items():
        event_date = datetime.strptime(value,'%m/%d').replace(year=today.year)
        
        if event_date < today:
            event_date = event_date.replace(year=today.year + 1) 

        date_times[key] = event_date
    return dict(sorted(date_times.items(), key=lambda item: item[1])) # item ["Asher's birthday", "06/16"]


def draw ():
    canvas.delete('all') #Clear the canvas

    title = Label(events_frame, text='My Countdown Calendar', font=('Arial',28,'bold underline'), \
                  fg=Colors.tilte, bg=Colors.background)
    title.pack(anchor='w')

    for key, value in sorted_events.items():
        days_until = day_between_dates(value, today)
        display = f'It is {days_until} days until {key} ({value.strftime("%B %d")})'

        if days_until == 0:
            display= f'Today is {key}!'
            text= Label(events_frame, text=display, font=('Arial', 28, 'bold'), fg= Colors.today, bg=Colors.background)
        else:
            text= Label(events_frame, text=display, font=('Arial', 28, 'bold'), fg= Colors.foreground, bg=Colors.background)
        text.pack(anchor='w')

    canvas.update_idletasks()
    canvas.create_window(0,0, anchor='nw', window=events_frame)
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mousewheel (event):
    #Allows to scroll with your mousewheel
    canvas.yview_scroll(int(-1 * (event.delta / 120)),"units")

if __name__ == '__main__':
    root = Tk()
    root.title ("My Countdown Calendar")

    canvas=Canvas(root,width =1000, height= 800, scrollregion=(0,0,1000,800))
    canvas.pack(side=LEFT,fill=BOTH, expand= YES)

    events_frame = Frame(canvas,bg= Colors.background)
    canvas.pack(fill=BOTH, expand= YES)

    scrollbar = Scrollbar(root, orient=VERTICAL, command= canvas.yview)
    scrollbar.pack(side= RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    today= datetime.today().replace(hour=0,minute=0,second=0,microsecond=0)
    events = get_events()
    sorted_events = parse_events(events,today)

    draw()

    canvas.bind_all("<MouseWheel>", on_mousewheel)

    root.mainloop()