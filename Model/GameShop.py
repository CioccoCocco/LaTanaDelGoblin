from Model.BoardGame import BoardGame
from Model.Player import Player
from Model.Author import Author

class GameShop():
    def __init__(self, name, owner):
        self._name = name
        self._owner = owner
        self._boardGames = []
        self._authors = []
        self._costumers = []

    def getName(self):
        return self._name
    def getOwner(self):
        return self._owner
    def getBoardGames(self):
        return self._boardGames
    def getCostumers(self):
        return self._costumers
    def getAuthors(self):
        return self._authors
    def getGameTypes(self):
        from Model.TypeOfGame import TypeOfGame
        return TypeOfGame.list()
    
    def setName(self, name):
        self._name = name
    def setOwner(self, owner):
        self._owner = owner
    def setBoardGames(self, boardGames):
        self._boardGames = boardGames
    def setCostumers(self, costumers):
        self._costumers = costumers
    def setAuthors(self, authors):
        self._authors = authors
    
    def addCostumer(self, costumer):
        if not self._costumers.__contains__(costumer):
            self._costumers.append(costumer)
    def addBoardGame(self, game):
        if not self._boardGames.__contains__(game):    
            self._boardGames.append(game)
    def addAuthor(self, author):
        if not self._authors.__contains__(author):
            self._authors.append(author)

    def removeCostumer(self, costumer):
        self._costumers.remove(costumer)
    def removeBoardGame(self, game):
        self._boardGames.remove(game)
    def removeAuthor(self, author):
        self._authors.remove(author)

    def generalRemove(self, element):
        if isinstance(element, BoardGame):
            self.removeBoardGame(element)
        elif isinstance(element, Author):
            self.removeAuthor(element)
        elif isinstance(element, Player):
            self.removeCostumer(element)
    
    def getCostumerByName(self, costumerName):
        for costumer in self._costumers:
            if( costumer.getName() == costumerName ):
                return costumer
    def getAuthorByName(self, authorFullName):
        for author in self._authors:
            if( author.__repr__() == authorFullName ):
                return author
    def getGameByName(self, gameName):
        for game in self._boardGames:
            if( game.getName() == gameName ):
                return game