# ODD OR EVEN GAME...

import random

def inputCheck():
    while True:
        try:
            user_input = int(input("\nEnter a number between 1 and 10: "))
            if 1 <= user_input <= 10:
                return user_input
            else:
                print("\tInvalid number! Enter a number between 1 and 10.")
        except ValueError:
            print("\tInvalid input! Please enter a valid input...")

def batting():
    print("Batting starts...")
    score=0
    computerscore=0
  
    while True:
        computerr=random.randint(1,10)
        userr=inputCheck()
        print("Computer:",computerr)
        score=score+userr
        print(f"Batting score of user is {score}")
 
        if userr==computerr:
            print("\nUser have been Bowled !")
            print(f"\tComputer need {score+1} to win.\n")
            print("User's turn to bowl...\n")
            while True:
                
                userr=inputCheck()
                computerr=random.randint(1,10)
                print("Computer:",computerr)
                computerscore=computerscore+computerr
                print(f"Total batting score of Computer is {computerscore}")

                if computerr==userr :
                    print("Computer have been bowled.")
                    print("\n\tUser Wins !")
                    exit()
                elif computerscore>score:
                    print("\n\tComputer Wins !")
                    exit()
                elif computerr==user and computerscore==score:
                    print("\n\tMatch is Tie !")    
                    exit()

def bowling():
    print("Bowling starts...")
    score=0
    computerscore=0
    
    while True:
        computerr=random.randint(1,10)
        userr=inputCheck()
        print("Computer:",computerr)
        computerscore=computerscore+computerr
        print(f"Batting score of Computer is {computerscore}")
 
        if computerr==userr:
            print("Computer have been Bowled !")
            print(f"\tUser need {computerscore+1} to win.\n")
            print("User's turn to bat...\n")
            while True:
                
                userr=inputCheck()
                computerr=random.randint(1,10)
                print("User:",userr)
                score=score+userr
                print(f"Total batting score of User is {score}")

                if userr==computerr :
                    print("\nUser have been bowled.")
                    print("\n\tComputer Wins !")
                    exit()
                elif score>computerscore:
                    print("\n\tUser Wins !")
                    exit()
                elif userr==computerr and score==computerscore:
                    print("\n\tMatch is Tie !")
                    exit()

user=int(input("Enter a number between 1-6 for toss: "))
toss=input("Choose \"odd\" or \"even\": ")
if user>=7 or user<=0:
    print("Invalid number!")
computer=random.randint(1,6)
print("Computer choose:",computer)

if toss.lower()=="even":
    if (user+computer)%2==0:
        print("\tYou have won toss!")
        call=input("\nChoose \"bat\" or \"ball\": ")
        if call.lower()=="bat":
            batting()
        elif call.lower()=="ball":
            bowling()
        else:
            print("\tInvalid input!")
    else:
        print("\tComputer won the toss!")
        computerchoose=random.choice(["bat","ball"])
        if computerchoose=="bat":
            print("\tComputer choose to bat first")
            bowling()
        else:
            print("\tComputer choose to ball")
            batting()
elif toss.lower()=="odd":
    if (user+computer)%2!=0:
        print("\tYou have won toss!")
        call=input("\nChoose \"bat\" or \"ball\": ")
        if call.lower()=="bat":
            batting()
        elif call.lower()=="ball":
            bowling()
        else:
            print("\tInvalid input!")
    else:
        print("\tComputer won the toss!")
        computerchoose=random.choice(["bat","ball"])
        if computerchoose=="bat":
            print("\tComputer choose to bat first")
            bowling()
        else:
            print("\tComputer choose to ball")
            batting()
            