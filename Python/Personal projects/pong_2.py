from tkinter import Tk
from random import choice
import os
from Simple import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Pong:
    def __init__(self):
        self.tk = Tk()

        self.p1 = [5, 4]
        self.p2 = [5, 58]

        self.move = [-1, choice([1, -1])]

        self.l = 5

        self.ball = [7, 31]

        self.terminal = [
            list(' ------------------------------------------------------------- '),
            list('|                                                             |'),
            list('|                                                             |'),
            list('|                                                             |'),
            list('|                                                             |'),
            list('|   |                                                     |   |'),
            list('|   |                                                     |   |'),
            list('|   |                          O                          |   |'),
            list('|   |                                                     |   |'),
            list('|   |                                                     |   |'),
            list('|                                                             |'),
            list('|                                                             |'),
            list('|                                                             |'),
            list('|                                                             |'),
            list(' ------------------------------------------------------------- ')
        ]

    def moveUp(self, p):
        i, j = p
        l = self.l

        if i == 1:
            return

        self.terminal[i + l - 1][j] = ' '

        for x in range(i - 1, i + l - 1):
            self.terminal[x][j] = '|'

        p[0] -= 1

    def moveDown(self, p):
        i, j = p
        l = self.l

        if i + l == len(self.terminal) - 1:
            return

        self.terminal[i][j] = ' '

        for x in range(i + 1, i + l + 1):
            self.terminal[x][j] = '|'

        p[0] += 1

    def moveComputer(self):
        if self.move[0] == -1:
            self.moveUp(self.p2)
        if self.move[0] == 1:
            self.moveDown(self.p2)

    def moveBall(self):
        try:
            if self.terminal[self.ball[0] + self.move[0]][self.ball[1]] == '-':
                self.move[0] *= -1

            if self.terminal[self.ball[0]][self.ball[1] + self.move[1]] == '|':
                self.move[1] *= -1
            elif self.terminal[self.ball[0] + self.move[0]][self.ball[1] + self.move[1]] == '|':
                self.move[0] *= -1
                self.move[1] *= -1

            self.terminal[self.ball[0]][self.ball[1]] = ' '

            self.ball[0] += self.move[0]
            self.ball[1] += self.move[1]

            self.terminal[self.ball[0]][self.ball[1]] = 'O'

            if ' ' in self.terminal[0][1:-1]:
                i = self.terminal[0][1:-1].index(' ')

                self.terminal[i] = '-'

            if ' ' in self.terminal[-1][1:-1]:
                i = self.terminal[-1][1:-1].index(' ')

                self.terminal[i] = '-'

            self.print()

            if self.move[1] == 1:
                self.moveComputer()
        except:
            if (self.terminal[self.ball[0] - 1] == '-') and (self.terminal[self.ball[0] + 1] == '|') or \
                    (self.terminal[self.ball[0] + 1] == '-') and (self.terminal[self.ball[0] - 1] == '|'):
                self.move[0] *= -1
            else:
                self.move[0] *= -1
                self.move[1] *= -1

        self.tk.after(25, self.moveBall)

    def play(self):
        self.tk.bind('<Up>', lambda x: self.moveUp(self.p1))
        self.tk.bind('<Down>', lambda x: self.moveDown(self.p1))

        self.moveBall()

        self.tk.mainloop()

    def print(self):
        clear()
        print('\n'.join(''.join(i) for i in self.terminal))

pong = Pong()
pong.play()
clear()