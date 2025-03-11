from  Python_Quiz_Program import *
from Multiple_choice_Python_Quiz_Program import *
from T_or_F_Python_Quiz_Program import *
from Simple import *
clear()
choice = int(input ('Enter a madlib to play:\
\n 1) Fill in blank .\n Mulitple choice.\n 3) True or false.\n'))

if choice == 1:
    main()
elif choice ==2:
    mulitple()
elif choice ==3:
    TorF()

