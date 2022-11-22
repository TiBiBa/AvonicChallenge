import copy
import random
from pokemon import Pokemon


class Battle:
    _player = None
    _opponent = None
    _turn = 0
    _mis_change = 0.05
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
        print("********************************************************************")
        self.print_health_bar(self._player)
        self.print_health_bar(self._opponent)
        print("********************************************************************")

    def print_health_bar(self, pokemon: Pokemon):
        print(pokemon.get_name())
        if pokemon.get_health() > 0:
            remaining_health = round((pokemon.get_health() / pokemon.get_health()) * 40)
        else:
            remaining_health = 0
        print(f"[{'=' * remaining_health}{'-' * (40 - remaining_health)}] {pokemon.get_health()}/{pokemon.get_max_health()}")

    def user_attack(self):
        self._player.list_moves()
        attack = input("What move do you want to use? ")
        self.attack(self._player, self._opponent)

    def computer_attack(self):
        self.attack(self._opponent, self._player)

    def set_starter(self):
        if self._player.get_speed() >= self._opponent.get_speed():
            self._turn = 0
        else:
            self._turn = 1

    def play_turn(self):
        # We print the battle before each move
        self.print_battle()
        if self._turn == 0:
            print("It is your turn to attack!")
            self.user_attack()
        else:
            print("It is the computers turn to attack!")
            self.computer_attack()
        self.switch_turn()

    def switch_turn(self):
        # Toggle between 0 and 1
        self._turn = (self._turn + 1) % 2

    def attack(self, attacker: Pokemon, defender: Pokemon):
        base_damage = attacker.get_attack() * 2 - defender.get_defense()
        if random.random() <= self._mis_change:
            damage = 0
        else:
            damage = base_damage * 2 if random.random() <= self._critical_hit_change else base_damage
        damage = max(0, damage)
        if damage > 0:
            defender.take_damage(damage)
        else:
            print("Your attack missed or didn't do any damage!")

    def is_finished(self):
        return self._player.get_health() == 0 or self._opponent.get_health() == 0

    def get_winner(self):
        if self._player.get_health() == 0:
            return self._player.get_name()
        return self._opponent.get_name()

    def show_conclusion(self):
        print("The game is finished!")
        self.print_battle()
