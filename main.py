from functions import *

goal = generateGoal()

playerScore = gameStart(goal)
computerScore = computerRoll()

win(playerScore, computerScore, goal)