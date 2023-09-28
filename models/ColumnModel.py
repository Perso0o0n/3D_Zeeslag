# column
# name
# bool is er schip
# bool is op geschoten
import json
import random

class ColumnModel:
    def __init__(self, Id, isSol = False, isMaw = False):
        self.Id = Id
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
            return "YOU"
        elif self.isVisited:
            return self.shortName
        else:
            return self.Id + " "

    def __repr__(self) -> str:
        if self.isPlayerposition:
            return "YOU"
        elif self.isVisited:
            return self.shortName
        else:
            return self.Id + " "
    
