class Pokemon:
    _name = ""
    _category = ""
    _moves = []
    _level = 50
    _max_health = 0
    _health = 0
    _attack = 0
    _defense = 0
    _speed = 0

    def __init__(self, name: str, category: str, moves: list, health: int, attack: int, defense: int, speed: int):
        self._name = name
        self._category = category
        self._moves = moves
        self._level = 50
        self._max_health = (self._health) = health
        self._attack = attack
        self._defense = defense
        self._speed = speed

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_health(self):
        return self._health

    def get_max_health(self):
        return self._max_health

    def take_damage(self, damage: int):
        self._health = max(0, self._health - damage)

    def get_attack(self):
        return self._attack

    def get_defense(self):
        return self._defense

    def get_speed(self):
        return self._speed

    def get_move(self, index):
        return self._moves[index-1]

    def get_moves(self):
        return self._moves

    def list_moves(self):
        index = 1
        for move in self._moves:
            print(f"[{index}] - {move.get_name()}")
            index += 1
