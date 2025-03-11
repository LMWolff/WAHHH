import os
from P_Simple import *
clear() 
def TorF():
    global score
    def checkguess (guess, answer):
        global score
        still_guesssing = True
        attempt = 0
        while still_guesssing and attempt <1:
            if guess.lower() == answer.lower():
                print ('You\'re correct!\n')
                score = score + 1
                print ('Your score is: %s' % score) 
                still_guesssing = False
        
            else:
                if attempt < 1:
                    print  ('Sorry wrong answer. Try again.\n ')
                attempt= attempt + 1
      
    score = 0

    print ('Welcome to my quiz!\n')
    print ('Are you ready for some random info? Here we go')

    #https://screenrant.com/terminator-movie-cameron-screenplay-sold-one-dollar/?scrlybrkr=d174f8ed#:~:text=James%20Cameron%20Sold%20The%20Script,one%20called%20it%20%22abject%22.
    guess1 = input ('The terminator script sold for only $1.\n \
    T or F\n ')
    checkguess (guess1, 'T')

    #How I know 13*13= 169
    guess2 = input ('The square root  of 169 is 84.5. \n \
    T or F\n ')
    checkguess (guess2, 'f')
    print ('84.5 is 169/2 the square root of 169 is 13.\n')

    #https://en.wikipedia.org/wiki/The_Game_Award_for_Game_of_the_Year
    guess3 = input ('God of War Ragnarök won game of the year in 2022.\n \
    T or F\n ')
    checkguess (guess3, 'f')
    print ('Elden Ring won.\n')

    #https://en.as.com/meristation/news/these-are-hollywoods-25-top-paid-actors-of-2022-and-2023-n/
    guess4 = input ('Tom Cruise is the highest paid actor as of 2023. \n \
    T or F\n ')
    checkguess (guess4, 'T')

    #https://en.wikipedia.org/wiki/Emu_War#:~:text=The%20Emu%20War%2C%20also%20known,the%20Wheatbelt%20of%20Western%20Australia.
    guess5 = input ('Australia lost a war to ostriches.\n \
    T or F\n ')
    checkguess (guess5, 'F')
    print ('The over population of emus won against the Australian government.')

    #https://www.grunge.com/929500/what-is-the-only-sport-to-ever-be-played-on-the-moon/
    guess6 = input ('Golf was the first sport played on the moon.\n \
    T or F\n ')
    checkguess(guess6, 't')

    #https://www.nts.org.uk/stories/the-unicorn-scotlands-national-animal#:~:text=You%20probably%20wouldn't%20think,creature%20dates%20back%20many%20centuries.
    guess7 = input ('The Dragon is Scotlands nation animal.\n \
    T or F\n ')
    checkguess (guess7, 'F')
    print ('The unicornn is.\n')

    #https://www.nationalgeographic.com/animals/article/weird-laws-nation-dogs-ferrets-bigfoot
    guess8 = input ('It is illegal to hunt bigfoot in Washington State.\n \
    T or F\n ')
    checkguess (guess8, 'T')

    #https://www.rabbies.com/en/blog/dragon-everything-you-need-know-about-welsh-national-animal#:~:text=The%20Dragon%3A%20Everything%20You%20Need%20to%20Know%20About%20the%20Welsh%20National%20Animal&text=The%20red%20dragon%2C%20or%20%E2%80%9CY,animal%20for%20thousands%20of%20years.
    guess9 = input ('The dragon is the national animal of Wales.\n \
    T or F\n ')
    checkguess (guess9, 'T')

    #https://mytopglobal.com/countries-with-the-most-pyramids/
    guess10 = input ('Egypt has the most pyramids in the world.\n \
    T or F\n ')
    checkguess (guess10, 'F')
    print ('Sudan has 255 pyramids while Egypt has 138.\n')

    #https://www.rd.com/article/letter-not-in-any-state-name/#:~:text=Got%20your%20guess%3F,dropped%20out%20of%20our%20alphabet.)
    guess11 = input ("The letter 'Z' doesn\'t appear in any U.S state. \n \
    T or F\n ")
    checkguess (guess11, 'F')
    print ('Arizona has Z but no U.S state has the letter Q.\n')

    #https://en.wikipedia.org/wiki/Beefalo#:~:text=Beefalo%20constitute%20a%20hybrid%20offspring,both%20animals%20for%20beef%20production.
    guess12 = input ('Gruffalo is a cross of a cow and bison called.\n \
    T or F\n ')
    checkguess (guess12, 'F')
    print ('A beefalo is a cross between the two, a Gruffalo is from the book "The Gruffalo" by  Axel Scheffler.\n')

    #https://www.britannica.com/topic/number-sign
    guess13 = input ('Octothorpe is the actual name of the # symbol.\n \
    T or F\n ')
    checkguess (guess13, 'T') 

    #https://www.nsf.gov/news/news_images.jsp?cntn_id=115564&org=NSF#:~:text=As%20bananas%20age%2C%20the%20chlorophyll,in%20studying%20programmed%20cell%20death.
    guess14= input ('Bananas glow green under black light.\n \
    T or F\n ')
    checkguess (guess14, 'f')
    print ('They glow blue due to the chlorophyll in the peels breaking down FCC particles.\n')

    #https://www.smithsonianmag.com/arts-culture/why-the-tomato-was-feared-in-europe-for-more-than-200-years-863735/#:~:text=In%20the%20late%201700s%2C%20a,were%20high%20in%20lead%20content.
    guess15 = input ('Europeans were scared of eating tomatoes when they were introduced.\n \
    T or F\n ')
    checkguess (guess15, 'T')
    print ('It\'s part of the nightshade family and the eurpeans belived it would kill you')

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
TorF()