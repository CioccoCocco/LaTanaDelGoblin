from enum import Enum

class TypeOfGame(Enum):
    COOP = "cooperative"
    SEMICOOP = "semi-cooperative"
    COMP = "competitive"
    SINGLEPLAYER = "singleplayer"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
    
    def getValue(self):
        return self.value