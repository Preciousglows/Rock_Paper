import random
print("Let's play, ROCK, PAPER SCISSORS!!!")
print("-----------------------------------")
possibleChoices =["R","P","S"]
tieScore = 0

def game(playerchoice,computerchoice):
    
    if(playerchoice =="R" and computerchoice =="P"):
        print("Sorry you lose :( ") 
    elif(playerchoice =="R" and computerchoice =="S"):
        print("Yay! You have won :)")
    elif(playerchoice =="S" and computerchoice =="P"):
        print("Yay! You have won :)")
    elif(playerchoice =="S" and computerchoice =="R"):
        print("Sorry you lose :( ")
    elif(playerchoice =="P" and computerchoice =="R"):
        print("Yay! You have won :)")
    elif(playerchoice =="P" and computerchoice =="S"):
        print("Sorry you lose :( ") 
    else:
        print("Oops!It's a tie,play again!")
        return "tie"


while(tieScore != "3"):
    while True:
     playerchoice= input("\nPick R for Rock, P for Paper,or S for Scissors:")
     if(playerchoice=="R" or playerchoice=="P" or playerchoice=="S"):
         break
     else:
         print("Invalid input. Try again!")
    
    computerchoice = random.choice(possibleChoices) 

    print("Player({0}):CPU({1})".format(playerchoice,computerchoice))
    result = game(playerchoice,computerchoice)
    if(result=="tie"):
        tieScore += 1
    else:
        break
print("Game Over!Thank You For Playing!!!")
  
         