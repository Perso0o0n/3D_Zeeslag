from models.ColumnModel import ColumnModel
from models.RowModel import RowModel
from models.Player import Player
from levels.wordle import wordle
from levels.MovieGuesser import movie_guesser
import time
import os
from colorama import Fore
import random
from levels.OtherActivities import OtherActivities

class GameBoard:
    def __init__(self,dificulty):
        #create board with a length scaled by the difficulty. 
        self.dificulty = dificulty
        self.length = dificulty * 3
        self.width = dificulty * 3
        self.player = Player(5,dificulty)
        self.map = []
        self.wordlewins = 0
        for i in range(0, self.length + 1):
            self.map.append(RowModel(f"{chr(65 + i)}", self.width))

    def returnMap(self):
        print(str(self.map).replace("], [", "]\n[").replace("[[", "[").replace("]]", "]"))

    def printStats(self):
        print(
            F" {self.player.fuel} units of fuel. \n",
            F"{self.player.ships} ships in your armada. \n",
            F"your bank account contains ${self.player.money} milion ISC"
        )

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
        
        #game end
        if name == "Devils Maw":
            print("You've reached your destination. ")
            return False
        
        #dragonquest
        if "Draconis" in name:
            print("the egg is hatching! seems like this system is a haching ground for dragons.")
            time.sleep(2)
            
            incorectinput = True
            while incorectinput:
                imp = input("the dragon hatchling wants to folow us. kill it? (Y/N)")
                match imp.upper():
                    case "Y":
                        incorectinput = False
                        print("you killed the poor thing. you monster.")
                        print("+100 ISC & +5 fuel")
                        self.player.fuel += 5
                        self.player.money += 100
                    case "N":
                        print("the dragon hatchlings needs a name...")
                        print("+1 ship & +3 fuel & dragon trophy")
                        self.player.fuel += 3
                        self.player.AddShips(1)
                        self.player.hasDragonTrophy = True
                    case _: 
                        print("Y or N u stupid.")

        # activity
        self.returnMap()
        if(isVisited):
            #shop???
            print(F"welcome back to {name}")
            if(self.map[inputlength].HasShop):
                self.shop(name)
        else:
            #minigame
            print(F"welcome to {name}")
            haswon = self.random_minigame(name)
        
        input("(press enter to move.)")
        return True

        

    def movePlayer(self,inputlength,inputwidth):
        
        self.map[self.player.playerAtLength].removePlayer(self.player.playerAtWidth)
        self.map[inputlength].addPlayer(inputwidth)
        self.player.playerAtLength = inputlength
        self.player.playerAtWidth = inputwidth
        return

    def shop(self,name):
        incorrectInput = True
        while(incorrectInput):
            userInput = input(F"{name} has a shop. enter? (Y/N)")           
            match userInput.upper():
                case "Y":
                    hasBoughtSomething = False
                    os.system("cls")
                    print("you enter the shop: ")
                    time.sleep(0.5)
                    while(incorrectInput):
                        print("wanna buy something?")
                        print(F"prices: \n\n1 unit of fuel: ${5*self.dificulty} milion ISC. (A)")
                        print(F"Fine spaceships: {11*self.dificulty} milion ISC per vessel. (B)")
                        print(F"All Access Platinum Pass AAPP: {20*self.dificulty} milion ISC. for your shopping convenience. (C)")
                        print(F"leave the shop. (D)")
                        print(F"your ISC: ${self.player.money} milion")
                        userInput = input("what will it be: ")
                        match userInput.upper():
                            case "A":
                                if self.player.BuyItem(5*self.dificulty):
                                    print("+1 unit of fuel")
                                    hasBoughtSomething = True
                                    self.player.fuel += 1
                                else:
                                    print("you are too poor")

                            case "B":
                                if self.player.BuyItem(11*self.dificulty):
                                    print("+1 ship")
                                    hasBoughtSomething = True
                                    self.player.AddShips(1)
                                else:
                                    print("you are too poor")

                            case "C":
                                if not(self.player.hasAAPP):
                                    if self.player.BuyItem(20*self.dificulty):
                                        hasBoughtSomething = True
                                        print("you got the legendary All Access Platinum Pass (AAPP)!")
                                        self.player.hasAAPP = True
                                    else:
                                        print("only the rich are allowed to carry an object of status so powerful as the AAPP! (not enough $)")
                                else: print("you already have the pass, valued customer.")

                            case "D":
                                #leave message
                                incorrectInput = False
                                if(hasBoughtSomething):
                                    os.system("cls")
                                    print("Until we meet again valued custumer!")
                                    if(self.player.hasAAPP):
                                        print(F"and some extra fuel for the way back for our AAPP customers! (+{self.player.ships} fuel)")
                                        self.player.fuel += self.player.ships
                                elif(not(self.player.hasAAPP)):
                                    print("not buying anything you poor ****? ")
                                print("have a nice day...")

                            case _:
                                input("that was not a valid input. (Y/N) (enter to continue)")
                        input("(enter to continue)")
                        os.system("cls")


                case "N":
                    return
                case _:
                    print("that was not a valid input. (Y/N)")
                    
                    
    def random_minigame(self, name):
        random_number = random.randint(0, 11 - self.dificulty)
        activity = OtherActivities()
        if random_number <= 3:
            #bad roll
            if random_number != 3:
                #random bad activity
                item, amount = activity.RandomBadActivity(difficulty= self.dificulty)
                return self.AddItemFromActivity(item, amount)

            else:
                #play wordle
                if not (wordle.play_wordle()):
                    #lost
                    self.wordlewins = 0
                    if not (self.player.RemoveShips(1)):
                        print("You are dead! ")
                        return False
                else:
                    #won
                    self.wordlewins += 1
                    if self.wordlewins == 3 and not (self.player.hasWordleTrophy):
                        print("You found the" + Fore.CYAN + " Wordle Master Trophy! " + Fore.RESET)
                        self.player.hasWordleTrophy = True

        elif random_number <= 6:
            # ok roll
            if random_number % 2 == 0:
                #random ok activity
                item, amount = activity.randomNormalActivity()
                return self.AddItemFromActivity(item, amount)
            else:
                #play wordle
                if not (wordle.play_wordle()):
                    #lost
                    self.wordlewins = 0
                    if not (self.player.RemoveShips(1)):
                        print("You are dead! ")
                        return False
                else:
                    #won
                    self.wordlewins += 1
                    if self.wordlewins == 3 and not (self.player.hasWordleTrophy):
                        print("You found the" + Fore.CYAN + " Wordle Master Trophy! " + Fore.RESET)
                        self.player.hasWordleTrophy = True
        else:
            # good roll
            if random_number % 2 == 0:
                # random good activity
                item, amount = activity.randomGoodActivity(self.player.hasKey)
                return self.AddItemFromActivity(item, amount)
            else:
                # movie guesser
                time.sleep(0.5)
                haswon, all_correct = movie_guesser.play_movie_guesser()
                if not (haswon):
                    if not (self.player.RemoveShips(1)):
                        print("You are dead! ")
                        return False
                elif all_correct:
                    self.player.hasMovieTrophy = True
    
    def AddItemFromActivity(self,item,amount):
        match item:
            case "ISC":
                self.player.money += amount
            case "ship":
                if not(self.player.RemoveShips(amount)):
                    print("you are dead. ")
                    return False
            case "fuel":
                self.player.fuel += amount
            case "mistery key":
                self.player.hasKey = True
            case "TheEgg":
                self.player.hasTheEgg
            case "shop":
                if amount == 0:
                    self.player.money -= 30
                    self.map[self.player.playerAtLength].BuyShop(self.player.playerAtWidth)
                    self.shop("saved enterprises")
                elif amount == 1:
                    
                    self.shop("new system")
                elif self.player.hasAAPP:
                    print("because we have an AAPP, we can enter.")
                    self.shop("AAPP enjoyers")
                else:
                    print("because we do not have a AAPP, the shopkeeper is aggressive and ctrl + alt + F4's a ship.")
                    if not(self.player.RemoveShips(1)):
                        print("you are dead. ")
                        return False

        return True