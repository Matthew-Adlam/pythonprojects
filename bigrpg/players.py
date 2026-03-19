class Players:
    def __init__(self,name,level,health=100):
        self.name = name
        self.health = health
        self.level = level
    
    def adjustHealth(self,amount,adding):
        if adding:
            self.health+=amount
        else:
            self.health-=amount
        if self.health > 100:
            self.health = 100

    def printHealth(self):
        print(self.health)
    
    def getHealth(self):
        return self.health
    
    def getName(self):
        return self.name
    
    def getLevel(self):
        return self.level

        