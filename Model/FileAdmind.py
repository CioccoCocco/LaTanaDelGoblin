import json
from Model.Author import Author
from Model.Player import Player
from Model.BoardGame import BoardGame

class FileAdmind():
    def __init__(self, model):
        self.playersFile = "players.json"
        self.authorsFile = "authors.json"
        self.gamesFile = "games.json"
        self.model = model  #this will be the gameshop, so I can interact with the lists
        
    def setPlayersFile(self, newName):
        self.playersFile = newName
    def setAuthorsFile(self, newName):
        self.authorsFile = newName
    def setGamesFile(self, newName):
        self.gamesFile = newName

    def getPlayersFile(self):
        return self.playersFile
    def getAuthorsFile(self):
        return self.authorsFile
    def getGamesFile(self):
        return self.gamesFile
    
    def jsonIntoGames(self, dictGames):
        games = []
        if len(dictGames) > 0:
            for gameData in dictGames:
                game = BoardGame(gameData['name'], gameData['yearOfRelease'], gameData['authors'], gameData['singleplayer'], 
                                 gameData['minPlayers'], gameData['maxPlayers'], gameData['type'])
                games.append(game)
        return games
    
    def loadPlayers(self):
        #loads the players from the playerFile into the GameShop
        playersDict = self.loadFile(self.playersFile)   #a dictionaire with ALL the players
        if len(playersDict) > 0:
            for player in playersDict:
                games = self.jsonIntoGames(player['games'])
                wishlist = self.jsonIntoGames(player['wishlist'])
                self.model.addCostumer(Player(player['name'], player['nickname'], player['subscriptionYear'], games, wishlist))
    
    def loadAuthors(self):
        #loads the authors from the authorsFile into the GameShop
        authorsDict = self.loadFile(self.authorsFile)   #a dictionaire with ALL the authors
        
        if len(authorsDict) > 0:
            for author in authorsDict:
                self.model.addAuthor(Author(author['name'], author['surname'], author['birthDate'], author['biography'], author['numberOfAwards'], author['inventedGames']))

    def loadGames(self):
        #loads the games from the gamesFile into the GameShop
        gamesDict = self.loadFile(self.gamesFile)   #a dictionaire with ALL the games
        
        if len(gamesDict) > 0:
            for game in gamesDict:
                self.model.addBoardGame(BoardGame(game['name'], game['yearOfRelease'], game['authors'], game['singleplayer'], 
                                                  game['minPlayers'], game['maxPlayers'], game['type']))

    def loadFile(self, fileName) -> dict:
        try:
            with open(fileName, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Il file '{fileName}' non esiste, quindi non verrà caricato nessun dato")
            return []

    def gameIntoJson(self, games):
        serializedGames = []
        if len(games) > 0:
            for game in games:
                gameData = {
                    'name': game.getName(),
                    'yearOfRelease': game.getYearOfRelease(),
                    'authors': game.getAuthors(),
                    'singleplayer': game.isSinglePlayer(),
                    'minPlayers': game.getMinPlayers(),
                    'maxPlayers': game.getMaxPlayers(),
                    'type': game.getType()
                }
                serializedGames.append(gameData)
        return serializedGames

    def dumpPlayers(self, players):
        playersData = []
        for player in players:
            playerData = {
                'name': player.getName(),
                'nickname': player.getNickname(),
                'subscriptionYear': player.getSubscriptionYear(),
                'games': self.gameIntoJson(player.getGames()),
                'wishlist': self.gameIntoJson(player.getFuturePurchases())
            }
            playersData.append(playerData)

        self.dumper(self.playersFile, playersData)
    
    def dumpAuthors(self, authors):
        authorsData = []
        for author in authors:
            authorData = {
                'name': author.getName(),
                'surname': author.getSurname(),
                'birthDate': author.getBirthDate(),
                'biography': author.getBiography(),
                'numberOfAwards': author.getNumberOfAwards(),
                'inventedGames': author.getInventedGames()
            }
            authorsData.append(authorData)

        self.dumper(self.authorsFile, authorsData)

    def dumpGames(self, games):
        gamesData = []
        for game in games:
            gameData = {
                'name': game.getName(),
                'yearOfRelease': game.getYearOfRelease(),
                'authors': game.getAuthors(),
                'singleplayer': game.isSinglePlayer(),
                'minPlayers': game.getMinPlayers(),
                'maxPlayers': game.getMaxPlayers(),
                'type': game.getType()
            }
            gamesData.append(gameData)

        self.dumper(self.gamesFile, gamesData)

    def dumper(self, fileName, data):
        with open(fileName, 'w') as file:
            json.dump(data, file)