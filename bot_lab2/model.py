def minimum(arr, U):
    minim = 99999999999
    pos = -1
    for i in range(len(arr)):
        if arr[i] < minim  and i + 1 not in U:
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
        self.player_winline = 0
        self.bot_winline = 8
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
            self.player_winline = 8
            self.bot_winline = 0
        self.board[self.bot_coord[0]][self.bot_coord[1]] = 2
        self.board[self.player_coord[0]][self.player_coord[1]] = 1

    def tactics(self):
        block = ''
        type = ''
        point = []
        key = 0
        if self.dijkstra(1)[2] == 2 and key != 1:
            self.state = 'defence'
            key += 1
        else:
            self.state = 'shock'
        if self.state == 'shock':
            num = self.dijkstra(2)[1]
            point.append(num[0])
            point.append(num[1])
            if point[0] != 0 and self.board[point[0]][point[1]] == 1:
                type = 'jump'
                point[0] -= 1
            else:
                type = 'move'
            self.make_turn(type, point, '')
        elif self.state == 'defence':
            type = 'wall'
            block = 'h'
            self.make_turn(type, [self.player_coord[0] - 1, self.player_coord[1]], block)
            point = [self.player_coord[0] - 1, self.player_coord[1]]
        return [type, point, block]

    def dijkstra(self, player):
        matrix = []
        matrix = self.board.copy()
        aa = []
        opponent = 2
        if player == 1:
            aa = self.player_coord.copy()
        else:
            aa = self.bot_coord.copy()
            opponent = 1
        a = aa[0] * 9 + (aa[1] + 1)
        E = {}
        V = []
        U = []
        d = []
        p = {}
        for i in range(9):
            for j in range(9):
                if True:

                    V.append(i * 9 + (j + 1))
                    E[i * 9 + (j + 1)] = []
                    p[i * 9 + (j + 1)] = []

                    if i - 1 != -1 and (j != 0 and j != 8) :
                        if self.block_points[i - 1][j] != 'h' and self.block_points[i - 1][j - 1] != 'h' and matrix[i - 1][j] != opponent:
                            E[i * 9 + (j + 1)].append((i - 1) * 9 + (j + 1))
                        elif self.block_points[i - 1][j] != 'h' and self.block_points[i - 1][j - 1] != 'h' and matrix[i - 1][j] == opponent:
                            if i > 2 and self.block_points[i - 2][j] != 'h' and self.block_points[i - 2][j - 1] != 'h':
                                E[i * 9 + (j + 1)].append((i - 2) * 9 + (j + 1))
                    elif i - 1 != -1 and j == 0:
                        if self.block_points[i - 1][j] != 'h':
                            E[i * 9 + (j + 1)].append((i - 1) * 9 + (j + 1))
                    elif i - 1 != -1 and j == 8:
                        if self.block_points[i - 1][j-1] != 'h':
                            E[i * 9 + (j + 1)].append((i - 1) * 9 + (j + 1))

                    if j - 1 != -1 and 0 < i < 8:
                        if self.block_points[i][j-1] != 'w' and self.block_points[i - 1][j-1] != 'w' and matrix[i][j - 1] != opponent:
                            E[i * 9 + (j + 1)].append(i * 9 + j)
                        elif self.block_points[i][j-1] != 'w' and self.block_points[i - 1][j-1] != 'w' and matrix[i][j - 1] == opponent:
                            if j > 1 and self.block_points[i][j-1] != 'w' and self.block_points[i - 1][j-1] != 'w':
                                E[i * 9 + (j + 1)].append(i * 9 + j - 1)
                    elif j - 1 != -1 and i == 0 :
                        if self.block_points[i][j-1] != 'w':
                            E[i * 9 + (j + 1)].append(i * 9 + j)
                    elif j - 1 != -1 and i == 8 :
                        if self.block_points[i - 1][j-1] != 'w':
                            E[i * 9 + (j + 1)].append(i * 9 + j)

                    if j + 1 != 9 and 0 < i < 8:
                        if self.block_points[i][j] != 'w' and self.block_points[i - 1][j] != 'w' and matrix[i][j + 1] != opponent:
                            E[i * 9 + (j + 1)].append(i * 9 + (j + 2))
                        elif self.block_points[i][j] != 'w' and self.block_points[i - 1][j] != 'w' and matrix[i][j + 1] == opponent:
                            if j < 7 and self.block_points[i][j] != 'w' and self.block_points[i - 1][j] != 'w':
                                E[i * 9 + (j + 1)].append(i * 9 + (j + 3))
                    elif j + 1 != 9 and i == 0 :
                        if self.block_points[i][j] != 'w':
                            E[i * 9 + (j + 1)].append(i * 9 + (j+2))
                    elif j + 1 != 9 and i == 8 :
                        if self.block_points[i - 1][j] != 'w':
                            E[i * 9 + (j + 1)].append(i * 9 + (j+2))

                    if i + 1 != 9 and 0 < j < 8:
                        if self.block_points[i][j] != 'h' and self.block_points[i][j-1] != 'h' and matrix[i + 1][j] != opponent:
                            E[i * 9 + (j + 1)].append((i + 1) * 9 + (j + 1))
                        elif self.block_points[i][j] != 'h' and self.block_points[i][j-1] != 'h' and matrix[i + 1][j] == opponent:
                            if i < 7 and self.block_points[i + 1][j] != 'h' and self.block_points[i + 1][j-1] != 'h':
                                E[i * 9 + (j + 1)].append((i + 2) * 9 + (j + 1))
                    elif i + 1 != 9 and j == 0:
                        if self.block_points[i][j] != 'h':
                            E[i * 9 + (j + 1)].append((i + 1) * 9 + (j + 1))
                    elif i + 1 != 9 and j == 8:
                        if self.block_points[i][j-1] != 'h':
                            E[i * 9 + (j + 1)].append((i + 1) * 9 + (j + 1))

        for i in range(82):
            if i == a:
                d.append(0)
                apos = i
            else:
                if i in V:
                    d.append(99999)
        v = minimum(d, U) + 1

        while True:
            U.append(v)

            for i in range(0, len(E[v])):
                if E[v][i] not in U:
                    if d[E[v][i] - 1] > d[v - 1] + 1:
                        d[E[v][i] - 1] = d[v - 1] + 1
                        p[E[v][i]] = p[v].copy()
                        p[E[v][i]].append(E[v][i])
            if len(U) > 80:
                break
            else:
                v = minimum(d, U) + 1

        minpoint = []
        mindist = 0
        min = 99999
        min_ = 0
        min_d = 0
        for i in range(9):
            if player == 1 and self.player_winline == 0:

                if d[i] < 99999 and d[i] < min:
                    min = d[i]
                    min_ = i
                    min_d = i + 1
            elif player == 1 and self.player_winline == 8:

                if d[71 + i] < 99999 and d[71 + i] < min:
                    min = d[71 + i]
                    min_ = i
                    min_d = i + 1 + 72
            elif  player == 2 and self.bot_winline == 0:

                if d[i] < 99999 and d[i] < min:
                    min = d[i]
                    min_ = i
                    min_d = i + 1
            elif  player == 2 and self.bot_winline == 8:

                if d[71 + i] < 99999 and d[71 + i] < min:
                    min = d[71 + i]
                    min_ = i
                    min_d = i + 72 + 1
        minway = []
        if (self.bot_winline == 0 and player == 2) or (self.player_coord == 0 and player == 1):
            minway = p[min_d].copy()
        else:
            minway = p[min_d - 1].copy()

        minpoint.append(minway[0] // 9)
        minpoint.append((minway[0] % 9) - 1)
        mindist = d[min_d - 1]
        return [minway, minpoint, mindist]

    def make_turn(self, type, point, block_type):
        if type == 'move' or type == 'jump':
            self.board[self.bot_coord[0]][self.bot_coord[1]] = 0
            self.bot_coord = point.copy()
            self.board[self.bot_coord[0]][self.bot_coord[1]] = 2
        elif type == 'wall':
            self.block_points[point[0]][point[1]] = block_type

    def init_turn(self, type, point, block_type):
        if type == 'move' or type == 'jump':
            self.board[self.player_coord[0]][self.player_coord[1]] = 0
            self.player_coord = point.copy()
            self.board[self.player_coord[0]][self.player_coord[1]] = 1
        elif type == 'wall':
            self.block_points[point[0]][point[1]] = block_type

    def is_end(self, color):
        if self.bot_coord[0] == self.bot_winline:
            return True
        if self.player_coord[0] == self.player_winline:
            return True
        return False