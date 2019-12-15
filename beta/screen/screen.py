class Screen:
    
    def __init__(self, map_ref):
        self.win = "terminal"

    def game_map(self, map_ref):
        screen = ""
        for value in map_ref.values():
            screen += value
        print(screen)

    def game_start(self):
        print("Bienvenue dans le jeu du labyrinthe !!!")
        print("Vous incarnez Mac Gyver. Le but est de vous échapper en récupérant la seringue hypodermique")
        print("Pour vous déplacer utilisez les touches ZQSD.")

    def game_win(self):
        print("YOU WIN !!!")

    def game_loose(self):
        print("You loose, try again...")

