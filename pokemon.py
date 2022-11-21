class Pokemon:
    _name = ""
    _type = ""
    _health = 0
    _attack = 0
    _defense = 0
    _speed = 0

    def __init__(self, name, type, health, attack, defense, speed):
        self._name = name
        self._type = type
        self._health = health
        self._attack = attack
        self._defense = defense
        self._speed = speed

    def get_name(self):
        return self._name

    def get_stats(self):
        return {'health': self._health, 'attack': self._attack, 'defense': self._defense, 'speed': self._speed}

    def get_health(self):
        return self._health

    def get_attack(self):
        return self._attack

    def get_defense(self):
        return self._defense

    def get_speed(self):
        return self._speed
