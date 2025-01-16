import random

def generateGoal() :
    goal = random.randint(1, 18)
    return goal

def rollDice() :
    diceVal = random.randint(1, 6)
    return diceVal

def gameStart() :
    print("Your target number is: " + str(generateGoal()))
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