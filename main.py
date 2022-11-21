validoptions = ['a', 's', 'd', 'q']


def initializegame():
    print("Pokemon is being loaded...")


def startmenu():
    print("Welcome, to Pokemon!")
    print("Select one of the following options:\n")

    print("(a) Select a Pokemon")
    print("(s) Start the fight")
    print("(d) List all Pokemons")
    print("(q) Quit")

    choice = input("What would you like to do?: ")
    if choice not in validoptions:
        print("You made an invalid choice, try again!\n\n")
        return startmenu()
    else:
        if choice == 'q':
            print("Thanks for playing!")
            exit(1)
        else:
            print("Still working on this...")

if __name__ == "__main__":
    initializegame()
    startmenu()
