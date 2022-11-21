class Game:
    pokemons = {}
    # The user_pokemon should only contain a reference to the actual one -> the index number on the list
    # We have to keep a copy of both the user Pokémon and the opponent to make sure we can reduce stats etc.
    user_pokemon = None

    def __init__(self):
        pass
        # We have to perform quite a few things here:
        # The game consist of Pokémons, whereas the Pokémons consists of their own data AND moves
        # The game can also "start" -> fight our selected Pokémon against the randomly selected one

    def initialize_pokemon(self):
        pass
        # Get all Pokémon, store into list

    def select_pokemon(self):
        pass
        # list the Pokémons, wait for user input
        # If not valid: recursively call this function again

    def get_selected_pokemon(self):
        return self.user_pokemon

    def list_pokemons(self):
        print(self.pokemons)

    def start_battle(self):
        pass
        if not self.user_pokemon:
            print("You should not come here!")
            exit(1)
        # Select a random opponent that is DIFFERENT that our selection
        # Compare speed, start turn-by-turn game
