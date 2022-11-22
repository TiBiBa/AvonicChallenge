import copy


class Battle:
    _player = None
    _opponent = None
    _turn = 0
    _critical_hit_change = 0.05

    def __init__(self):
        pass

    def clear_battle(self):
        self._player = None
        self._opponent = None
        self._turn = 0

    def set_players(self, player, opponent):
        # We want to keep the original Pokémon data intact -> deepcopy the objects
        self._player = copy.deepcopy(player)
        self._opponent = copy.deepcopy(opponent)

    def start_battle(self):
        self.set_starter()
        self.play_turn()

    def print_battle(self):
        print("We printen de battle!")

    def user_attack(self):
        pass

    def computer_attack(self):
        pass

    def set_starter(self):
        if self._player.get_speed() >= self._opponent.get_speed():
            self._turn = 0
        self._turn = 1

    def play_turn(self):
        # We print the battle before each move
        self.print_battle()
        if self._turn == 0:
            self.user_attack()
        else:
            self.computer_attack()
        self.switch_turn()

    def switch_turn(self):
        # Toggle between 0 and 1
        self._turn = (self._turn + 1) % 2

    def calculate_damage(self):
        # Use a max() to make sure we don't return a negative damage
        return max(0, self._player.get_attack() * 2 - self._opponent.get_defense())

    def is_finished(self):
        return self._player.get_health() == 0 or self._opponent.get_health() == 0

    def get_winner(self):
        if self._player.get_health() == 0:
            return self._player.get_name()
        return self._opponent.get_name()

    def show_conclusion(self):
        pass
