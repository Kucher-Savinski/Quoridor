import colorama
import os

colorama.init()


class Menu:
    def __init__(self):
        print(
            'This game is controlled with arrows keys and some extra keys\n(Hints will be showed you when it will be needed)\n(Be sure you use English layout)\nPress ENTER to continue')
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
        self.show_board(0, matrix, 10, players, 1, [], [])

    def show_board(self, player_num, matrix, blocks, players, turn, prev_point, prev_block):
        os.system('cls||clear')
        player1_icon = 'Ψ'
        player2_icon = 'Θ'
        self.board.append('0  1  2  3  4  5  6  7  8  9')
        for i in range(1, 10):
            line = str(i) + '  '
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
                    print(f'On previous turn player {1 if player_num == 0 else 0}({player1_icon if player_num == 1 else player2_icon}) puts block on position{prev_block}')
                if prev_block == []:
                    print(f'On previous turn player {1 if player_num == 0 else 0}({player1_icon if player_num == 1 else player2_icon}) moves on position{prev_point}')

            print(f'Now is player {player_num} turn, please make move with ARROWS or put block with P( blocks left: {blocks})')
