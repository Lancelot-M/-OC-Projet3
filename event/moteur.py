""" Classe qui permet de gerer les interactions entre objet."""

class Moteur:

    def __init__(self, screen=None, player=None, ennemy=None, item=None, mapp=None):
        self.screen = screen
        self.player = player
        self.ennemy = ennemy
        self.item = item
        self.mapp = mapp

    def move(self):
        if self.player:
            import getch
            key = getch.getch()
            new_pos = self.player.way(key)
            if new_pos in self.mapp.path.pos:
                if new_pos == self.ennemy.coord:
                    if self.player.inventory == "empty":
                        self.screen.game_loose()
                        exit()
                    else:
                        self.screen.game_win()
                        exit()
                if new_pos in self.item.pos:
                    self.player.inventory = "seringue hypodermique"
                self.mapp.ref[self.player.coord] = " "
                self.player.coord = new_pos
                self.mapp.ref[self.player.coord] = "M"
        else:
            exit()

    def play(self):
        self.screen.game_start()
        while 1:
            self.screen.game_map()
            self.move()
