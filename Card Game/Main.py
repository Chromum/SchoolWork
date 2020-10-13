import pickle, time, os, random


fileName = "Credentials.txt"
credentialJson = {} 


def SignIn():
  print("Sign In")
  


def SignUp():
    global credentialJson, fileName
    print("What do you want your Username and Password to be")
    newUsername = input("New Username \n")
    newPassword = input("New Password \n")

    credentialJson = {
        "Username" : newUsername,
        "Password" : newPassword
    }
    
    dump = pickle.dumps(credentialJson)

##
##    if os.stat(fileName).st_size == 0:
##      Poo = open(fileName, "w"):
##      Poo.write(dump)
##    else:
##      p = open( fileName,"rb")
##      data = pickle.load(p)
##      temp = {}
##      temp = data
##      temp.append(dump)
##      data = temp
##      pickle.dump(data, l)



  
  
##  
##
##
##if(input("Are you a new user \n") == "Yes"):
##  SignUp()
##else:
##  SignIn()

#Game

def Play(player1Name, player2Name, Cards):
    print("Playing")
    player1CardNumRan = random.randint(0,len(Cards))
    player2CardNumRan = random.randint(0,len(Cards))

    player1Card = Cards[player1CardNumRan]
    player2Card = Cards[player2CardNumRan]

    
    player1CardColour = player1Card[0]
    player2CardColour = player2Card[0]

    player1CardNum = player1Card[1]
    player2CardNum = player2Card[1]



    print("Player 1 Card Colour:", player1CardColour, " | ", "Player 1 Card Num:",player1CardNum)
    print("Player 2 Card Colour:", player2CardColour," | ", "PLayer 2 Card Num:",player2CardNum)

    






#Game Setup

colours = ["red","yellow","black"]
maxCardNum = 10
Cards = []


def GameSetup(player1Name, player2Name):
    global colours, maxCardNum, Cards
    print("Setup")
    numOfCards = 30
    for i in range(0,numOfCards):
        pickedColour = random.choice(colours)
        pickedInt = random.randint(0,maxCardNum)
        Cards.append([pickedColour,pickedInt])
    Play(player1Name,player2Name,Cards)
    
        



#Temp Sign in system

def SignInSystem():
    player1Name = input("What is player ones name \n")
    player2Name = input("What is player twos name \n")


    if(player1Name != "" and player2Name != "" and player1Name != player2Name):
        GameSetup(player1Name,player2Name)
    else:
        print("Player Names are empty please enter a name OR your names are the same \n")
        SignInSystem()












SignInSystem()

