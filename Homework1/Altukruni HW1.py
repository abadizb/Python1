# Altukruni Abdulhalim
# Python programming
# Homework1
#09/12/2014
import random
no = "no"
yes = "yes"
while True:
    Name = input ("Hi, what is your name? ")
    print("Hello " + Name + " lets play a game")
    print("Think of a random number from 1 to 100, and i will guess it!")
    input ("you ready? ")
    print ("is it larger than 50")
    answer = input("yes or no ?: ")
    if answer == no:
        count = 1
        
        while answer == no:
            count +=1
            x = random.randint(1, 50)
            print("is it ", (x))
            answer = input("yes or no ? : ")
        else:
            print ("you win!!!")
            print ("you have tried", count, "times!" )
            playagain = input ("Do you want to play again?: yes or no ")
            if playagain == no:
                print ("Good bye")
                break
            else:
                continue
            
    if answer == yes:
        count = 1
        answer = input("yes or no ?: ")
        while answer == no:
            count +=1
            x = random.randint(51, 100)
            print("is it ", (x))
            answer = input("yes or no ? : ")
        else:
            print ("you win!!!")
            print ("you have tried", count, "times!" )
            playagain = input ("Do you want to play again?: yes or no ")
            if playagain == no:
                print ("Good bye")
                break
            else:
                continue
 
