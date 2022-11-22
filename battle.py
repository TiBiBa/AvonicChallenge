import copy
import random
from time import sleep

from move import Move
from pokemon import Pokemon


class Battle:
    _player = None
    _opponent = None
    _turn = 0
    _critical_hit_change = 0.05

    def __init__(self):
        pass

    def set_players(self, player: Pokemon, opponent: Pokemon):
        self._player = copy.deepcopy(player)
        self._opponent = copy.deepcopy(opponent)

    def start_battle(self):
        self.set_starter()
        print(f"You will be battling against {self._opponent.get_name()}, good luck!")
        self.play_turn()

    def print_battle(self):
        print("********************************************************************")
        self.print_health_bar(self._player)
        self.print_health_bar(self._opponent)
        print("********************************************************************\n")

    def print_health_bar(self, pokemon: Pokemon):
        print(f"{pokemon.get_name()} - lvl.{pokemon.get_level()}")
        if pokemon.get_health() > 0:
            remaining_health = round((pokemon.get_health() / pokemon.get_max_health()) * 40)
        else:
            remaining_health = 0
        print(f"[{'=' * remaining_health}{'_' * (40 - remaining_health)}] {pokemon.get_health()}/{pokemon.get_max_health()}")

    def user_attack(self):
        print("It is your turn to attack!")
        self._player.list_moves()
        move_index = input("What move do you want to use? ")
        try:
            move_index = int(move_index)
            if move_index < 1 or move_index > len(self._player.get_moves()):
                print("This move is invalid, try again!")
                self.user_attack()
            else:
                move = self._player.get_move(move_index)
                self.attack(move, self._player, self._opponent)
        except ValueError:
            print("This move is invalid, try again!")
            self.user_attack()

    def computer_attack(self):
        print("It is the opponents turn to attack!")
        sleep(2)
        move_index = random.randint(1, len(self._opponent.get_moves()))
        move = self._opponent.get_move(move_index)
        self.attack(move, self._opponent, self._player)

    def set_starter(self):
        if self._player.get_speed() >= self._opponent.get_speed():
            self._turn = 0
        else:
            self._turn = 1

    def play_turn(self):
        self.print_battle()
        if self._turn == 0:
            self.user_attack()
        else:
            self.computer_attack()
        self.switch_turn()

    def switch_turn(self):
        # Toggle between 0 and 1
        self._turn = (self._turn + 1) % 2

    # Loosely based on https://gamerant.com/pokemon-damage-calculation-help-guide/
    def calculate_damage(self, level: int, move_damage: int, accuracy: int, attack: int, defense: int):
        damage = 0
        if random.randint(0, 100) < accuracy:
            base_damage = ((((2 * level) / 5) + 2) * move_damage * (attack / defense) / 50) + 2
            damage = base_damage * 1.5 if random.random() <= self._critical_hit_change else base_damage
        return round(max(0, damage))

    def attack(self, move: Move, attacker: Pokemon, defender: Pokemon):
        damage = self.calculate_damage(attacker.get_level(), move.get_damage(), move.get_accuracy(), attacker.get_attack(), defender.get_defense())
        if damage > 0:
            defender.take_damage(damage)
            print(f"{attacker.get_name()} attacks with {move.get_name()} and does {damage} damage to {defender.get_name()}")
        else:
            print("Your attack missed or didn't do any damage!")

    def is_finished(self):
        return self._player.get_health() == 0 or self._opponent.get_health() == 0

    def _get_winner(self):
        if not self.is_finished():
            print("The game is not finished yet!")
            return
        if self._player.get_health() == 0:
            return self._opponent.get_name()
        return self._player.get_name()

    def show_conclusion(self):
        self.print_battle()
        print(f"And the winner is.... {self._get_winner()}")
