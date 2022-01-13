
class Game:
    def __init__(self, type):
        self.gametype = type
        self.board = []
        for i in range(9):
            self.board.append([0,0,0,0,0,0,0,0,0])

class Player:
    pass

class AI(Player):
    pass
