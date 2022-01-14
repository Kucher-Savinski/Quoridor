import colorama
import os
import time
colorama.init()


class Menu:
    def __init__(self):
        print(
            'This game is controlled with arrows keys and some extra keys\n(Hints will be showed you when it will be needed) Menu confirm key is SPACE\n(Be sure you use English layout)\nPress SPACE to continue')
        self.menu_text = ['Start player vs player', 'Start player vs noob AI', 'Start player vs master AI',
                          'Start noob AI vs master AI', 'Exit']

    def show_menu(self, pos):
        int(pos)
        os.system('cls||clear')
        for i in range(5):
            if (i == pos):
                print(colorama.Fore.YELLOW + self.menu_text[i])
            else:
                print(colorama.Fore.WHITE + self.menu_text[i])


class Board:
    def __init__(self, matrix, players):
        self.board = []
        self.show_board(0, matrix, 10, players, 1, [], [], '')

    def show_board(self, player_num, matrix, blocks, players, turn, prev_point, prev_block, err):
        os.system('cls||clear')
        self.board = []
        player1_icon = 'Θ'
        player2_icon = 'Ψ'
        self.board.append('0  1  2  3  4  5  6  7  8  9')
        for i in range(1, 10):
            line = str(i)+'  '
            for j in range(9):
                if matrix[i - 1][j] == 0:
                    line += '•  '
                elif matrix[i - 1][j] == -1:
                    line += '#  '
                elif matrix[i - 1][j] == 1:
                    line += 'Θ  '
                elif matrix[i - 1][j] == 2:
                    line += 'Ψ  '
            self.board.append(line)
        for i in range(10):
            print(self.board[i])

        if players == 2:
            if turn != 1:
                if prev_point == []:
                    print(f'On previous turn player {2 if player_num == 0 else 1}({player1_icon if player_num == 1 else player2_icon}) puts block on position{prev_block}')
                elif prev_block == []:
                    print(f'On previous turn player {2 if player_num == 0 else 1}({player1_icon if player_num == 1 else player2_icon}) moves on position{prev_point}')

            print(f'Now is player {player_num+1}({player1_icon if player_num == 0 else player2_icon}) turn, please make move with ARROWS or put block with P( blocks left: {blocks})')
            print(f'(Press ESCAPE to go to main menu)')
            if err != '':
                print(err)

    def game_over(self, player):
        os.system('cls||clear')
        print(f'Player {player+1} won!!!!')




    def input_point(self, err):
            time.sleep(0.1)
            if err != '':
                print(colorama.Fore.RED + err + colorama.Fore.WHITE + '. Please try again')
            print(colorama.Fore.WHITE + 'Input coordinates splitted with space.(Example:4 6) Type esc to switch on move mode. Press ENTER to confirm your coordinates  ')
            ans = input()
            coord = ans.split(' ')
            if ans == 'esc':
                return [ans]

            if len(coord) == 2 and -2 < int(coord[0])-1 < 9 and -2 < int(coord[1])-1 < 9:
                return [int(coord[0])-1,int(coord[1])-1]
            return ['-1']


    def blocks_error(self):
        print('You don`t have any blocks available')