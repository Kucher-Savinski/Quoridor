import model
import view

class Start:
    def __init__(self):
        self.maincolor = ''
        self.main_board_abr = 'ABCDEFGHI'
        self.blocks_board_abr = 'STUVWXYZ'
        self.vision = view.outpost()
        self.player = self.vision.start()
        self.game = model.Game(self.player)

        if self.player == 2:
            self.game.make_turn('move', [7 , 4], '')
            move = 'move ' + self.main_board_abr[4] + '8'
            self.vision.show_move(move)

        while True:

            command = self.vision.get_move()
            command1 = command.split(' ')
            move, point = command1[0], command1[1]
            block_type = ''
            ppoint = []
            if len(point) == 3:
                s = point[2]
                block_type += s
                ppoint.append(int(point[1]) - 1)
                for i in range(len(self.blocks_board_abr)):
                    if self.blocks_board_abr[i] == point[0]:
                        ppoint.append(i)

            if len(point) == 2:
                ppoint.append(int(point[1]) - 1)
                for i in range(len(self.main_board_abr)):
                    if self.main_board_abr[i] == point[0]:
                        ppoint.append(i)

            self.game.init_turn(move, ppoint, block_type)

            turned = self.game.tactics()
            if turned[0] == 'wall':
                move = turned[0] + ' ' + self.blocks_board_abr[turned[1][1]] + str(turned[1][0] + 1) + turned[2]
            else:
                move = turned[0] + ' ' + self.main_board_abr[turned[1][1]] + str(turned[1][0] + 1) + turned[2]
            self.vision.show_move(move)


