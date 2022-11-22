import random
from battle import Battle


class Game:
    _pokemons = []
    _battle = None
    _user_pokemon = None
    _opponent_pokemon = None

    def __init__(self):
        self._battle = Battle()

    def initialize_pokemon(self):
        pass
        # Get all Pokémon, store into list

    def select_pokemon(self):
        self.list_pokemons()
        choice = input("\nWhich Pokémon would you like to choice? ")
        try:
            choice = int(choice)
            if choice < 0 or choice > len(self._pokemons):
                print("This index is invalid, try again!")
                self.select_pokemon()
            else:
                self._user_pokemon = self._pokemons[choice]
        except ValueError:
            print("This index is invalid, try again!")
            self.select_pokemon()

    def get_selected_pokemon(self):
        return self._user_pokemon if self._user_pokemon else "You haven't selected a Pokémon yet!"

    def list_pokemons(self):
        for index, pokemon in self._pokemons:
            print(f"[{index}] - {pokemon.get_name()}")

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
