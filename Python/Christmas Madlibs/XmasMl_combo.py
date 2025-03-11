from Selecting_a_tree import *
from Cool_It_Madlib_BW import *
from Christmas_madlib import *
from THE_LODGE_madlib_EF import *
from Simple import *


choice = input ('Enter a madlib to play \n \
1) Selecting a Tree\n 2)Cool It madlib \n 3)Decorate! madlib \n 4)The Lodege madlib \n')

if choice == ('1'):
    S_A_t()
elif choice == ('2'):
    C_I()
elif  choice == ('3'):
    decorate()
elif choice == ('4'):
    T_L()
else:
    clear()