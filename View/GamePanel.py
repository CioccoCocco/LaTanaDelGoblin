import tkinter as tk

class GamePanel(tk.Frame):
    def __init__(self, parent, game):
        super().__init__(parent)
        self.parent = parent
        self.game = game    #the game that has to be displayed
        # self.config(background="purple")
        self.config(borderwidth=2, relief="solid")
        self.configure(height=600)

        # print(self.parent.__repr__())
        # print(self.info)

        gameName = tk.Label(self, text=game.getName(), font=("Times New Roman", 15))
        gameName.grid(row=1, column=0, columnspan=3)

        infoButton = tk.Button(self, text="Show Info", command=lambda: self.showInfo())
        infoButton.grid(row=0, column=0, columnspan=2)

        deleteButton = tk.Button(self, text="X", background="red", command=lambda: self.destroyGame())
        deleteButton.grid(row=0, column=2)

    def getGame(self):
        return self.game
    
    def showInfo(self):
        self.parent.parent.infoFrame.showInfo(self.game)
    
    def destroyGame(self):
        self.destroy()
        self.parent.removeGameFromPlayer(self.game)
        self.parent.refresh()

    def __repr__(self):
        return "GAMEPANEL"