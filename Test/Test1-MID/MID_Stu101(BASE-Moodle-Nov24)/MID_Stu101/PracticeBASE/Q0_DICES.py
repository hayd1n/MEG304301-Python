# Q0_DICES.py
# StuID:_____   (revised: MEG304 2021Fall)
## TODO:  change this .py to a runnable jupyter notebook.
## GOAL:  Running 10-time(max.) games to get the sum of two-dices.
##        if the sum of the nth-trial is less than 6, then game over (Exit).
## 運行（最多）10次遊戲以獲得兩個骰子的總和。如果第n次試驗的總和小於6，則遊戲結束（退出）。

import random

x = random.randint(1,6)
y = random.randint(1,6)
roll = x + y

def diceTest(n):
    ## TODO: add "assert" to avoid inproper input parameter
    ## TODO: redesign it, a new function to "return" the sum of two dices.
    
    if n < 6 or n > 10:
        print("Error!! {0}:input 'n' should be 6~10 ".format(n))
        return 
    x = random.randint(1,n)
    y = random.randint(1,n)
    ## TODO: sum of  two dices.  change or redesign it with "return" its sum.
    roll = x + y
    ##TODO: print -- use different ways to print it out.
    print(f"\tDice: {n} faces for the result:{roll}={x}+{y}")
    ##  Return 

##  Add some necessary statements to make it as main() function
## 
# diceTest(7)
# diceTest(10)
# diceTest(21)