
class Game:
    def __init__(self, type):
        self.gametype = type
        self.board = []
        for i in range(9):
            self.board.append([0,0,0,0,0,0,0,0,0])
        self.board[0][4] = 2
        self.board[8][4] = 1
        if type == 'PvP':
            player1 = Player(1)
            player2 = Player(2)
            self.players = [None, player1, player2 ]

    def make_turn(self, player_num, turn_type, point, way):
        if turn_type == 'move':
            if self.is_blocked(self, way, player_num) == False:
                self.players[player_num].make_move(point)
                return True
            return False
        elif turn_type == 'put':
            if self.board[point[0]][point[1]] == -1 or self.players[player_num].get_blocks() == 0:
                return False
            else:
                self.players[player_num].put_block()
                self.board[point[0]][point[1]] == -1
                return True



    def is_blocked(self, way, player_num):
        firtspos = self.players[player_num].get_pos()
        if way == 'up':
            if firtspos[0] == 0 or self.board[firtspos[0]-1][firtspos[1]] == -1:
                return True
            else:
                return False
        if way == 'down':
            if firtspos[0] == 8 or self.board[firtspos[0]+1][firtspos[1]] == -1:
                return True
            else:
                return False
        if way == 'left':
            if firtspos[1] == 0 or self.board[firtspos[0]][firtspos[1]-1] == -1:
                return True
            else:
                return False
        if way == 'right':
            if firtspos[1] == 8 or self.board[firtspos[0]][firtspos[1]+1] == -1:
                return True
            else:
                return False

class Player:
    def __init__(self,number):
        self.blocks = 10
        if number == 1:
            self.position = [8, 4]
        elif number == 2:
            self.position = [0, 4]

    def make_move(self, point):
        oldpos = self.position
        self.position = point

    def put_block(self):
        self.blocks -= 1

    def get_pos(self):
        return self.position

    def get_blocks(self):
        return self.blocks

class AI_noob:
    pass
