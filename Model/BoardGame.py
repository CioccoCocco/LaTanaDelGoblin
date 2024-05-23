class BoardGame():
    def __init__(self, name, yearOfRelease, authors, singleplayer, minPlayers, maxPlayers, type):
        self._name = name
        self._yearOfRelease = yearOfRelease
        self._authors = authors
        self._singleplayer = singleplayer
        self._minPlayers = minPlayers
        self._maxPlayers = maxPlayers
        self._type = type
    
    def getName(self):
        return self._name
    def getYearOfRelease(self):
        return self._yearOfRelease
    def getAuthors(self):
        return self._authors
    def isSinglePlayer(self):
        return self._singleplayer
    def getMinPlayers(self):
        return self._minPlayers
    def getMaxPlayers(self):
        return self._maxPlayers
    def getType(self):
        return self._type
    
    def setName(self, name):
        self._name = name
    def setYearOfRelease(self, yearOfRelease):
        self._yearOfRelease = yearOfRelease
    def setAuthors(self, authors):
        self._authors = authors
    def setSingleplayer(self, singleplayer):
        self._singleplayer = singleplayer
    def setMinPlayers(self, minPlayers):
        self._minPlayers = minPlayers
    def setMaxPlayers(self, maxPlayers):
        self._maxPlayers = maxPlayers
    def setType(self, type):
        self._type = type

    def __repr__(self) -> str:
        return self._name