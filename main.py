from models import RowModel


def isValidInput(userInput, chosen_locations):
  #check if the input of the user is valid
  invalid_letters = ("klmnopqrstuvwxyz")
  
  if userInput[0].lower() in invalid_letters or userInput.isdigit(
  ) or userInput.isalpha() or not(userInput[1].isdigit()) or len(userInput) != 2:
    return False
  elif userInput in chosen_locations:
    print(str(p1_ships[-2] + str(p1_ships[-1]) + " already chosen "))
    return False

  else:
    return True

chosen_p1_locations = []

row = RowModel.RowModel("A",2)
print(row.Name)

width = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
length = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

p1_ships = input("Where do you want your ships? ")
p1_locations = p1_ships.split(", ")
for ShipLocation in p1_locations:
  if isValidInput(ShipLocation, chosen_p1_locations):
    chosen_p1_locations.append(ShipLocation)
  else:
    print("Invalid Input")
  





