class Pokemon:
    _name = ""
    _type = ""  # this should be a value of a fixed list of options -> Todo: What would be best to store this?
    _moves = []
    _health = 0
    _attack = 0
    _defense = 0
    _speed = 0

    def __init__(self):
        pass

    def set_stats(self, stats):
        pass
        # Set all stats on the current Pokémon

    def set_move(self, move):
        if len(self.moves) == 4:
            print("This pokemon already knows 4 moves, please remove one before you can add one!")
        else:
            print(move)
            print("Learning a move...")

    def get_moves(self):
        return self._moves

    def get_health(self):
        return self._health

    def get_attack(self):
        return self._attack

    def get_defense(self):
        return self._defense

    def get_speed(self):
        return self._speed
