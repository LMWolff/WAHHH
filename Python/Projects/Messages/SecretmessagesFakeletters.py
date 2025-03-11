from tkinter import messagebox, simpledialog, Tk
from random import choice
from P_Simple import *
import os
clear()

def get_task():
    task = simpledialog.askstring ('Task','Do you want to encrypt or decrypt')
    return task

def get_message():
    message= simpledialog.askstring ('Message','Please enter the message: ')
    return message

def is_even (number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range (0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters




def get_letters(message):
    even_letters = []
    odd_letters=[]
    for counter in range (1, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
        else:
            odd_letters.append(message[counter])
    return {"even":even_letters , "odd":odd_letters}

def swap_letters(message):
    letter_list = []
    if not is_even (len(message)):
        message += ' '
    for i in range (int(len(message)/2)):
        letter_list.append(message[i*2+1])
        letter_list.append(message[i*2])
    new_message = ''.join(letter_list)
    return new_message

def encrypt (message):
    encrypted_list = []
    fake_letters = ['b','d','f','h','j','l','n','p','r','t','v','w','x','z','Q','F','L','A','3','1','4','5']
    for counter in range (0, len(message)):
        encrypted_list .append(message[counter])
        encrypted_list.append(choice(fake_letters))
    new_message = ''.join(encrypted_list)
    return new_message


def decrypt (message):
    even_letters= get_even_letters(message)
    new_message = ''.join(even_letters)
    return new_message

root = Tk()

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = encrypt(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
    elif task == 'decrypt':
        message = get_message ()
        decrypted = decrypt(message)
        messagebox.showinfo ('Plaintext of the secret message is:', decrypted)
    else:
        break

root.mainloop() 
