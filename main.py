from game import Game
from utils import VALID_MENU_OPTIONS


def initialize_game():
    game = Game()


def start_menu():
    print("Welcome, to Pokemon!")
    print("Select one of the following options:\n")

    print("(a) Select a Pokemon")
    print("(s) Start the fight")
    print("(d) List all Pokemons")
    print("(q) Quit")

    choice = input("What would you like to do?: ")
    if choice not in VALID_MENU_OPTIONS:
        print("You made an invalid choice, try again!\n\n")
        return start_menu()
    else:
        if choice == 'q':
            print("Thanks for playing!")
            exit(1)
        else:
            print("Still working on this...")


if __name__ == "__main__":
    initialize_game()
    start_menu()
