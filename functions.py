import random

def generateGoal() :
    goal = random.randint(1, 18)
    return goal

def rollDice() :
    diceVal = random.randint(1, 6)
    return diceVal

def gameStart(goal) :
    print("Your target number is: " + str(goal))
    dice = int(input("How many dice would you like to roll? (Max of 3 dice): "))
    print("You are rolling: " + str(dice) + " dice.")
    return playerRoll(dice)


def computerRoll() :
    rolls = random.randint(1, 3)
    print("Computer is rolling: " + str(rolls) + " dice.")
    computerScore = 0
    while rolls > 0 :
        computerScore = computerScore + rollDice()
        rolls = rolls - 1
    return computerScore

def playerRoll(dice):
    if 0 < dice <= 3 :
        playerScore = 0
        while dice > 0:
            playerScore = playerScore + rollDice()
            dice = dice - 1
        return playerScore
    
def win(playerScore, computerScore, goal):
    playerWins = 0
    computerWins = 0
    print("Computer score: " + str(computerScore))
    print("Player score: " + str(playerScore))
    if playerScore > goal :
        print("Bust! You lose!")
        computerWins = computerWins + 1
    elif computerScore > goal:
        print("Computer bust! You win!")
        playerWins = playerWins + 1
    elif playerScore > computerScore:
        print("You win!")
        playerWins = playerWins + 1
    else:
        print("You lose!")
        computerWins = computerWins + 1
    print("Player wins: " + str(playerWins))
    print("Computer wins: " + str(computerWins))
        