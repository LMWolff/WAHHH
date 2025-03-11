from P_Simple import *
clear()
 
def mulitple():
    global score
    def checkguess (guess, answer):
        global score
        still_guesssing = True
        attempt = 0
        while still_guesssing and attempt <2:
            if guess.lower() == answer.lower():
                print ('You\'re correct!\n')
                score = score + 1
                print ('Your score is: %s' % score) 
                still_guesssing = False
        
            else:
                if attempt < 1:
                    guess = input ('Sorry wrong answer. Try again. ')
                attempt= attempt + 1
            if attempt == 3:
                print ('The correct answer is '+ answer + '\n')

    score = 0

    print ('Welcome to my quiz!\n')
    print ('Are you ready for some random info? Here we go')

    #https://screenrant.com/terminator-movie-cameron-screenplay-sold-one-dollar/?scrlybrkr=d174f8ed#:~:text=James%20Cameron%20Sold%20The%20Script,one%20called%20it%20%22abject%22.
    guess1 = input ('How many dollars was the terminator script sold for?\n \
    A) 1\n B) 50\n C) 100 thousand\n D) 7 million\n ')
    checkguess (guess1, 'A')

    #How I know 13*13= 169
    guess2 = input ('What is the (square root )-> √169?\n A) 15\n  B) 19\n C) 13\n D )84.5\n ')
    checkguess (guess2, 'C')

    #https://en.wikipedia.org/wiki/The_Game_Award_for_Game_of_the_Year
    guess3 = input ('What game won game of the year in 2022?\n \
    A) God of War\n B) Elden Ring\n C) Stray\n D) Hoizon Forbidden West:\n ')
    checkguess (guess3, 'B')

    #https://en.as.com/meristation/news/these-are-hollywoods-25-top-paid-actors-of-2022-and-2023-n/
    guess4 = input ('Who is the highest paid actor as of 2023? \n \
    A) The Rock \n B) Tom Cruise \n C) Johnny Depp \n D) Will Smith \n')
    checkguess (guess4, 'B')

    #https://en.wikipedia.org/wiki/Emu_War#:~:text=The%20Emu%20War%2C%20also%20known,the%20Wheatbelt%20of%20Western%20Australia.
    guess5 = input ('What bird did Australia lose a war to?\n \
    A) Ostriche \n B) Penguin \n C) Emu \n D) Red-winged blackbird \n')
    checkguess (guess5, 'C')

    #https://www.grunge.com/929500/what-is-the-only-sport-to-ever-be-played-on-the-moon/
    guess6 = input ('What was the first sport played on the moon?\n \
    A) Rugby \n B) Baseball \n C) Cricket \n D) Golf \n')
    checkguess(guess6, 'D')

    #https://www.nts.org.uk/stories/the-unicorn-scotlands-national-animal#:~:text=You%20probably%20wouldn't%20think,creature%20dates%20back%20many%20centuries.
    guess7 = input ('What is Scotlands nation animal?\n \
    A) Deer \n B) Unicorn \n C) Pegasus \n D) Dragon \n')
    checkguess (guess7, 'B')

    #https://www.nationalgeographic.com/animals/article/weird-laws-nation-dogs-ferrets-bigfoot
    guess8 = input ('What creature is illegal to hunt in Washington State?\n \
    A) Big foot \n B) Yeti \n C) Pegasus \n D) Loch Ness Monster \n')
    checkguess (guess8, 'A')

    #https://www.rabbies.com/en/blog/dragon-everything-you-need-know-about-welsh-national-animal#:~:text=The%20Dragon%3A%20Everything%20You%20Need%20to%20Know%20About%20the%20Welsh%20National%20Animal&text=The%20red%20dragon%2C%20or%20%E2%80%9CY,animal%20for%20thousands%20of%20years.
    guess9 = input ('What is the national animal of Wales?\n \
    A) Kiwi \n B) Yeti \n C) Dragon \n D) Inicorn \n')
    checkguess (guess9, 'C')

    #https://mytopglobal.com/countries-with-the-most-pyramids/
    guess10 = input ('What country has the most pyramids in the world?\n \
    A) Mexico\n B) Peru \n C) Egypt \n D) Sudan \n')
    checkguess (guess10, 'D')

    #https://www.rd.com/article/letter-not-in-any-state-name/#:~:text=Got%20your%20guess%3F,dropped%20out%20of%20our%20alphabet.)
    guess11 = input ('What letter doesn\'t appear in any U.S state? \n \
    A) Z \n B) Q \n C) B \n D) L \n')
    checkguess (guess11, 'B')

    #https://en.wikipedia.org/wiki/Beefalo#:~:text=Beefalo%20constitute%20a%20hybrid%20offspring,both%20animals%20for%20beef%20production.
    guess12 = input ('What is a cross of a cow and bison called?\n \
    A) Beefalo \n B) Bow \n C) Cison \n D) Gruffalo \n')
    checkguess (guess12, 'A')

    #https://www.britannica.com/topic/number-sign
    guess13 = input ('What is the actual name of the # symbol?\n \
    A) Loop symbol \n B) Number sign \n C) Octothorpe \n D) Hashtage/pound is the actual name \n')
    checkguess (guess13, 'c') 

    #https://www.nsf.gov/news/news_images.jsp?cntn_id=115564&org=NSF#:~:text=As%20bananas%20age%2C%20the%20chlorophyll,in%20studying%20programmed%20cell%20death.
    guess14= input ('what color do bananas glow under black light?\n \
    A) Green \n B) red \n C) purple \n D) blue \n')
    checkguess (guess14, 'D')

    #https://www.smithsonianmag.com/arts-culture/why-the-tomato-was-feared-in-europe-for-more-than-200-years-863735/#:~:text=In%20the%20late%201700s%2C%20a,were%20high%20in%20lead%20content.
    guess15 = input ('What fruit were europeans scared of eating when they were introduced?\n \
    A) apple \n B) tomato \n C) banana \n D) potato \n')
    checkguess (guess15, 'B')

    print ('\nThanks for taking my quiz')
    print ('Your final score was %s/15.' % score)
    percent = (score / 15) * 100
    percent = round (percent, 2)
    percent = str(percent)
    print ('You get a '  + percent +'%')

    percent = float(percent)
    if percent >= 97 and percent <=100:
        print ('Your grade is an A+!')
    elif percent >= 93 and percent <=96.99:
        print ('Your grade is a A!')
    elif percent >= 90 and percent <=92.99:
        print ('Your grade is a A-!')
    elif percent >= 87 and percent <=89.99:
        print ('Your grade is a B+.')
    elif percent >= 83 and percent <=86.99:
        print ('Your grade is a B.')
    elif percent >= 80 and percent <=82.99:
        print ('Your grade is a B-!')
    elif percent >= 77 and percent <=79.99:
        print ('Your grade is a C+.')
    elif percent >= 73 and percent <=76.99:
        print ('Your grade is a C.')
    elif percent >= 70 and percent <=72.99:
        print ('Your grade is a C-.')
    elif percent >= 67 and percent <=69.99:
        print ('Your grade is a D+..')
    elif percent >= 65 and percent <=66.99:
        print ('Your grade is a D.')
    elif percent >= 60 and percent <=64.99:
        print ('Your grade is a D.')
    else: 
        print ('You failed 😟...')

mulitple()