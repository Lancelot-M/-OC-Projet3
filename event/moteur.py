from screen.screen import *
from position.position import Position
from mapp.labyrinthe import *
from mapp.structure import *
from character.ennemy import *
from character.item import *
from character.player import *

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
                if new_pos == self.ennemy.pos[0]:
                    if self.player.inventory == "empty":
                        self.screen.game_loose()
                        exit()
                    else:
                        self.screen.game_win()
                        exit()
                if new_pos == self.item.pos[0]:
                    self.player.inventory = "seringue hypodermique"
                self.mapp.ref[self.player.pos[0]] = " "
                self.player.pos[0] = new_pos
                self.mapp.ref[self.player.pos[0]] = "M"
        else:
            exit()

    def play(self):
        while 1:
            self.screen.game_map()
            self.move()
