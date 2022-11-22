import csv
from move import Move


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

    def __init__(self, name: str, category: str, health: int, attack: int, defense: int, speed: int):
        self._name = name
        self._category = category
        self._level = 50
        self._max_health = (self._health) = health
        self._attack = attack
        self._defense = defense
        self._speed = speed
        self.initialize_moves()

    def initialize_moves(self):
        self._moves = []
        with open("moves.csv", mode="r") as file:
            content = csv.DictReader(file, delimiter=";")
            for move in content:
                self.add_move(move)

    def add_move(self, data: dict):
        try:
            damage = int(data.get("damage"))
            accuracy = int(data.get("accuracy"))
        except ValueError:
            print("One or more of your input values in invalid!")
            print(f"The issue occurs at the following Move: {data.get('name')}")
            exit(1)
        move = Move(data.get("name"), damage, accuracy)
        self._moves.append(move)

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
