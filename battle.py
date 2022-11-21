class Battle:
    _player = None
    _opponent = None
    _turn = 0
    finished = False

    def __init__(self, player, opponent):
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

    def is_finished(self):
        return self._player.get_health() == 0 or self._opponent.get_health() == 0

    def get_winner(self):
        if self._player.get_health() == 0:
            return self._player.get_name()
        return self._opponent.get_name()
