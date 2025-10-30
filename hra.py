from hraci import Location
class Game:

    castle = Location("Hrad", "Stojíš před bránou hradu, která je zřejmě jediným vchodem do pevnosti. Klíčová dírka je pokryta pavučinami, což vzbuzuje dojem, že je budova opuštěná.")
    first_forest = Location("Les", "Jsi na lesní cestě, která se sahá až za obzor, kde mizí ve stínu zapadajícího slunce.")
    crossroads_forest = Location("Lesní rozcestí", "Nacházíš se na lesním rozcestí.")
    third_forest = Location("Les", "Jsi na lesní cestě, která sahá až za obzor, kde mizí v siluetě zapadajícího slunce.")
    pond = Location("Rybník", "Došel jsi ke břehu malého rybníka. Hladina je jako zrcadlo. Kousek od tebe je dřevěná plošina se stavidlem.")
    fourth_forest = Location("Les", "Jsi na lesní cestě, která sahá až za obzor, kde mizí v siluetě zapadajícího slunce.")
    house = Location("Dům", "Stojíš před svým rodným domem, citíš vůni čerstvě nasekaného dřeva, která se line z hromady vedle vstupních dvěří.")

    # Propojeni lokaci
    castle.east = first_forest
    first_forest.west = castle
    first_forest.east = crossroads_forest
    crossroads_forest.west = first_forest
    crossroads_forest.east = third_forest
    crossroads_forest.south = fourth_forest
    third_forest.west = crossroads_forest
    third_forest.east = pond
    pond.west = third_forest
    fourth_forest.north = crossroads_forest
    fourth_forest.east = house
    house.west = fourth_forest
    # Ulozeni aktualni lokace
    current_location = house

    # Zpracuje prikaz
    def execute_command(self, command):
        command = command.lower()
        if command.startswith("jdi"):

            if command.endswith("sever") and self.current_location.north:
                self.current_location = self.current_location.north
            elif command.endswith("jih") and self.current_location.south:
                self.current_location = self.current_location.south
            elif command.endswith("západ") and self.current_location.west:
                self.current_location = self.current_location.west
            elif command.endswith("východ") and self.current_location.east:
                self.current_location = self.current_location.east
            else:
                print("Tímto směrem nelze jít.")

        elif command != "konec":
            print("Můj vstupní slovník neobsahuje tento příkaz.")

    def get_current_location(self):
        return self.current_location

#start of menu
game = Game()
command = ""

while command.lower() != "konec":
    print(game.get_current_location())
    print("Zadej příkaz: ", end="")
    command = input()
    game.execute_command(command)