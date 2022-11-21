class Pokemon:

    moves = []
    stats = {}

    def __init__(self):
        pass

    def set_move(self, move):
        if len(self.moves) == 4:
            print("This pokemon already knows 4 moves, please remove one before you can add one!")
        else:
            print(move)
            print("Learning a move...")


    def remove_move(self, move):
        print(move)
        print("To-do...")
