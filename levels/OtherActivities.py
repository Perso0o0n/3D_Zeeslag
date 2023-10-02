import random
import time
from models.Player import Player
class OtherActivities:

    def randomGoodActivity(self,hasKey):
        randInt = random.randint(1,4)
        match randInt:
            case 1:
                return self.ALockedBox(hasKey)
            case 2:
                return self.FoundCanisterInSpace()
            case 3:
                return self.FoundTheEgg()
            case 4:
                return self.AShop()

    def randomNormalActivity(self):
        randInt = random.randint(1,4)
        match randInt:
            case 1:
                return self.BrokenShip()
            case 2:
                return self.maintenance()
            case 3:
                return self.BrokenShop()
            case 4:
                return self.DebreeField()

    def RandomBadActivity(self, difficulty):
        randInt = random.randint(1,4)
        match randInt:
            case 1:
                return self.Bomb(difficulty)
            case 2:
                return self.leach(difficulty)
            case 3:
                return self.Bandits(difficulty)
            case 4:
                return self.AngryShop()


    def FoundCanisterInSpace():
        item = "nothing"
        amount = 0
        match (random.randint(1,3)):
            case 1:
                item = "fuel"
                amount = 10 
            case 2:
                item = "ISC"
                amount = 50 
            case 3:
                item = "mistery key"
                amount += 1
        print(F"when entering in the system you bumped into a mysterious canister. \nafter further inspection you realize that this canister contains {item}.")
        if item != "nothing":
            print(F"+{amount} {item}")
        return item, amount
    @staticmethod
    def FoundTheEgg():
        print(F"one of the moons of this system also has a moon the size of 2 ships. It is always on the dark side of this moon, strange...")
        time.sleep(1)
        print("this moon-moon is actualy not a moon but some kind of egg.")
        while(True):
            take = input("shall take the egg with us for further research? (Y/N)")
            match take.upper():
                case "Y":
                    print("+1 mistery egg")
                    return "TheEgg", 1
                case "N":
                    print("we leave the egg alone!")
                    return "nothing", 0
                case _:
                    print("invalid input. (Y/N)")
    @staticmethod
    def BrokenShip():
        print("a ship is sinking into one of the gas giants. it seems to have no crew.")
        time.sleep(1)
        randInt = random.randint(1,3)
        while(True):
            take = input("rescue the ship, using one fuel? (Y/N)")
            match take.upper():
                case "Y":
                    print("-1 fuel")
                    if randInt == 1:
                        print("instead of saving the ship, we accidentally pushed it into the gas giant.")
                        return "fuel", -1
                    print("we saved the ship! it has enough fuel to refund the fuel we used in saving it.")
                    print("+1 ship")
                    return "ship", 1
                case "N":
                    print("we leave the egg alone!")
                    return "nothing", 0
                case _:
                    print("invalid input. (Y/N)")
    @staticmethod
    def DebreeField():
        print("this system has a debree field made up of broken spaceships.")
        randInt = random.randint(1,4)
        while(True):
            take = input("loot, the debree field? (Y/N)")
            match take.upper():
                case "Y":
                    if randInt == 1:
                        print("one of our ships crashed into a stray projectile and combusted instantly.")
                        print("-1 ship")
                        return "ship", -1
                    if randInt == 2:
                        print("afer a lot of searching we found nothing. everything is smashed to bits. we wasted some fuel.")
                        print("-2 fuel")
                        return "fuel", -2
                    if randInt == 3:
                        print("some fuel has been recovered from a wreckage.")
                        print("+1 fuel")
                        return "fuel", +1
                    if randInt == 4:
                        print("we found a ship that still functions!")
                        print("+1 ship")
                        return "ship", 1
                case "N":
                    print("we fly around the debree field!")
                    return "nothing", 0
                case _:
                    print("invalid input. (Y/N)")
    @staticmethod
    def ALockedBox(hasKey):
        print("our scanners pick up a small object in this system.")
        time.sleep(2)
        print("it seems to be a box with a lock on it.")
        if hasKey:
            while True:
                open = input("open the box. (Y/N)")
                match open.upper():
                    case "Y":
                        print("+100 ISC")
                        return "ISC", 100
                    case "N":
                        print("we leave.")
                        return "nothing", 0
                    case _:
                        print("invalid input. (Y/N)")
        print("but we dont have a key")
        return "nothing", 0
    @staticmethod
    def AShop():
        print("this system has a shop.")
        return "shop", 1
    @staticmethod
    def AngryShop():
        print("this system has a shop, it is only accessible to AAPP custumers.")
        return "shop", -1
    @staticmethod
    def BrokenShop():
        print("this system has a shop, but it seems wrecked")
        while True:
                open = input("fund the shop $30 milion to reopen? (Y/N)")
                match open.upper():
                    case "Y":
                        print("-30 ISC")
                        return "shop", 0
                    case "N":
                        print("we leave them to bankruptcy.")
                        return "nothing", 0
                    case _:
                        print("invalid input. (Y/N)")
    @staticmethod
    def Bomb(difficulty):
        print("this system is full of space mines.")
        randInt = random.randint(0,2+difficulty)
        print(F"we lost {randInt} ships, trying to get out of the minefield.")
        return "ship", randInt*-1
    @staticmethod
    def leach(difficulty):
        print("this system is full of fuel sucking space leaches.")
        randInt = random.randint(1+difficulty,4+difficulty)
        print(F"we lost {randInt} fuel, trying to exterminate the leaches.")
        return "fuel", randInt*-1
    @staticmethod
    def Bandits(difficulty):
        print("this system is full of pirates.")
        randInt = random.randint(10*difficulty,10 + 10*difficulty)
        print(F"we lost ${randInt} ISC, for our passage.")
        return "ISC", randInt*-1
    @staticmethod
    def maintenance():
        print("a ship is in need of some maintenance.")
        print("-$5 ISC")
        return "ISC", -5

