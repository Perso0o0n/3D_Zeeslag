# column
# name
# bool is er schip
# bool is op geschoten
import json
import random
from colorama import Fore

class ColumnModel:
    def __init__(self, Id, isSol = False, isMaw = False):
        self.Id = Id
        self.HasShop = isSol
        if isSol:
            self.name = "Sol"
            self.shortName = "SOL"
        elif isMaw:
            self.name = "Devils Maw"
            self.shortName = "MAW"
        else:
            #give star random name from json
            try:
                with open("stars.json","r") as file:
                    config = file.read()
                JsonConfig = json.loads(config)
            except Exception:
                print("failed to load the file")
            stars = JsonConfig["stars"]
            rand = random.randint(0,len(stars)-1)
            self.name = stars[rand]
            self.shortName = self.name[slice(3)]
        
        #set position
        self.isPlayerposition = isSol
        self.isVisited = isSol

    def __str__(self):
        if self.isPlayerposition:
            return Fore.LIGHTGREEN_EX + "YOU" + Fore.RESET
        elif self.isVisited:
            return Fore.LIGHTBLACK_EX + self.shortName  +  Fore.RESET
        else:
            return Fore.LIGHTBLACK_EX + self.Id + " " + Fore.RESET

    def __repr__(self) -> str:
        if self.isPlayerposition:
            return Fore.LIGHTGREEN_EX + "YOU" + Fore.RESET
        elif self.isVisited:
            return Fore.LIGHTBLACK_EX + self.shortName + Fore.RESET
        else:
            return  self.Id + " "
    
