from GameBoard import GameBoard
import os
import time


chosen_p1_locations = []

#select difficulty
valid_input = False
while not(valid_input):
    difficulty = input("choose difficulty (1,2,3): "))
    if(difficulty.isdigit() and len(difficulty) == 1):
        if(int(difficulty) <= 3 and int(difficulty) >= 1):
            valid_input = True
            gameBoard = GameBoard(int(difficulty))
            
#start the game
gameInProgress = True
print(
    "welcome to spaceslag"
)

#run the game
while(gameInProgress):
    os.system('cls')
    gameBoard.returnMap()
    moveTo = input("where do you want to move to? (? for help, Q for quit): ")
    if(moveTo == "Q"):
        gameInProgress = False
        print("U lost!")
        continue
    elif(moveTo == "?"):
        input("good luck >:)")
        continue
    elif(gameBoard.isValidInput(moveTo)):
        pass
    else:
        print(F"{moveTo} is not a valid input")
        time.sleep(2)
        continue

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
