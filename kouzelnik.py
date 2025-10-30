from bojovnik import Fighter
class Wizard(Fighter):

    def __init__(self, name, health, attack, defense, cube, mana, magical_attack):
        super().__init__(name, health, attack, defense, cube)
        self._mana = mana
        self._max_mana = mana
        self._magical_attack = magical_attack

    def offense(self, opponent):
        #mana není naplnena
        if self._mana < self._max_mana:
            self._mana = self._mana + 10
            if self._mana > self._max_mana:
                self._mana = self._max_mana
            super().offense(opponent)
        #magický utok
        else:
            hit = self._magical_attack + self._cube.roll()
            message = f"{self._name} použil magii za {hit} hp."
            self._set_message(message)
            self._mana = 0
            opponent.defend(hit)

    def graphic_mana(self):
        return self.graphic_pointer(self._mana, self._max_mana)