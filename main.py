import random 
 # Rock, Paper & Scizzor game 

def gameW(comp, user): 
    if comp == user:
        return None  
    elif comp == "r":
        if user == "s":
            return False 
        elif user == "p":
            return True 
    elif comp == "s":
        if user == "p":
            return False 
        elif user == "r":
            return True 
    elif comp == "p":
        if user == "r":
            return False 
        elif user == "s":
            return True 


print("Computer's Turn.\n Options: 1. Rock(r) 2. Paper(p) 3. Scissors(s)")
print("***** ***** ***** ***** *****")
rand = random.randint(1, 3)
if rand == 1:
    comp = "r"
elif rand == 2:
    comp = "p"
elif rand == 3:
    comp = "s"

userInput = input("Your turn.\n Options: 1. Rock(r) 2. Paper(p) 3. Scissors(s)\n")
a = gameW(comp, userInput)

print(f"Computer picked {comp}")
print(f"You picked {userInput}")

if a == None:
    print("This round has resulted in a tie as you have matched comp's choice")
elif a:
    print("You have won this round!")
else:
    print("You have lost this round!")
