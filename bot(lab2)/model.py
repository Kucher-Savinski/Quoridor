def minimum(arr, U):
    minim = 999999999
    pos = -1
    for i in range(len(arr)):
        if arr[i] < minim and arr[i] > -1 and arr[i] not in U:
            minim = arr[i]
            pos = i
    return pos


class Game:
    def __init__(self, player):
        self.gametype = type
        self.board = []
        self.block_points = []
        self.bot_coord = []
        self.player_coord = []
        self.state = 'shock'
        for i in range(9):
            self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        for i in range(8):
            self.block_points.append(['', '', '', '', '', '', '', ''])
        if player == 1:
            self.bot_coord.append(0)
            self.bot_coord.append(4)
            self.player_coord.append(8)
            self.player_coord.append(4)
        else:
            self.bot_coord.append(8)
            self.bot_coord.append(4)
            self.player_coord.append(0)
            self.player_coord.append(4)
        self.board[self.bot_coord[0]][self.bot_coord[1]] = 2
        self.board[self.player_coord[0]][self.player_coord[1]] = 1

    def tactics(self):
        pass

    def dijkstra(self, player):
        matrix = []
        matrix.copy(self.board)
        aa = []
        if player == 1:
            aa.copy(self.player_coord)
        else:
            aa.copy(self.bot_coord)
        a = aa[0] * 9 + (aa[1] + 1)
        E = {}
        V = []
        U = []
        d = []
        p = {}
        for i in range(9):
            for j in range(9):
                if matrix[i][j] == 0:

                    V.append(i * 9 + (j + 1))
                    E[i * 9 + (j + 1)] = []
                    p[i * 9 + (j + 1)] = []

                    if i - 1 != -1 and (j != 0 and j != 8) :
                        if self.block_points[i - 1][j] != 'h' and self.block_points[i - 1][j - 1] != 'h':
                            E[i * 9 + (j + 1)].append((i - 1) * 9 + (j + 1))
                    elif i - 1 != -1 and j == 0:
                        if self.block_points[i - 1][j] != 'h':
                            E[i * 9 + (j + 1)].append((i - 1) * 9 + (j + 1))
                    elif i - 1 != -1 and j == 8:
                        if self.block_points[i - 1][j-1] != 'h':
                            E[i * 9 + (j + 1)].append((i - 1) * 9 + (j + 1))

                    if j - 1 != -1 and 0 < i < 8:
                        if self.block_points[i][j-1] != 'w' and self.block_points[i - 1][j-1] != 'w':
                            E[i * 9 + (j + 1)].append(i * 9 + j)
                    elif j - 1 != -1 and i == 0 :
                        if self.block_points[i][j-1] != 'w':
                            E[i * 9 + (j + 1)].append(i * 9 + j)
                    elif j - 1 != -1 and i == 8 :
                        if self.block_points[i - 1][j-1] != 'w':
                            E[i * 9 + (j + 1)].append(i * 9 + j)

                    if j + 1 != 9 and 0 < i < 8:
                        if self.block_points[i][j + 1] != 'w' and self.block_points[i - 1][j + 1] != 'w':
                            E[i * 9 + (j + 1)].append(i * 9 + (j + 2))
                    elif j + 1 != 9 and i == 0 :
                        if self.block_points[i][j + 1] != 'w':
                            E[i * 9 + (j + 1)].append(i * 9 + j)
                    elif j + 1 != 9 and i == 8 :
                        if self.block_points[i - 1][j-1] != 'w':
                            E[i * 9 + (j + 1)].append(i * 9 + j)

                    if i + 1 != 9:
                        if self.block_points[i + 1][j] != 'h' and self.block_points[i + 1][j-1] != 'h':
                            E[i * 9 + (j + 1)].append((i + 1) * 9 + (j + 1))
                    elif i + 1 != 9 and j == 0:
                        if self.block_points[i + 1][j] != 'h':
                            E[i * 9 + (j + 1)].append((i - 1) * 9 + (j + 1))
                    elif i + 1 != 9 and j == 8:
                        if self.block_points[i + 1][j-1] != 'h':
                            E[i * 9 + (j + 1)].append((i - 1) * 9 + (j + 1))

        for i in range(81):
            if i == a:
                d.append(0)
                apos = i
            else:
                if i in V:
                    d.append(99999)

        v = minimum(d, U)

        while True:
            U.append(v)
            for i in range(len(E[a])):
                if E[v][i] not in U:
                    if d[E[v][i]] > d[v] + 1:
                        d[E[v][i]] = d[v] + 1
                        p[E[v][i]].append(E[v][i])
            if minimum(d, U) == -1:
                break
            else:
                v = minimum(d, U)
        minway = []
        minpoint = []
        for i in range(9):
            if player == 1:
                if d[72 + i + 1] != -1 and d[72 + i + 1] != 99999:
                    minpoint.append(0)
                    minpoint.append(i)
            else:
                if d[i + 1] != -1 and d[i + 1] != 99999:
                    minpoint.append(8)
                    minpoint.append(i)
        return [minway, minpoint]

    def make_turn(self, type, point):
        if type == 'move':
            pass

        elif type == 'wall':
            pass


    def init_turn(self, type, point, block_type):
        if type == 'move' or type == 'jump':
            self.board[self.player_coord[0]][self.player_coord[1]] = 0
            self.player_coord.copy(point)
            self.board[self.player_coord[0]][self.player_coord[1]] = 1
        elif type == 'wall':
            self.block_points[point[0]][point[1]] = block_type


