"""
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
"""