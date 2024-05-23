import subprocess

try:
    import tkinter as tk
except ImportError:
    # if module is not installed, it will be automatically installed
    subprocess.check_call(["pip", "install", 'tkinter'])
    import tkinter as tk

try:
    from tkcalendar import DateEntry
except ImportError:
    subprocess.check_call(["pip", "install", 'tkcalendar'])
    from tkcalendar import DateEntry

try:
    from datetime import datetime as date
except ImportError:
    subprocess.check_call(["pip", "install", 'datetime'])
    from datetime import datetime as date

from View.DataFrame import DataFrame
from View.GamesFrame import GamesFrame
from View.InfoFrame import InfoFrame

class MainWindow(tk.Tk):
    def __init__(self, model, fileAdmind):
        super().__init__()
        self.model = model    
        self.fileAdmind = fileAdmind
        self.title(self.model.getName())
        self.geometry("1000x800")
        self.resizable(False, False)
        # self.configure(background="yellow")
        self.mainmenu = tk.Menu(self)
        self.config(menu=self.mainmenu)

        self.playersMenu = tk.Menu(self.mainmenu)
        self.playersMenuRefresh()
        self.mainmenu.add_cascade(label="Change Player", menu=self.playersMenu)

        self.authorsMenu = tk.Menu(self.mainmenu, tearoff=0)
        self.authorsMenu.add_command(label="Author Manager", command=lambda: self.manageAuthors())
        self.authorsMenu.add_command(label="Game Manager", command=lambda: self.manageGames())
        self.mainmenu.add_cascade(label="Manage Lists", menu=self.authorsMenu)

        self.dataFrame = DataFrame(parent=self)
        self.dataFrame.pack(side=tk.LEFT, fill="both")

        self.gamesFrame = GamesFrame(parent=self)
        self.gamesFrame.pack(side=tk.TOP, fill="both", expand=True)

        self.infoFrame = InfoFrame(parent=self)
        self.infoFrame.pack(side=tk.BOTTOM, fill="both")
        
    def getModel(self):
        return self.model
    
    def getFileAdmind(self):
        return self.fileAdmind
    
    def getMainMenu(self):
        return self.mainmenu
    
    def playersMenuRefresh(self):
        self.playersMenu.delete(0, "end")
        self.players = self.model.getCostumers()

        if self.players is not None and len(self.players) > 0:
            self.selectedPlayer = self.players[0]
            for player in self.players:
                self.playersMenu.add_command(label=player, command=lambda p=player:self.changePlayer(p))
        else: 
            self.selectedPlayer = None

        self.playersMenu.add_separator()
        self.playersMenu.add_command(label="+ New Player", command=self.addPlayer)
    
    def addPlayer(self):
        PlayerCreator(self)

    def changePlayer(self, player):
        self.selectedPlayer = player
        self.refresh()

    def createPlayer(self, player):
        self.model.addCostumer(player)
        # self.fileAdmind.dumpPlayer(player)
        self.changePlayer(player)
        self.playersMenuRefresh()
    
    def getSelectedPlayer(self):
        return self.selectedPlayer
    
    def changeToOwnedPage(self):
        self.gamesFrame.setDisplaySource("games")
        self.refresh()

    def changeToWishlistPage(self):
        self.gamesFrame.setDisplaySource("wishlist")
        self.refresh()

    def manageAuthors(self):
        AuthorCreator(self)
    
    def manageGames(self):
        GameCreator(self)
    
    def executeWindow(self):
        self.mainloop()

    def refresh(self):
        self.dataFrame.refresh()
        self.gamesFrame.refresh()
    
    def __repr__(self):
        return "MAINWINDOW"

