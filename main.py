from game import Game

# A short overview for my own clarity:
# - We have a main, that contains a game
# - A game consist of Pokémons
# - A Pokémon consists of moves
# - A game can contain a Battle
# - A battle contains two Pokémons

class Main:
    valid_options = ['a', 's', 'd', 'q']

    def __init__(self):
        self.game = Game()
        self.menu()

    def menu(self):
        print("Welcome, to Pokémon!")
        print("Select one of the following options:\n")

        print("(a) Select a Pokémon")
        # We can only start a fight if we have already selected a Pokémon
        if self.game.get_selected_pokemon():
            print("(s) Start the fight")
        print("(d) List all Pokemons")
        print("(q) Quit")

        choice = input("\nWhat would you like to do? ")
        if choice not in self.valid_options:
            print("You made an invalid choice, try again!\n\n")
            return self.menu()
        else:
            if choice == 'a':
                self.game.select_pokemon()
            elif choice == 's':
                self.game.start_fight()
            elif choice == 'd':
                self.game.list_pokemons()
            else:
                print("Thanks for playing!")
                exit(1)


if __name__ == "__main__":
    main = Main()
