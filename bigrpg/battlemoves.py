class BattleMoves:
    def __init__(self,name,lowdamage,highdamage,accuracy,description,level):
        self.name = name
        self.lowdamage = lowdamage
        self.highdamage = highdamage
        self.accuracy = accuracy
        self.description = description
        self.level = level
    
    def getName(self):
        return self.name
    
    def getLowDamage(self):
        return self.lowdamage
    
    def getHighDamage(self):
        return self.highdamage
    
    def getAccuracy(self):
        return self.accuracy
    
    def getDescription(self):
        return self.description
    
    def getLevel(self):
        return self.level
