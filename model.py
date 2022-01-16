import random
def minimum(arr, U):
    minim = 999999999
    pos = -1
    for i in range(len(arr)):
        if arr[i] < minim and arr[i] > -1 and arr[i] not in U:
            minim = arr[i]
            pos = i
    return pos

class Game:
    def __init__(self, type):
        self.gametype = type
        self.board = []
        for i in range(9):
            self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board[0][4] = 2
        self.board[8][4] = 1
        if type == 'PvP':
            player1 = Player(1)
            player2 = Player(2)
            self.players = [player1, player2]
        elif type == 'PvAIn':
            player1 = Player(1)
            player2 = AI_noob(2)
            self.players = [player1, player2]

    def make_turn(self, player_num, turn_type, point):
        if turn_type == 'move':
            ppos = []
            ppos.append(self.players[player_num].get_pos()[0])
            ppos.append(self.players[player_num].get_pos()[1])
            self.board[ppos[0]][ppos[1]] = 0
            self.players[player_num].make_move(point)
            self.board[point[0]][point[1]] = 1 if player_num == 0 else 2

        elif turn_type == 'put':
            self.players[player_num].put_block()
            self.board[point[0]][point[1]] = -1

    def ai_turn(self):
        while True:
            act = self.players[1].make_decision()
            if len(act) == 1:
                if act[0] == 1 and self.is_blocked('up',1) == False:
                    point = [self.players[1].get_pos()[0]-1, self.players[1].get_pos()[1]]
                    self.board[self.players[1].get_pos()[0]][self.players[1].get_pos()[0]] = 0
                    self.players[1].make_move(point)
                    self.board[point[0]][point[1]] = 2
                    break
                elif act[0] == 2 and self.is_blocked('down',1) == False:
                    point = [self.players[1].get_pos()[0] + 1, self.players[1].get_pos()[1]]
                    self.board[self.players[1].get_pos()[0]][self.players[1].get_pos()[0]] = 0
                    self.players[1].make_move(point)
                    self.board[point[0]][point[1]] = 2
                    break
                elif act[0] == 3 and self.is_blocked('left',1) == False:
                    point = [self.players[1].get_pos()[0], self.players[1].get_pos()[1] - 1]
                    self.board[self.players[1].get_pos()[0]][self.players[1].get_pos()[0]] = 0
                    self.players[1].make_move(point)
                    self.board[point[0]][point[1]] = 2
                    break
                elif act[0] == 4 and self.is_blocked('right',1) == False:
                    point = [self.players[1].get_pos()[0], self.players[1].get_pos()[1] + 2]
                    self.board[self.players[1].get_pos()[0]][self.players[1].get_pos()[0]] = 0
                    self.players[1].make_move(point)
                    self.board[point[0]][point[1]] = 2
                    break

            elif len(act) == 2:
                if self.board[act[0]][act[1]] == 0:
                    self.players[1].put_block()
                    self.board[act[0]][act[1]] = -1
                    break


    def is_blocked(self, way, player_num):
        firtspos = self.players[player_num].get_pos()
        if way == 'up':
            if firtspos[0] == 0 or self.board[firtspos[0] - 1][firtspos[1]] != 0:
                return True
        if way == 'down':
            if firtspos[0] == 8 or self.board[firtspos[0] + 1][firtspos[1]] != 0:
                return True
        if way == 'left':
            if firtspos[1] == 0 or self.board[firtspos[0]][firtspos[1] - 1] != 0:
                return True
        if way == 'right':
            if firtspos[1] == 8 or self.board[firtspos[0]][firtspos[1] + 1] != 0:
                return True
        return False

    def is_route(self, point):
        key = -2
        for k in range(2):
            matrix = []
            matrix.copy(self.board)
            matrix[point[0]][point[1]] = -1
            aa = []
            aa.copy(self.players[k].get_pos())
            a = aa[0]*9 + (aa[1] + 1)
            E = {}
            V = []
            U = []
            d = []
            for i in range(9):
                for j in range(9):
                    if matrix[i][j] == 0:
                        V.append(i*9+(j+1))
                        E[i * 9 + (j + 1)] = []
                        if i - 1 != -1:
                            if matrix[i - 1][j] == 0:
                                E[i * 9 + (j + 1)].append((i - 1) * 9 + (j + 1))
                        if j - 1 != -1:
                            if matrix[i][j - 1] == 0:
                                E[i * 9 + (j + 1)].append(i * 9 + j)
                        if j + 1 != 9:
                            if matrix[i][j+1] == 0:
                                E[i * 9 + (j + 1)].append(i * 9 + (j + 2))
                        if i + 1 != 9:
                            if matrix[i + 1][j] == 0:
                                E[i * 9 + (j + 1)].append((i + 1) * 9 + (j + 1))

            for i in range(81):
                if i == a:
                    d.append(0)
                    apos = i
                else:
                    if i in V:
                        d.append(99999)
                    else:
                        d.append(-1)
            v = minimum(d, U)

            while True:
                U.append(v)
                for i in range(len(E[a])):
                    if E[v][i] not in U:
                        if d[E[v][i]] > d[v]:
                            d[E[v][i]] = d[v] + 1
                if minimum(d, U) == -1:
                    break
                else:
                    v = minimum(d, U)

            kkey = 0
            for i in range(9):
                if k == 0:
                    if d[72 + i + 1] != -1 and d[72 + i + 1] != 99999:
                        kkey += 1
                else:
                    if d[i + 1] != -1 and d[i + 1] != 99999:
                        kkey += 1
            if kkey > 0:
                key += 1
        if key == 0:
            return True
        return False


    def get_board(self):
        return self.board

    def get_blocks(self,player):
        return self.players[player].get_blocks()


class Player:
    def __init__(self, number):
        self.blocks = 10
        if number == 1:
            self.position = [8, 4]
        elif number == 2:
            self.position = [0, 4]

    def make_move(self, point):
        self.position = point

    def put_block(self):
        self.blocks -= 1

    def get_pos(self):
        return self.position

    def get_blocks(self):
        return self.blocks


class AI_noob(Player):

    def make_decision(self):
        act = random.randint(1,3)
        if act == 1 and self.get_blocks() != 0:
            return [random.randrange(0, 9), random.randrange(0, 9)]
        else:
            way = random.randint(1, 5)
            return [way]





