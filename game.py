import random
from battle import Battle


class Game:
    pokemons = []
    user_pokemon = None
    opponent_pokemon = None

    def __init__(self):
        pass
        # We have to perform quite a few things here:
        # The game consist of Pokémons, whereas the Pokémons consists of their own data AND moves
        # The game can also "start" -> fight our selected Pokémon against the randomly selected one

    def initialize_pokemon(self):
        pass
        # Get all Pokémon, store into list

    def select_pokemon(self):
        self.list_pokemons()
        choice = input("\nWhich Pokémon would you like to choice? ")
        try:
            choice = int(choice)
            if choice < 0 or choice > len(self.pokemons):
                print("This index is invalid, try again!")
                self.select_pokemon()
            else:
                self.user_pokemon = choice
        except ValueError:
            print("This index is invalid, try again!")
            self.select_pokemon()

    def get_selected_pokemon(self):
        return self.user_pokemon if self.user_pokemon else "You haven't selected a Pokémon yet!"

    def list_pokemons(self):
        print(self.pokemons)

    def start_battle(self):
        self.randomize_opponent()
        battle = Battle(self.pokemons[self.user_pokemon], self.pokemons[self.opponent_pokemon])
        while not battle.is_finished():
            battle.play_turn()

    def randomize_opponent(self):
        self.opponent_pokemon = random.randint(0, len(self.pokemons))
        if self.opponent_pokemon == self.user_pokemon:
            self.randomize_opponent()
