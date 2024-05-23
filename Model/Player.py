class Player:
    def __init__(self, name, nickname, subscriptionYear):
        self._name = name
        self._nickname = nickname
        self._subscriptionYear = subscriptionYear
        self._games = []
        self._future_purchases = []

    def __init__(self, name, nickname, subscriptionYear, games, future_purchases):
        self._name = name
        self._nickname = nickname
        self._subscriptionYear = subscriptionYear
        self._games = games
        self._future_purchases = future_purchases
    
    def getName(self):
        return self._name
    def getNickname(self):
        return self._nickname
    def getSubscriptionYear(self):
        return self._subscriptionYear
    def getGames(self):
        return self._games
    def getFuturePurchases(self):
        return self._future_purchases
    def getGameByName(self, name):
        for game in self._games:
            if game.getName() == name:
                return game
        return None
    def getFuturePurchaseByName(self, name):
        for game in self._future_purchases:
            if game.getName() == name:
                return game
        return None
    
    def setName(self, name):
        self._name = name
    def setNickname(self, nickname):
        self._nickname = nickname
    def setSubscriptionYear(self, subscriptionYear):
        self._subscriptionYear = subscriptionYear
    def setGames(self, games):
        self._games = games
    def setFuturePurchases(self, future_purchases):
        self._future_purchases = future_purchases
    
    def addGame(self, game):
        self._games.append(game)
    def addFuturePurchase(self, game):
        self._future_purchases.append(game)
    def removeGame(self, game):
        self._games.remove(game)
    def removeFuturePurchase(self, game):
        self._future_purchases.remove(game)

    def own(self, gameToCheck):
        for game in self._games:
            if game.getName() == gameToCheck.getName():
                return True
        return False
    def want(self, gameToCheck):
        for game in self._future_purchases:
            if game.getName() == gameToCheck.getName():
                return True
        return False

    def __repr__(self):
        return self._nickname