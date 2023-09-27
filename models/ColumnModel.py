# column
# name
# bool is er schip
# bool is op geschoten


class ColumnModel:
    def __init__(self, Id, isSol = False):
        self.Id = Id
        if isSol:
            self.name = "Sol"
            self.shortName = "SOL"
        else:
            self.name = "unknown"
            self.shortName = "IDK"
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
    
