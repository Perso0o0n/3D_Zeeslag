from models.ColumnModel import ColumnModel
from models.RowModel import RowModel
import time

class GameBoard:
    def __init__(self,dificulty):
        #create board with a length scaled by the difficulty. 
        self.length = dificulty * 3
        self.width = dificulty * 3
        self.playerPosition = 'A0'
        AddMap = []
        for i in range(0, self.length + 1):
            AddMap.append(RowModel(f"{chr(65 + i)}", self.width))
        self.map = AddMap

    def returnMap(self):
        print(str(self.map).replace("], [", "\n").replace("[[", "").replace("]]", ""))

    def isValidInput(self, userInput):
    # check if the input of the user is valid
        userInput = str(userInput)
        if len(userInput) != 2:
            print("input to long.")
            time.sleep(3)
            return False
        if(userInput[0].isalpha() and userInput[1].isdigit()):
            inputlength = ord(userInput[0])
            inputwidth = int(userInput[1])
            if(inputlength < 0 or inputlength > self.length or inputlength < 0 or inputwidth > self.width):
                print("length or width to long/short")
                time.sleep(3)
                return False
            if(userInput == self.playerPosition):
                print("you are already there.")
                time.sleep(3)
                return False
            #while()
            