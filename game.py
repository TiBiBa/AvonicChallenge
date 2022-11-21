class Game:
    pokemons = {}

    def __init__(self):
        print("Initializing the game...")
        print("This is the complex part...")
        # We have to perform quite a few things here:
        # The game consist of pokemons, whereas the pokemons consists of their own data AND moves
        # The game can also "start" -> fight our selected pokemon against the randomly selected one

    def add_pokemon(self, pokemon):
        self.pokemons[pokemon.name] = pokemon

    def remove_pokemon(self, name):
        self.pokemons.pop(name)

    def list_pokemons(self):
        print(self.pokemons)
