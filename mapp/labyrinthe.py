import pygame
from config import *
from position.position import Position
from mapp.structure import Structure
from character.ennemy import Ennemy
from character.player import Player
from character.item import Items

class Labyrinthe(Position):

    """Classe contenant tout les éléments du jeu.(Joueur, gardien, structures...) La gestion des déplacements se fait a traves elle."""
    def __init__(self, file_name):
        self.name = file_name
        self.ref = self.mkdico()
        self.wall = Structure(self.ref, image=WALL)
        self.path = Structure(self.ref, image=[PATH, GARDIEN, ITEM1, HERO])
        self.player = Player(self.ref)
        self.gardien = Ennemy(self.ref)
        self.items = Items(self.ref)

    def mkdico(self):
        c = ""
        x = 0
        y = 0
        map_ref = {}
        with open(self.name, "r") as f:
            c = f.read(1)
            while c:
                if c == "\n":
                    x = 0
                    y += 40
                    c = f.read(1)
                    continue
                map_ref[x, y] = c
                x += 40
                c = f.read(1)
            return map_ref

    def find_coord(self, key):

        x = self.player.coord[0]
        y = self.player.coord[1]
        if key == pygame.K_LEFT:
            return (x - 40, y)
        elif key == pygame.K_UP:
            return (x, y - 40)
        elif key == pygame.K_DOWN:
            return (x, y + 40)
        elif key == pygame.K_RIGHT:
            return (x + 40, y)
        else:
            exit()

    def move(self, key):

        if self.player:
            new_coord = self.find_coord(key)
            if new_coord in self.path.pos:
                if new_coord == self.gardien.coord:
                    if self.player.inventory == []:
                        print("YOU LOOSE")
                        exit()
                    else:
                        print("YOU WIN")
                        exit()
                if new_coord in self.items.pos:
                    self.player.inventory.append("seringue hypodermique")
                self.ref[self.player.coord] = PATH
                self.player.coord = new_coord
                self.ref[self.player.coord] = HERO
        else:
            exit()
