import colorama
import os

colorama.init()

class Menu:
    def __init__(self):
        print('This game is controlled with arrows keys and some extra keys\n(Hints will be showed you when it will be needed)\n(Be sure you use English layout)\nPress ENTER to continue')
        self.menu_text = ['Start player vs player', 'Start player vs noob AI', 'Start player vs master AI', 'Start noob AI vs master AI', 'Exit']

    def show_menu(self, pos):
        int(pos)
        os.system('cls||clear')
        for i in range(5):
            if(i == pos):
                print(colorama.Fore.YELLOW + self.menu_text[i])
            else:
                print(colorama.Fore.WHITE + self.menu_text[i])

