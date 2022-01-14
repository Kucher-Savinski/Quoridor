import keyboard
import model, view
import time
import sys

class Start:
    def __init__(self):
        self.main_menu = view.Menu()
        while True:
            if keyboard.is_pressed('space'):
                self.main_menu.show_menu(0)
                self.menu_control()
                break

    def menu_control(self):
        pos = 0
        self.main_menu.show_menu(pos)
        while True:
            time.sleep(0.04)
            if keyboard.is_pressed('up'):
                if pos > 0:
                    pos -= 1
                    self.main_menu.show_menu(pos)
                    time.sleep(0.15)
            elif keyboard.is_pressed('down'):
                if pos < 4:
                    pos += 1
                    self.main_menu.show_menu(pos)
                    time.sleep(0.15)
            elif keyboard.is_pressed('space'):
                if pos == 4:
                    time.sleep(0.1)
                    sys.exit()
                if pos == 0:
                    self.go_game('PvP')
                    self.main_menu.show_menu(pos)
                    continue
                elif pos == 1:
                    self.go_game('PvAIn')
                    self.main_menu.show_menu(pos)
                    continue
                elif pos == 2:
                    self.go_game('PvAIm')
                    self.main_menu.show_menu(pos)
                    continue
                elif pos == 3:
                    self.go_game('AIn_v_AIm')
                    self.main_menu.show_menu(pos)
                    continue

    def go_game(self, type):

        if type == 'PvP':
            self.new_game = model.Game(type)
            self.turn = 1
            player_num = 0
            key = 0
            kkey = 0
            self.new_board = view.Board(self.new_game.get_board(), 2)
            while True:
                if kkey != 0:
                    break
                self.previous_block = [[], []]
                self.previous_point = [self.new_game.players[0].get_pos(), self.new_game.players[1].get_pos()]
                while True:
                    if kkey != 0:
                        break
                    point = []
                    if keyboard.is_pressed('up'):
                        if self.new_game.is_blocked('up', player_num):
                            self.new_board.show_board(player_num, self.new_game.get_board(), self.new_game.get_blocks(player_num), 2, self.turn,
                                                      [], [], 'Error:way is blocked')
                        else:
                            point.append(self.previous_point[player_num][0] - 1)
                            point.append(self.previous_point[player_num][1])
                            if (player_num == 0 and point[0] == 0) or (player_num == 1 and point[0] == 8):
                                self.new_board.game_over(player_num)
                                kkey = 1
                                time.sleep(5)
                            self.new_game.make_turn(player_num, 'move', point)
                            self.turn += 1
                            pp = player_num
                            player_num = (player_num + 1) % 2
                            self.new_board.show_board(player_num, self.new_game.get_board(), self.new_game.get_blocks(player_num), 2,self.turn,
                                                      self.previous_point[player_num], [], '')
                            self.previous_point[pp] = point

                            time.sleep(0.1)
                            continue
                    elif keyboard.is_pressed('down'):
                        if self.new_game.is_blocked('down',player_num):
                            self.new_board.show_board(player_num, self.new_game.get_board(), self.new_game.get_blocks(player_num), 2, self.turn,
                                                      [], [], 'Error:way is blocked')
                        else:
                            point.append(self.previous_point[player_num][0] + 1)
                            point.append(self.previous_point[player_num][1])
                            if (player_num == 0 and point[0] == 0) or (player_num == 1 and point[0] == 8):
                                self.new_board.game_over(player_num)
                                time.sleep(5)
                                kkey = 1
                            self.new_game.make_turn(player_num, 'move', point)
                            self.turn += 1
                            pp = player_num
                            player_num = (player_num + 1) % 2
                            self.new_board.show_board(player_num, self.new_game.get_board(), self.new_game.get_blocks(player_num), 2,self.turn,
                                                      self.previous_point[player_num], [], '')
                            self.previous_point[pp] = point

                            time.sleep(0.1)
                            continue
                    elif keyboard.is_pressed('left'):
                        if self.new_game.is_blocked('left',player_num):
                            self.new_board.show_board(player_num, self.new_game.get_board(), self.new_game.get_blocks(player_num), 2, self.turn,
                                                      [], [], 'Error:way is blocked')
                        else:
                            point.append(self.previous_point[player_num][0])
                            point.append(self.previous_point[player_num][1] - 1)
                            if (player_num == 0 and point[0] == 0) or (player_num == 1 and point[0] == 8):
                                self.new_board.game_over(player_num)
                                kkey = 1
                                time.sleep(5)
                            self.new_game.make_turn(player_num, 'move', point)
                            self.turn += 1
                            pp = player_num
                            player_num = (player_num + 1) % 2
                            self.new_board.show_board(player_num, self.new_game.get_board(), self.new_game.get_blocks(player_num), 2,self.turn,
                                                      self.previous_point[player_num], [], '')
                            self.previous_point[pp] = point

                            time.sleep(0.1)
                            continue
                    elif keyboard.is_pressed('right'):
                        if self.new_game.is_blocked('right',player_num):
                            self.new_board.show_board(player_num, self.new_game.get_board(), self.new_game.get_blocks(player_num), 2, self.turn,
                                                      [], [], 'Error:way is blocked')
                        else:
                            point.append(self.previous_point[player_num][0])
                            point.append(self.previous_point[player_num][1] + 1)
                            if (player_num == 0 and point[0] == 0) or (player_num == 1 and point[0] == 8):
                                self.new_board.game_over(player_num)
                                kkey = 1
                                time.sleep(5)
                            self.new_game.make_turn(player_num, 'move', point)
                            self.turn += 1
                            pp = player_num
                            player_num = (player_num + 1) % 2
                            self.new_board.show_board(player_num, self.new_game.get_board(), self.new_game.get_blocks(player_num), 2,self.turn,
                                                      self.previous_point[player_num], [], '')
                            self.previous_point[pp] = point

                            time.sleep(0.1)
                            continue
                    elif keyboard.is_pressed('P'):

                        if self.new_game.players[player_num].get_blocks() == 0:
                            self.new_board.blocks_error()
                            continue
                        err = ''
                        while True:
                            coords = self.new_board.input_point(err)
                            if coords[0] == '-1':
                                err = 'Inputted wrong data'
                            elif coords[0] == 'esc':
                                break
                            elif self.new_game.get_board()[coords[0]][coords[1]] != 0:
                                err = 'This cell is not available'
                            else:
                                self.previous_block[player_num] = coords
                                self.new_game.make_turn(player_num, 'put', coords)
                                pp = player_num
                                player_num = (player_num + 1) % 2
                                self.turn += 1
                                coords[0] += 1
                                coords[1] += 1
                                self.new_board.show_board(player_num, self.new_game.get_board(),
                                                          self.new_game.get_blocks(player_num), 2, self.turn,
                                                          [], self.previous_block[pp], '')
                                break

                    elif keyboard.is_pressed('escape'):
                        kkey = 1



            return 0