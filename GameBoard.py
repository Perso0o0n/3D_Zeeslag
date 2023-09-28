from models.ColumnModel import ColumnModel
from models.RowModel import RowModel
from models.Player import Player
import time
import os
from colorama import Fore

class GameBoard:
    def __init__(self,dificulty):
        #create board with a length scaled by the difficulty. 
        self.length = dificulty * 3
        self.width = dificulty * 3
        self.player = Player(5)
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
            if(inputwidth == self.player.playerAtWidth and inputlength == self.player.playerAtLength):
                print("you are already there.")
                return False
            if((inputlength < self.player.playerAtLength -1 or inputlength > self.player.playerAtLength +1)
               or (inputwidth < self.player.playerAtWidth -1 or inputwidth > self.player.playerAtWidth +1)):
                print("you can only fly to adjacent stars")
                return False
            return True
        return False

    def Travel(self,userInput):
        # consume fuel
        if(not(self.player.fly())):
            print("out of fuel!")
            return False
        
        # where to go
        inputlength = ord(userInput[0]) - 65
        inputwidth = int(userInput[1])

        #move
        isVisited = self.map[inputlength].GetVisited(inputwidth)
        name = self.map[inputlength].GetStarName(inputwidth)
        self.movePlayer(inputlength,inputwidth)
        os.system('cls')

        # activity
        self.returnMap()
        if(isVisited):
            #shop???
            print(F"welcome back to {name}")
            if(self.map[inputlength].HasShop):
                pass
        else:
            #minigame
            print(F"welcome to {name}")
        input("press enter to move.")
        return True

        

    def movePlayer(self,inputlength,inputwidth):
        
        self.map[self.player.playerAtLength].removePlayer(self.player.playerAtWidth)
        self.map[inputlength].addPlayer(inputwidth)
        self.player.playerAtLength = inputlength
        self.player.playerAtWidth = inputwidth
        return

            