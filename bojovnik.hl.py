from  bojovnik import Fighter
from  kostka import Cube
from arena import Arena
from mag import Wizard


cube = Cube(6)
fighter = Fighter("Spiderman", 100, 20, 10, cube)
gandalf = Wizard("Gandalf", 60, 18, 15, cube, 30, 45)
arena = Arena(fighter, gandalf, cube)

arena.start_battle()