class Move:
    _name = ""
    _damage = 0
    _accuracy = 0

    def __init__(self, name: str, damage: int, accuracy: int):
        self._name = name
        self._damage = damage
        self._accuracy = accuracy

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage

    def get_accuracy(self):
        return self._accuracy
