from GameBoard import GameBoard
import os
import time
import winsound


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
    moveTo = input("where do you want to move to? (? for help, Q for quit): ")
    if(moveTo == "Q"):
        gameInProgress = False
        print("You pressed a big red and shiny button.")
        time.sleep(1.5)
        print("Surely this has no negative concequenses?")
        time.sleep(2.25)
        print("right???")
        time.sleep(2.5)
        #boom
        winsound.Beep(1000,2000)
        time.sleep(1.25)
        print("You lost!")
    elif(moveTo == "?"):
        input("good luck >:)")
    elif(gameBoard.isValidInput(moveTo)):
        gameInProgress = gameBoard.movePlayer(moveTo)
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
