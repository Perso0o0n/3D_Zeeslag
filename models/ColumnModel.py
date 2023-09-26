# column
# name
# bool is er schip
# bool is op geschoten


class ColumnModel:
    def __init__(self, name):
        self.name = name
        self.IsHit = False
        self.IsShip = False

    def __str__(self):
        if self.IsHit and self.IsShip:
            return "X"
        elif self.IsHit:
            return "*"
        else:
            return self.name

    def __repr__(self) -> str:
        if self.IsHit and self.IsShip:
            return "X"
        elif self.IsHit:
            return "*"
        else:
            return self.name
