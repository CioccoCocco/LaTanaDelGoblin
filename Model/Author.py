class Author:
    def __init__(self, name, surname, birthDate, biography, numberOfAwards):
        self._name = name
        self._surname = surname
        self._birthDate = birthDate
        self._biography = biography
        self._numberOfAwards = numberOfAwards
        self._inventedGames = {}    # a dictionaire (or HashMap+)

    def __init__(self, name, surname, birthDate, biography, numberOfAwards, inventedGames):
        self._name = name
        self._surname = surname
        self._birthDate = birthDate
        self._biography = biography
        self._numberOfAwards = numberOfAwards
        self._inventedGames = inventedGames
    
    def getName(self):
        return self._name
    def getSurname(self):
        return self._surname
    def getBirthDate(self):
        return self._birthDate
    def getBiography(self):
        return self._biography
    def getNumberOfAwards(self):
        return self._numberOfAwards
    def getInventedGames(self):
        return self._inventedGames

    def setName(self, name):
        self._name = name
    def setSurname(self, surname):
        self._surname = surname
    def setBirthDate(self, birthDate):
        self._birthDate = birthDate
    def setBiography(self, biography):
        self._biography = biography
    def setNumberOfAwards(self, numberOfAwards):
        self._numberOfAwards = numberOfAwards
    def setInventedGames(self, inventedGames):
        self._inventedGames = inventedGames
    
    def addGame(self, game, awards = None):
        if awards is None:
            awards = 0
        self._inventedGames[game.getName()] = awards
    def removeGame(self, game):
        self._inventedGames.remove(game)
    def addAwardsForGame(self, game):
        self._inventedGames[game] += 1
        self._numberOfAwards += 1
    def addAwardsForGame(self, game, awards):
        self._inventedGames[game] += awards
        self._numberOfAwards += awards

    def __repr__(self):
        return f"{self._name} {self._surname}"