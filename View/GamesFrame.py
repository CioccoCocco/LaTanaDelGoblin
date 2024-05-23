import tkinter as tk
from View.GamePanel import GamePanel

class GamesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, height=600)
        self.parent = parent
        # self.config(background="red")
        self.config(borderwidth=2, relief="solid")
        self.source = "games"

        self.player = None
        self.changePlayer()

        self.displayGames()

        gameAdder = tk.Button(self, text="+", command=lambda: self.newGame())
        gameAdder.grid(row=9, column=6)
            
    def changePlayer(self):
        self.player = self.parent.getSelectedPlayer()

    def setDisplaySource(self, source):
        self.source = source

    def getProperList(self):
        if self.source == "games":
            return self.player.getGames()
        else:
            return self.player.getFuturePurchases()
    
    def displayGames(self):
        if self.player is not None:
            # games = self.player.getGames()
            games = self.getProperList()

            gamesNumber = len(games)
            self.columnsNumber = 5
            self.rowsNumber = (int)(gamesNumber / self.columnsNumber) + 1 # 5 games each row (or 5 columns)
            # print(rowsNumber)

            self.columnconfigure(self.columnsNumber, weight=1)
            self.rowconfigure(self.rowsNumber+1, weight=1)

            column = 0
            row = 0
            for game in games:
                gamePanel = GamePanel(self, game)
                gamePanel.grid(row=row, column=column, padx=5, pady=5)
                column = (column + 1) % self.columnsNumber
                if column == 0:
                    row = row + 1

    def removeGameFromPlayer(self, game):
        if self.source == "games":    
            self.player.removeGame(game)
        else:
            self.player.removeFuturePurchase(game)

    def clear(self):
        for widget in self.winfo_children():
            if isinstance(widget, GamePanel):
                widget.destroy()

    def refresh(self):
        self.changePlayer()
        self.clear()
        self.displayGames()

    def newGame(self):
        GameCreator(self)

    def addGame(self, game):
        if self.source == "games":    
            self.player.addGame(game)
            if self.player.want(game):
                # this is needed because 'game' and 'removableGame' are completely identical, but are different instances of BoardGame
                # so I can't remove 'game', but I have to find the right instance which has the same name
                removableGame = self.player.getFuturePurchaseByName(game.getName())
                self.player.removeFuturePurchase(removableGame)
        else:
            self.player.addFuturePurchase(game)
        self.displayGames()

    def playerOwns(self, game):
        return self.player.own(game)
    
    def playerWants(self, game):
        return self.player.want(game)

    def __repr__(self):
        return "GAMESFRAME"
    
class GameCreator(tk.Toplevel):
        def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent
            self.title("Add Game")
            self.resizable(False, False)

            selectionLabel = tk.Label(self, text="Select a game")
            selectionLabel.grid(row=0, column=3, padx=10, pady=10)

            # **GAME SELECTOR**
            labelSelector = tk.Label(self, text="Games List")
            self.listboxGames = tk.Listbox(self, selectmode="multiple")
            gamesList = parent.parent.getModel().getBoardGames()
            # print(gamesList)
            if len(gamesList) > 0:
                counter = 1
                for game in gamesList:
                    if (not parent.playerOwns(game) and parent.source == "games") or ((not (parent.playerWants(game) or parent.playerOwns(game))) and parent.source == "wishlist"):
                        self.listboxGames.insert(counter, game)
            labelSelector.grid(row=1, column=3, padx=5, pady=5)
            self.listboxGames.grid(row=2, rowspan=3, column=3, padx=5, pady=5)
            confirmAdditionButton = tk.Button(self, text="Confirm addition", command=self.confirmAddition)
            confirmAdditionButton.grid(row=11, column=3, padx=10, pady=10)
        
        def confirmAddition(self):
            gamesNames = self.getAllSelectedElements(self.listboxGames)
            for gameName in gamesNames:
                game = self.parent.parent.getModel().getGameByName(gameName)
                self.parent.addGame(game)
            self.destroy()

        def getAllSelectedElements(self, listBox):
            selectedElements = []
            for element in listBox.curselection():
                selectedElements.append(listBox.get(element))
            return selectedElements

        def __repr__(self):
            return "GAMECREATOR"