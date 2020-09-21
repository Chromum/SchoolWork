import random



randomNumber = 0
usedGuesses = 0


oopieDoopie = int(input("What is the maximum number you want"))



def PickNumer(poop):
    global randomNumber
    randomNumber = random.randint(1,poop)

PickNumer(oopieDoopie)

while(usedGuesses < 6):
    playerGuess = int(input("What number you guess \n"))


    print("Your Guess Was " , playerGuess)



    if(playerGuess == randomNumber):
         print("You get a point!")
         PickNumer(oopieDoopie)

    else:
        print("You got it wrong")

    usedGuesses += 1

print("Thanks for playing")
    

    
 
