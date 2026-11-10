class GameCharacter:
    def __init__(self, name: str):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        """Read-only access to the character's name."""
        return self._name

    @property
    def health(self):
        """Returns the current health."""
        return self._health

    @health.setter
    def health(self, value):
        """Sets health, preventing it from dropping below 0 or exceeding 100."""
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def mana(self):
        """Returns the current mana."""
        return self._mana

    @mana.setter
    def mana(self, value):
        """Sets mana, preventing it from dropping below 0 or exceeding 50."""
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self):
        """Returns the character's current level."""
        return self._level

    def level_up(self):
        """Increases level by 1, resets vitals, and prints a success message."""
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        """Returns a formatted string of the character's stats."""
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"
