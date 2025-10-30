class Cube:

    def __init__(self, number_of_walls=6):
        self.__number_of_walls = number_of_walls

    def sides(self):
        return self.__number_of_walls

    def roll(self):         #Vykoná hod kostkou a vrátí číslo od 1 do počtu stěn kostky
        import random as _random
        return _random.randint(1, self.__number_of_walls)

    def __str__(self):
        return str(f"Kostka s {self.__number_of_walls} stěnami.")
