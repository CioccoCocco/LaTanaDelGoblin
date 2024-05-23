from Model.GameShop import GameShop
from Model.FileAdmind import FileAdmind
from View.MainWindow import MainWindow

tanaDeiGoblin = GameShop("La Tana Dei Goblin Udine", "Zephyrus Edavane")

fileAdmind = FileAdmind(tanaDeiGoblin)
fileAdmind.loadAuthors()
fileAdmind.loadPlayers()
fileAdmind.loadGames()

mw = MainWindow(tanaDeiGoblin, fileAdmind)
mw.executeWindow()

print("Initiate dumping in files")
print("Dumping authors")
fileAdmind.dumpAuthors(tanaDeiGoblin.getAuthors())

print("Dumping games")
fileAdmind.dumpGames(tanaDeiGoblin.getBoardGames())

print("Dumping costumers")
fileAdmind.dumpPlayers(tanaDeiGoblin.getCostumers())