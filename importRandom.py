import random 
import os
num=random.randint(0,100)
guess=9
n=0
safaGar=lambda:os.system("cls")
while(True):
    if guess==0:
        safaGar()
        print("\n\nYou can't guess anything\n\nGO KILL YOURSELF!!!\n")
        print("In spite of losing if u wish to try again?\n(press y for yes and n for no)")
        x=input()
        safaGar()
        if(x=="y" or x=="Y"):
            safaGar()
            guess=9
            num=random.randint(0,100)
        elif(x=="n" or x=="N"): break
        else:
            #print("\n\nYou can only enter y or n")
            safaGar()
            input("\n\nStupid you should enter either y or n...\nI dont want to play with you\nPress enter to exit")
            break
    print("\nNumber of guess left=",guess)
    try:
        n=int(input("\nGuess a number within 0 to 99:\n"))
        safaGar()
        print("You have entered:->",n,"\n")
        if n<num:print("\nENTER A GREATER NUMBER!")
        elif n>num:print("\nENTER A SMALLER NUMBER!")
    except:
        safaGar()
        print("\n\nYou can enter integer only\nAs punishment you lose your one chance")
        
   
    guess-=1
    
    if n==num:
        safaGar()
        print("\n\nCongratulations you have guessed correctly\nnumber of attempt:",9-guess,"\nDo u want to play again?\n(press y for yes and n for no)")
        x=input()
        if(x=="y" or x=="Y"):
            safaGar()
            guess=9
            num=random.randint(0,100)
        elif(x=="n" or x=="N"): break
        else:
            safaGar()
            #print("\nYou can only enter y or n")
            input("\n\nDon't u have Sense?\n\nYou can only enter y or n\n\nNow press enter to exit")
            break