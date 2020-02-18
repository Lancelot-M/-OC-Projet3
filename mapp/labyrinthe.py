"""File containing the class representing the card and its components."""

import pygame
from config import WALL, HERO, GARDIEN, ITEM1, ITEM2, ITEM3, PATH
from position.position import Position
from mapp.structure import Structure
from character.init_movable import Movable

class Labyrinthe(Position):

    """Class containing the elements of the game. The management of displacements is done through it."""
    def __init__(self, map_file):
        self.name = map_file
        self.ref = self.mkdico()
        self.movable = Movable(self.ref)
        self.wall = Structure(self.ref, image=WALL)
        self.path = Structure(self.ref, image=[PATH, GARDIEN, HERO, ITEM1])
        self.init_labyrinthe_items()

    def init_labyrinthe_items(self):
        """Initialization of objects on a random position."""
        self.ref[self.movable.item1.pos] = ITEM1
        self.ref[self.movable.item2.pos] = ITEM2
        self.ref[self.movable.item3.pos] = ITEM3
    def mkdico(self):
        """Dictionary [coordinate] == [symbol]"""
        text = ""
        abscisse = 0
        ordonnee = 0
        map_ref = {}
        with open(self.name, "r") as fichier:
            text = fichier.read(1)
            while text:
                if text == "\n":
                    abscisse = 0
                    ordonnee += 40
                    text = fichier.read(1)
                    continue
                map_ref[abscisse, ordonnee] = text
                abscisse += 40
                text = fichier.read(1)
            return map_ref
    def find_coord(self, key):
        """Renvoie de coordonnee en fonction de la touche clavier."""
        abscisse = self.movable.player.coord[0]
        ordonnee = self.movable.player.coord[1]
        if key == pygame.K_LEFT:
            return abscisse - 40, ordonnee
        elif key == pygame.K_UP:
            return abscisse, ordonnee - 40
        elif key == pygame.K_DOWN:
            return abscisse, ordonnee + 40
        elif key == pygame.K_RIGHT:
            return abscisse + 40, ordonnee
        return None
    def move(self, key):
        """Hero movement management"""
        if self.movable.player:
            new_coord = self.find_coord(key)
            if new_coord in self.path.pos:
                if new_coord == self.movable.gardien.coord:
                    if len(self.movable.player.inventory) < 3:
                        return "LOOSE"
                    return "WIN"
                if new_coord == self.movable.item1.pos:
                    if "AIGUILLE" not in self.movable.player.inventory:
                        self.movable.player.inventory.append("AIGUILLE")
                if new_coord == self.movable.item3.pos:
                    if "ETHER" not in self.movable.player.inventory:
                        self.movable.player.inventory.append("ETHER")
                if new_coord == self.movable.item2.pos:
                    if "TUBE" not in self.movable.player.inventory:
                        self.movable.player.inventory.append("TUBE")
                self.ref[self.movable.player.coord] = PATH
                self.movable.player.coord = new_coord
                self.ref[self.movable.player.coord] = HERO
        return "play"
