from tkinter import messagebox, simpledialog, Tk
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
    swapped_message = swap_letters(message)
    encrypt_message = ''.join(reversed(swapped_message))
    return encrypt_message

def decrypt (message):
    unreversed_message= ''.join(reversed(message))
    decrypted_message = swap_letters (unreversed_message)
    return decrypted_message

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
