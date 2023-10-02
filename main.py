from GameBoard import GameBoard
from levels.MovieGuesser import movie_guesser
import os
import time
import winsound
from colorama import Fore



#start the game
gameInProgress = True
input(
    "welcome to spaceslag (press enter to continue)"
)

#select difficulty
valid_input = False
while not(valid_input):
    difficulty = input("choose difficulty (1,2,3): ")
    if(difficulty.isdigit() and len(difficulty) == 1):
        if(int(difficulty) <= 3 and int(difficulty) >= 1):
            valid_input = True
            gameBoard = GameBoard(int(difficulty))         

#run the game
while(gameInProgress):
    os.system('cls')
    gameBoard.returnMap()
    gameBoard.printStats()
    moveTo = input("where do you want to move to? (? for help, Q for quit): ")
    if(moveTo.upper() == "Q"):
        gameInProgress = False
        print("You pressed a big red and shiny button.")
        time.sleep(1.5)
        print("Surely this has no negative consequences?")
        time.sleep(2.25)
        print("right???")
        time.sleep(2.5)
        #boom
        winsound.Beep(1000,2000) # piep
        #winsound.MessageBeep(-1)# bleeb
        time.sleep(1.25)
        print("You lost!")
    elif(moveTo == "?"):
        print("your goal is to reach the 'devils maw', a black hole that needs to be discovered.")
        time.sleep(0.5)
        print("this maw is in the oposite side of 'sol', the system the earth resides in.")
        time.sleep(0.5)
        print("(in 'sol' there will always be a shop!)")
        time.sleep(0.5)
        print("you can move by typing the coördinates of the star you want to visit, but you can only move to adjacent stars. (sol is A0)")
        time.sleep(0.5)
        print("moving uses fuel equal to your ships/lives. on the way you can lose or gain ships and fuel.")
        time.sleep(0.5)
        print("good luck!")
        input("(press enter to continue)")
    elif(gameBoard.isValidInput(moveTo)):
        gameInProgress = gameBoard.Travel(moveTo)
    else:
        input(F"{moveTo} is not a valid input")

# valid_input = False

# while not valid_input:
#     p1_ships = input("Where do you want your ships? ")
#     p1_locations = p1_ships.split(", ")

#     for ShipLocation in p1_locations:
#         if isValidInput(ShipLocation, chosen_p1_locations):
#             chosen_p1_locations.append(ShipLocation)
#             valid_input = True

#         else:
#             print("Invalid Input")
#             valid_input = False
#             break

#     if valid_input:
#         print("Valid Input")
