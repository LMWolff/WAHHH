import os


# Simple Defs
def clear(): #clears Terminal
    os.system('cls')

def line(): # prints a line
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def end(): # Breaks loop
    quit()

def new(): # New line
    print('\n')

def working():
    print('working')

def onoff(var):
    if var == True:
        return 'on'
    
    if var == False:
        return 'off'

def Format(string):
    string = string.lower().split('')
    for j in range(len(string)):
        string[j] = [j][0].capitalize() + string[j][1:]
    return ' '.join(string)