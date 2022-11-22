class Battle:
    _player = None
    _opponent = None
    _turn = 0
    _critical_hit_change = 0.05

    def __init__(self):
        pass

    def clear_battlefield(self):
        self._player = None
        self._opponent = None
        self._turn = 0

    def set_players(self, player, opponent):
        self._player = player
        self._opponent = opponent

    def start_battle(self):
        # Determine the starter
        self.set_starter()
        # If the user -> ask for move, otherwise do this automatically

    def print_battle(self):
        pass

    def user_attack(self):
        pass

    def computer_attack(self):
        pass

    def calculate_damage(self):
        pass

    def set_starter(self):
        if self._player.get_speed() >= self._opponent.get_speed():
            self._turn = 0
        self._turn = 1

    def play_turn(self):
        # Check who should play, either do a move automatically or wait for user input
        pass

    def switch_turn(self):
        # Toggle between 0 and 1
        self._turn = (self.turn + 1) % 2

    def calculate_damage(self):
        # Use a max() to make sure we don't return a negative damage
        return max(0, self._player.get_attack() * 2 - self._opponent.get_defense())

    def is_finished(self):
        return self._player.get_health() == 0 or self._opponent.get_health() == 0

    def get_winner(self):
        if self._player.get_health() == 0:
            return self._player.get_name()
        return self._opponent.get_name()
