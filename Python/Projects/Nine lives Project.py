import random
from P_Simple import *

clear()

#Good luck guessing the 3rd or 6th word
words = ['burger','taco','pneumonoultramicroscopicsilicovolcanoconiosis','cheese','weird','hippopotomonstrosesquippedaliophobia', 'free','fries','freeze','minecraft','minceraft','skyrim','hotdog','sweetroll','straw']
word = random.choice(words)
#clue = list('_' * len(word))  
clue =['_'] * len (word)
#hearts = u'\u2764'
# using symbols vs unicode 
heart = ('♥')
guessed_word_correctly = False
unknown_letters = len (word)

def update_clue (guessed_letter, word, clue, unknown_letters):
    index = 0
    while index < len(word):
        if guessed_letter == word[index]:
            clue[index] = guessed_letter
            unknown_letters = unknown_letters -1
        index = index + 1
    return unknown_letters 

# This sets up the difficulty level
difficulty = input('Choose a difficulty level (type 1, 2 ,3 or 4):\n 1:Easy 2: Normal, 3: Hard, 4 Extreme ')
difficulty = int (difficulty)

if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
elif difficulty == 3:
    lives = 6
elif difficulty == 4:
    lives = 3
elif difficulty == 88224646:
    lives= 100
else:
    print ('You didn\'t press a correct number. try again')
    difficulty = input('Choose a difficulty level (type 1, 2 or 3):\n 1:Easy 2: Normal, 3: Hard, 4 Extreme')
 
while lives > 0: 
    for j in range(len(clue)):   #The for code is just to make it look nicer when working in visual studio
        print(clue[j], end='')
    print('\n')
    print ('Lives left: ' + heart * lives)
    guess = input ('Guess a letter or the whole word: ')

    if guess == word:
        guessed_word_correctly = True
        break

    if guess in word:
        unknown_letters = update_clue(guess, word, clue , unknown_letters)
    
    else:
        print ('Incorrect, You lose a life 😢')  #emojis make it more fun
        lives = lives - 1
    
    if unknown_letters == 0:
        guessed_word_correctly = True
        break

if guessed_word_correctly:
    print ('You won 👍! the secret word is: ' + word)
    str(lives)
    print ('You had ' + str (lives) + ' lives left')


else: 
    print ('You lost 👎! the secret word is: ' + word)

















    #If you're reading this

    #Hi 👋