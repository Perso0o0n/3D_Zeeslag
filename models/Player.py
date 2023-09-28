  
class Player:
    def __init__(self, ships, dificulty):
        self.ships = ships
        self.money = 75 + 25*dificulty
        self.playerAtLength = 0
        self.playerAtWidth = 0
        self.fuel = 35 + 15*dificulty
    
    def RemoveShips(self, amount):
        self.ships -= amount
        if self.ships < 1:
            return False
        return True
    
    def AddShips(self, amount):
        self.ships += amount
        if self.ships > 15:
            while self.ships > 15:
                self.ships -= 1
                self.money += 15
        return
    
    def BuyItem(self, price):
        if(self.money >= price):
            self.money -= price
            return True
        return False
    
    def fly(self):
        self.fuel -= self.ships
        if self.fuel < 0:
            return False
        return True
