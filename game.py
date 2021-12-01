import random

letters =  list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


class Game():
    def __init__(self):
        self.grid = [ random.choice(letters) for i in range(9)]
    def is_valid(self, word):
        if not word:
            return False
        grid = self.grid.copy()
        for let in word:
            if let not in grid:
                return False
            grid.remove(let)
        return True


