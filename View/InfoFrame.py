import tkinter as tk

class InfoFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.game = None
        self.config(borderwidth=2, relief="solid")

        self.nameLabel = tk.Label(self, font=("Times New Roman", 15))
        self.authorsLabel = tk.Label(self, font=("Times New Roman", 15))
        self.playersLabel = tk.Label(self, font=("Times New Roman", 15))
        self.typeLabel = tk.Label(self, font=("Times New Roman", 15))

        self.noGameLabel = tk.Label(self, text="Select a game to display info",  font=("Times New Roman", 35))

        self.noGameLabel.pack()

    placed = False
    def showInfo(self, game):
        self.nameLabel.config(text=f"Name: {game.getName()}")
        authors = "Authors: "
        for author in game.getAuthors():
            authors = authors + f"{author}, "
        authors = authors[:len(authors) - 2]
        self.authorsLabel.config(text=authors)
        self.authorsLabel.bind("<Button-1>", lambda event: self.onLabelClick(game))
        players = f"Players: {game.getMinPlayers()} - {game.getMaxPlayers()}"
        self.playersLabel.config(text=players)
        self.typeLabel.config(text=f"Type of game: {game.getType()}")

        if not self.placed:
            self.placeComponents()

    def placeComponents(self):
        self.noGameLabel.destroy()
        # profilePicture.pack(side="top", padx=10, pady=10)    
        self.nameLabel.pack(side="top", padx=10, pady=10, anchor='w')
        self.authorsLabel.pack(side="top", padx=10, pady=10, anchor='w')
        self.playersLabel.pack(side="top", padx=10, pady=10, anchor='w')
        self.typeLabel.pack(side="top", padx=10, pady=10, anchor='w')
        self.placed = True

    def onLabelClick(self, game):
        for authorFullName in game.getAuthors():
            author = self.parent.getModel().getAuthorByName(authorFullName)
            AuthorDisplayer(self, author)

class AuthorDisplayer(tk.Toplevel):
    def __init__(self, parent, author):
        super().__init__(parent)
        self.parent = parent
        # name, surname, birthDate, biography, numberOfAwards
        nameLabel = tk.Label(self, text= f"{author.getName()} {author.getSurname()}")
        bdLabel = tk.Label(self, text=author.getBirthDate())
        # bioText = tk.Text(self)
        # bioText.insert(tk.END, author.getBiography())
        bioText = tk.Label(self, text=author.getBiography(), wraplength=300)
        awardsLabel = tk.Label(self, text=f"{author.getNumberOfAwards()} awards")

        # creating a table
        tableGames = tk.Listbox(self)
        gamesList = author.getInventedGames()
        if gamesList:
            counter = 0
            for game in gamesList:
                tableGames.insert(counter, f"{game} = {gamesList[game]}")
                counter = counter + 1
        else:
            tableGames.insert(0, "No invented games")
        tableGames.config(state=tk.DISABLED)
        nameLabel.pack(side=tk.TOP, padx=5, pady=5)
        bdLabel.pack(side=tk.TOP, padx=5, pady=5)
        bioText.pack(side=tk.TOP, padx=5, pady=5)
        awardsLabel.pack(side=tk.TOP, padx=5, pady=5)
        tableGames.pack(side=tk.TOP, padx=5, pady=5)
