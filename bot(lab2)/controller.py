import model
import view

class Start:
    def __init__(self):

        self.main_board_abr = 'ABCDEFGHI'
        self.blocks_board_abr = 'STUVWXYZ'
        self.vision = view.outpost()
        player = self.vision.start()
        self.game = model.Game(player)

    def main_game(self):
        while True:
            pass