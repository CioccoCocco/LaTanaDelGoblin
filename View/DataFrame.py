import tkinter as tk

class DataFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # mainmenu = tk.Menu(parent)
        # parent.config(menu=mainmenu)
        # self.config(background="blue")
        self.config(borderwidth=2, relief="solid")

        self.noPlayerFound = tk.Label(self, text="No Player\nwas found,\ncheck source file",  font=("Times New Roman", 35))

        self.nickname = tk.Label(self, font=("MV Boli", 25), borderwidth=1, relief="solid", padx=5, pady=5)
        self.name = tk.Label(self, font=("Times New Roman", 15))
        self.year = tk.Label(self, font=("Times New Roman", 15))
        self.ownedButton = tk.Button(self, text="Owned", command=self.changeToOwnedPage, state="disabled")
        self.wishlistButton = tk.Button(self, text="Wishlist", command=self.changeToWishlistPage)

        if self.parent.getSelectedPlayer() is not None: 
            self.selectedPlayer = self.parent.getSelectedPlayer()
            self.insertPlayer(self.selectedPlayer)
            self.placeComponents()
        else:
            self.noPlayerFound.pack(side="top")

    def changeToOwnedPage(self):
        self.parent.changeToOwnedPage()
        self.ownedButton.config(state="disabled")
        self.wishlistButton.config(state="active")

    def changeToWishlistPage(self):
        self.parent.changeToWishlistPage()
        self.ownedButton.config(state="active")
        self.wishlistButton.config(state="disabled")

    placed = False
    def insertPlayer(self, player):
        self.nickname.config(text=player.getNickname())
        self.name.config(text=player.getName())
        self.year.config(text=player.getSubscriptionYear())
        if not self.placed:
            self.placeComponents()

    def placeComponents(self):
        self.noPlayerFound.destroy() 
        self.nickname.pack(side="top", padx=10, pady=10)
        self.name.pack(side="top", padx=10, pady=10)
        self.year.pack(side="top", padx=10, pady=10)
        self.ownedButton.pack(side="top", padx=10, pady=10)
        self.wishlistButton.pack(side="top", padx=10, pady=10)
        self.placed = True

    def refresh(self):
        self.selectedPlayer = self.parent.getSelectedPlayer()
        self.insertPlayer(self.selectedPlayer)

    def __repr__(self):
        return "DATAFRAME"