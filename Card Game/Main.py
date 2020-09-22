import pickle, time

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
    
    l = open(fileName, 'ab')
    data = pickle.load(l)
    temp = {}
    temp = data
    temp.append(dump)
    data = temp
    pickle.dump(data, l)

  
  
  


if(input("Are you a new user \n") == "Yes"):
  SignUp()
else:
  SignIn()

