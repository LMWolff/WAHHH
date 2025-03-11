import random 
import string
from P_Simple import *
clear()


adjs = ['green','tall','ugly','buffalo','violent']
nouns = ['McDonlds','Buffalo','Man','WendysFourForFour','WendysFiveDollarBiggyBag','SubwayFiveDollarFootlong']
#numbers = [1,2,3,4,5]
#sp_chs = ['@','#','$','!','?']
number_of_passwords = None

print ('Welcome to the Python Password Picker!\n')
number_of_passwords = int (input ('Please enter the number of passwords you would like: \n'))

'''while True:
    for num in range (number_of_passwords):
        adj = random.choice (adjs)
        noun = random.choice (nouns)
        #number = random.choice(numbers)
        number = random.randrange(0,100)
        #sp_ch = random.choice (sp_chs)
        sp_ch = random.choice (string.punctuation)

        password = adj + noun + str (number) + sp_ch
        print ('This is your secrue password: %s ' % password)

    response = input ('Would you like to choose another password? Type y or n: ').lower()
    if response == 'n':
        break
    elif response =='':
        break
    number_of_passwords = int (input ('Please enter the number of passwords you would like: \n'))
#how can we force it to take input, but if it is not recongnized, it will run the program again

#My perfered code'''


while True:
        for num in range (number_of_passwords):
            letter = ['q','a','z','w','s','x','e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','o','l','p''Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
                      '!','@','#','$','%','^','&','*','1','2','3','4','5','6','7','8','9','0',']','[','-','=','+','_','?','<','>','~','{','}','(',')']
            password = ''
            for j in range(15):
                password += random.choice(letter)

            print (password)
        response = input ('Would you like to choose another password? Type y or n: ').lower()
        if response == 'n':
            break
        elif response =='':
            break