class PlayerCreator(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Create new Player")
        # self.geometry("300x200")
        self.resizable(False, False)

        labelName = tk.Label(self, text="Name: ")
        self.entryName = tk.Entry(self)
        labelNickname = tk.Label(self, text="Nickname: ")
        self.entryNickname = tk.Entry(self)
        labelName.grid(row=0, column=0, padx=5, pady=5)
        labelNickname.grid(row=1, column=0, padx=5, pady=5)
        self.entryName.grid(row=0, column=1, padx=5, pady=5)
        self.entryNickname.grid(row=1, column=1, padx=5, pady=5)

        confirmButton = tk.Button(self, text="Confirm", command=self.on_confirm)
        confirmButton.grid(row=2, column=0, padx=10, pady=10)

    def on_confirm(self):
        from Model.Player import Player
        self.parent.createPlayer(player=Player(self.entryName.get(), self.entryNickname.get(), date.now().strftime("%Y"), [], []))
        self.destroy()

    def __repr__(self):
        return "PLAYERCREATOR"
    
class GameCreator(tk.Toplevel):
        def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent
            self.title("Add Game")
            self.resizable(False, False)
            vcmd = (self.register(self.callback))

            creationLabel = tk.Label(self, text="Create new Game")
            creationLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

            # **GAME CREATOR**
            # NAME
            labelName = tk.Label(self, text="Name: ")
            self.entryName = tk.Entry(self)
            # YEAR
            labelYear = tk.Label(self, text="Year: ")
            self.entryYear = tk.Entry(self, validate="all", validatecommand=(vcmd, "%P"))
            # AUTHORS
            labelAuthors = tk.Label(self, text="Authors: ")
            self.listboxAuthors = tk.Listbox(self, selectmode="multiple", exportselection=0)
            authorslist = parent.getModel().getAuthors()
            if len(authorslist) > 0:
                counter = 1
                for author in authorslist:
                    self.listboxAuthors.insert(counter, author)
            # # SINGLEPLAYER
            # self.varOfCheckSp = tk.IntVar()
            # self.checkSp = tk.Checkbutton(self, text="SinglePlayer", variable=self.varOfCheckSp, offvalue=0, onvalue=1)
            # NUMBER OF PLAYERS
            labelPlayers = tk.Label(self, text="Players: ")
            labelMin = tk.Label(self, text="Minimum: ")
            self.entryMin = tk.Entry(self, validate="all", validatecommand=(vcmd, "%P"))
            labelMax = tk.Label(self, text="Maximum: ")
            self.entryMax = tk.Entry(self, validate="all", validatecommand=(vcmd, "%P"))
            # TYPE OF GAME
            labelType = tk.Label(self, text="Type")
            self.listboxType = tk.Listbox(self, exportselection=0)
            typelist = self.parent.getModel().getGameTypes()
            if len(typelist) > 0:
                counter = 1
                for type in typelist:
                    self.listboxType.insert(counter, type)

            labelName.grid(row=1, column=0, padx=5, pady=5)
            self.entryName.grid(row=1, column=1, padx=5, pady=5)
            labelYear.grid(row=2, column=0, padx=5, pady=5)
            self.entryYear.grid(row=2, column=1, padx=5, pady=5)
            labelAuthors.grid(row=3, column=0, padx=5, pady=5)
            self.listboxAuthors.grid(row=4, column=0, padx=5, pady=5)
            # self.checkSp.grid(row=5, column=0, padx=5, pady=5)
            labelPlayers.grid(row=6, column=0, padx=5, pady=5)
            labelMin.grid(row=7, column=0, padx=5, pady=5)
            self.entryMin.grid(row=7, column=1, padx=5, pady=5)
            labelMax.grid(row=8, column=0, padx=5, pady=5)
            self.entryMax.grid(row=8, column=1, padx=5, pady=5)
            labelType.grid(row=9, column=0, padx=5, pady=5)
            self.listboxType.grid(row=10, column=0, padx=5, pady=5)
            confirmCreationButton = tk.Button(self, text="Confirm creation", command=self.confirmCreation)
            confirmCreationButton.grid(row=11, column=0, padx=10, pady=10)

        def callback(self, P):
            if str.isdigit(P) or P == "":
                return True
            else:
                return False
        
        def confirmCreation(self):
            authors = self.getAllSelectedElements(self.listboxAuthors)
            type = self.listboxType.get(self.listboxType.curselection())
            # print(type)
            # if type == ["'singleplayer'"]:
            if type == "singleplayer":
                singleplayer = True
                minPlayers = "1"
                maxPlayers = "1"
            else: 
                singleplayer = False
                minPlayers = self.entryMin.get()
                maxPlayers = self.entryMax.get()
            
            from Model.BoardGame import BoardGame
            game = BoardGame(name=self.entryName.get(), yearOfRelease=self.entryYear.get(), authors=authors, singleplayer=singleplayer, 
                                             minPlayers=minPlayers, maxPlayers=maxPlayers, type=type)
            self.parent.getModel().addBoardGame(game)
            for authorFullName in authors:
                author = self.parent.getModel().getAuthorByName(authorFullName)
                author.addGame(game)
            self.destroy()

        def getAllSelectedElements(self, listBox):
            selectedElements = []
            for element in listBox.curselection():
                selectedElements.append(listBox.get(element))
            return selectedElements

        def __repr__(self):
            return "GAMECREATOR"

class AuthorCreator(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.authorsList = parent.getModel().getAuthors()
        self.title("Manage the Authors")
        self.resizable(False, False)

        labelName = tk.Label(self, text="Name: ")
        self.entryName = tk.Entry(self)
        labelSurname = tk.Label(self, text="Surname: ")
        self.entrySurname = tk.Entry(self)
        labelBD = tk.Label(self, text="Bithdate: ")
        self.entryBD = DateEntry(self)
        labelBio = tk.Label(self, text="Biography: ")
        self.entryBio = tk.Text(self, width=50, height=10)

        labelName.grid(row=0, column=0, padx=5, pady=5)
        self.entryName.grid(row=0, column=1, padx=5, pady=5)
        labelSurname.grid(row=1, column=0, padx=5, pady=5)
        self.entrySurname.grid(row=1, column=1, padx=5, pady=5)
        labelBD.grid(row=2, column=0, padx=5, pady=5)
        self.entryBD.grid(row=2, column=1, padx=5, pady=5)
        labelBio.grid(row=3, column=0, padx=5, pady=5)
        self.entryBio.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        confirmButton = tk.Button(self, text="Confirm", command=lambda: self.addAuthor())
        confirmButton.grid(row=5, column=0, padx=10, pady=10)
    
    def addAuthor(self):
        from Model.Author import Author
        author = Author(name=self.entryName.get(), surname=self.entrySurname.get(), birthDate=self.entryBD.get(), 
                        biography=self.entryBio.get("1.0", "end-1c"), numberOfAwards=0, inventedGames={})
        self.parent.getModel().addAuthor(author)
        # self.parent.getFileAdmind().dumpAuthor(author)
        self.destroy()
    
    def __repr__(self):
        return "AUTHORCREATOR"