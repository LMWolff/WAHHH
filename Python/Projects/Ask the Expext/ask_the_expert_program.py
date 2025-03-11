from P_Simple import *
from tkinter import Tk, simpledialog, messagebox
clear()

#This is based off of my favorite game Borderlands 2
#The code tells you who drops what item that you can use
def read_from_file():
    with open('F:\Logan 2023-24\Python\Projects\Ask the Expext/special_items_list.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            unique, source = line.split ('/')
            special_item_list[unique] = source
            unique = unique.lower()
            source = source.lower()
            special_item_list[unique] = source

def write_to_file (unique,source):
    with open('F:\Logan 2023-24\Python\Projects\Ask the Expext/new_special_items_list.txt', 'a') as file:
        file.write('\n' + unique + '/' + source)


print ('\nAsk the Expert- Welcome to my expert Borderland 2 Uniques drop program')
print ('Find who drops what unique gear on old game.\n')

root = Tk()
root.withdraw()

special_item_list = {}

read_from_file()

while True:
    query_unique = simpledialog.askstring('Item','Type the name of a unique item: ').lower()
    if ' ' in query_unique:
        query_unique == query_unique.split(" ") [0].capitalize() + " " + query_unique.split(" ") [1].capitalize()
        
    else: 
        query_unique == query_unique.capitalize()

    if query_unique in special_item_list:
        result = special_item_list[query_unique]
        messagebox.showinfo ('Answer','The source of '+ query_unique + ' is ' + result + '.')

    else:
        new_unique= simpledialog.askstring('Teach Me', 'I don\'t know. Please enlighten me. Give me the name of the source of ' + query_unique +'?')
        if ' ' in new_unique:
            new_unique == new_unique.split(" ") [0].capitalize() + " " + new_unique.split(" ") [1].capitalize()
        else: 
            new_unique == new_unique.capitalize()
            special_item_list[query_unique] = new_unique
        write_to_file (query_unique, new_unique)

root.mailoop()

#print (special_item_list)

#Used to be only legendary items but i change it most uniques
#Does not contain any quest item.
#Also no class modes but both can be added later.