import sys

import keyboard
import time
import model, view



class Start:
    def __init__(self):
        self.main_menu = view.Menu()
        while True:
            if keyboard.is_pressed('enter'):
                self.main_menu.show_menu(0)
                self.menu_control()
                break

    def menu_control(self):
        pos = 0
        while True:
            if keyboard.is_pressed('up'):
                if pos > 0:
                    pos -= 1
                    self.main_menu.show_menu(pos)
                    time.sleep(0.08)
            elif keyboard.is_pressed('down'):
                if pos < 4:
                    pos += 1
                    self.main_menu.show_menu(pos)
                    time.sleep(0.08)
            elif keyboard.is_pressed('enter'):
                if pos == 4:
                    sys.exit()
                if pos == 0:
                    self.new_game('PvP')
                elif pos == 1:
                    self.new_game('PvAIn')
                elif pos == 2:
                    self.new_game('PvAIm')
                elif pos == 3:
                    self.new_game('AIn_v_AIm')

    def new_game(self, type):
        pass




