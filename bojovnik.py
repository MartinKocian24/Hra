class Fighter:

    def __init__(self, name, health, attack, defense, cube):
        self._name = name
        self._health = health
        self._max_health = health
        self._attack = attack
        self._defense = defense
        self._cube = cube
        self._message = ""

    def __str__(self):
        return str(self._name)

    def alive(self):
        return self._health > 0

    def graphic_pointer(self, current, maximal):
        together = 20          #urcuje celkovou delku života
        count = int(current / maximal * together)
        if count == 0 and self.alive():
            count = 1
        return f"[{'█'*count}{' '*(together-count)}]"

    def graphic_health(self):
        return self.graphic_pointer(self._health, self._max_health)

    def defend(self, hit):
        damage = hit - (self._defense + self._cube.roll())
        if damage > 0:
            message = f"{self._name} utrpěl poškození {damage} hp."
            self._health = self._health - damage
            if self._health < 0:
                self._health = 0
                message = f"{message [:-1]} a zemřel."
        else:
            message = f"{self._name} odrazil útok."
        self._set_message(message)

    def offense(self, opponent):
        hit = self._attack + self._cube.roll()
        message = f"{self._name} útočí s úderem za {hit} hp."
        self._set_message(message)
        opponent.defend(hit)

    def _set_message(self, message):
        self._message = message

    def last_message(self):
        return self._message