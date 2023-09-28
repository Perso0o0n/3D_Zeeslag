from models.ColumnModel import ColumnModel
from models.RowModel import RowModel
import time
import os
from colorama import Fore

class GameBoard:
    def __init__(self,dificulty):
        #create board with a length scaled by the difficulty. 
        self.length = dificulty * 3
        self.width = dificulty * 3
        self.playerAtLength = 0
        self.playerAtWidth = 0
        self.map = []
        for i in range(0, self.length + 1):
            self.map.append(RowModel(f"{chr(65 + i)}", self.width))

    def returnMap(self):
        print(str(self.map).replace("], [", "]\n[").replace("[[", "[").replace("]]", "]"))

    def isValidInput(self, userInput):
    # check if the input of the user is valid
        userInput = str(userInput)
        if len(userInput) != 2:
            print("input to long/short.")
            return False
        elif(userInput[0].isalpha() and userInput[1].isdigit()):
            inputlength = ord(userInput[0]) - 65
            inputwidth = int(userInput[1])
            if(inputlength < 0 or inputlength > self.length or inputwidth < 0 or inputwidth > self.width):
                print("out of range")
                return False
            if(inputwidth == self.playerAtWidth and inputlength == self.playerAtLength):
                print("you are already there.")
                return False
            if((inputlength < self.playerAtLength -1 or inputlength > self.playerAtLength +1)
               or (inputwidth < self.playerAtWidth -1 or inputwidth > self.playerAtWidth +1)):
                print("you can only fly to adjacent stars")
                return False
            return True
        return False

    def Travel(self,userInput):
        inputlength = ord(userInput[0]) - 65
        inputwidth = int(userInput[1])
        isVisited = self.map[inputlength].GetVisited(inputwidth)
        name = self.map[inputlength].GetStarName(inputwidth)
        self.movePlayer(inputlength,inputwidth)
        os.system('cls')
        self.returnMap()
        if(isVisited):
            print(F"welcome back to {name}")
            #shop???
        else:
            print(F"welcome to {name}")
            #minigame
        input("press enter to move.")
        return True

        

    def movePlayer(self,inputlength,inputwidth):
        
        self.map[self.playerAtLength].removePlayer(self.playerAtWidth)
        self.map[inputlength].addPlayer(inputwidth)
        self.playerAtLength = inputlength
        self.playerAtWidth = inputwidth
        return

            