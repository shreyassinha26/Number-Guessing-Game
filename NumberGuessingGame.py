import random
win=False
num=0
rand=random.randrange(0,101)
guesses=0

while(guesses<7 and win==False):
    guesses+=1
    user=int(input("Enter a random number between 0 and 100   "))
    enter=False
    while(enter==False):
        if(user<101 and user >=0):
            enter=True
        else:
           user=int(input("Enter an integer number between 0 and 100   "))
    if(user==rand):
        win = True
        print("Correct you win")
    elif(user>rand):
        print("Too high guess a lesser number")
    else:
        print("Too low guess a greater number") 

if(win==False):
    print("Too many guesses you lose")