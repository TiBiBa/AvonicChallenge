class Game:
    pokemons = {}
    user_pokemon = None

    def __init__(self):
        pass
        # We have to perform quite a few things here:
        # The game consist of pokemons, whereas the pokemons consists of their own data AND moves
        # The game can also "start" -> fight our selected pokemon against the randomly selected one

    def get_selected_pokemon(self):
        return self.user_pokemon

    def add_pokemon(self, pokemon):
        self.pokemons[pokemon.name] = pokemon

    def remove_pokemon(self, name):
        self.pokemons.pop(name)

    def list_pokemons(self):
        print(self.pokemons)
