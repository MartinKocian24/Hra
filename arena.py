from kouzelnik import Wizard
class Arena:

    def __init__(self, fighter_1, fighter_2, cube):
        self._fighter_1 = fighter_1
        self._fighter_2 = fighter_2
        self._cube = cube

    def _draw_arena(self):
        # zakomentováno kvůli kompileru
        # self._vycisti_obrazovku()
        self._clear_screen()
        print("-------------- Aréna -------------- \n")
        print("Bojovníci: \n")
        self._print_fighter(self._fighter_1)
        self._print_fighter(self._fighter_2)

    def _clear_screen(self):
        import os as _os
        _os.system('cls' if _os.name == 'nt' else 'clear')

    def _print_message(self, message):
        import time as _time
        print(message)
        _time.sleep(0.75)

    def start_battle(self):
        import random as _random
        print("Vítejte v aréně!")
        print(f"Dnes se utkají {self._fighter_1} a {self._fighter_2}!")
        print("Zápas může začít...", end=" ")
        input()

        if _random.randint(0, 1):
            (self._fighter_1, self._fighter_2) = (self._fighter_2, self._fighter_1) #pokud padlo True, prohodi se bojovnici
        while self._fighter_1.alive() and self._fighter_2.alive():
            self._fighter_1.offense(self._fighter_2)
            self._draw_arena()
            self._print_message(self._fighter_1.last_message())
            self._print_message(self._fighter_2.last_message())
            self._fighter_2.offense(self._fighter_1)
            self._draw_arena()
            self._print_message(self._fighter_2.last_message())
            self._print_message(self._fighter_1.last_message())

    def _print_fighter(self, fighter):
        print(fighter)
        print(f"Život: {fighter.graphic_health()}")
        if isinstance(fighter, Wizard):
            print(f"Mana: {fighter.graphic_mana()}")