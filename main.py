from models.ColumnModel import ColumnModel
from models.RowModel import RowModel


def returnMap(map):
    print(str(map).replace("], [", "\n").replace("[[", "").replace("]]", ""))


def isValidInput(userInput, chosen_locations):
    # check if the input of the user is valid
    invalid_letters = "klmnopqrstuvwxyz"

    if (
        userInput[0].lower() in invalid_letters
        or userInput.isdigit()
        or userInput.isalpha()
        or not (userInput[1].isdigit())
        or len(userInput) != 2
    ):
        return False
    elif userInput in chosen_locations:
        print(str(p1_ships[-2] + str(p1_ships[-1]) + " already chosen "))
        return False
    else:
        return True


chosen_p1_locations = []

valid_input = False
length = int(input("give length"))
width = int(input("give width"))
map = []
for i in range(0, length):
    map.append(RowModel(f"{chr(65 + i)}", width))
returnMap(map)

valid_input = False

while not valid_input:
    p1_ships = input("Where do you want your ships? ")
    p1_locations = p1_ships.split(", ")

    for ShipLocation in p1_locations:
        if isValidInput(ShipLocation, chosen_p1_locations):
            chosen_p1_locations.append(ShipLocation)
            valid_input = True

        else:
            print("Invalid Input")
            valid_input = False
            break

    if valid_input:
        print("Valid Input")
