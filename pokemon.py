class Pokemon:
    _name = ""
    _category = ""  # Fixme: either add support for type calculation or remove this variable
    _max_health = 0
    _health = 0
    _attack = 0
    _defense = 0
    _speed = 0

    def __init__(self, name: str, category: str, health: int, attack: int, defense: int, speed: int):
        self._name = name
        self._category = category
        self._max_health = self._health = health  # Set both equal to health -> reduce _health only in Battle
        self._attack = attack
        self._defense = defense
        self._speed = speed

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def get_max_health(self):
        return self._max_health

    def get_attack(self):
        return self._attack

    def get_defense(self):
        return self._defense

    def get_speed(self):
        return self._speed

    def list_moves(self):
        # Todo: This is hard-coded for now, would be nice to use the Move class for this
        print("(a) - Tackle")
