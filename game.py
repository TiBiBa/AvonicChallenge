import random
import csv
from battle import Battle
from pokemon import Pokemon


class Game:
    _pokemons = []
    _battle = None
    _user_pokemon = None
    _opponent_pokemon = None

    def __init__(self):
        self.initialize_pokemon()
        self._battle = Battle()

    def initialize_pokemon(self):
        with open('pokemon.csv', mode='r') as file:
            content = csv.DictReader(file, delimiter=';')
            for pokemon in content:
                self.add_pokemon(pokemon)

    def add_pokemon(self, data):
        # All data is provided as a strings -> cast the relevant values to an int
        try:
            health = int(data.get('health'))
            attack = int(data.get('attack'))
            defense = int(data.get('defense'))
            speed = int(data.get('speed'))
        except ValueError:
            print("One or more of your input values in invalid!")
            print(f"The issue occurs at the following Pokémon: {data.get('name')}")
            exit(1)
        pokemon = Pokemon(data.get('name'), data.get('type'), health, attack, defense, speed)
        self._pokemons.append(pokemon)

    def select_pokemon(self):
        self.list_pokemons()
        choice = input("Which Pokémon would you like to choice? ")
        try:
            choice = int(choice)
            if choice < 1 or choice > len(self._pokemons):
                print("This index is invalid, try again!")
                self.select_pokemon()
            else:
                # We use the -1 to make sure the Pokémons listed start with 1. instead of 0.
                self._user_pokemon = self._pokemons[choice-1]
        except ValueError:
            print("This index is invalid, try again!")
            self.select_pokemon()

    def get_selected_pokemon(self):
        return self._user_pokemon if self._user_pokemon else "You haven't selected a Pokémon yet!"

    def list_pokemons(self):
        index = 1
        for pokemon in self._pokemons:
            print(f"{index} - {pokemon.get_name()}")
            index += 1

    def start_battle(self):
        self.randomize_opponent()
        self._battle.clear_battlefield()
        self._battle.set_players(self._user_pokemon, self._opponent_pokemon)
        while not self._battle.is_finished():
            self._battle.play_turn()

    def randomize_opponent(self):
        self._opponent_pokemon = self._pokemons[random.randint(0, len(self._pokemons))]
        if self._opponent_pokemon == self._user_pokemon:
            self.randomize_opponent()
