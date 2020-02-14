"""Fichier contenant la position des objet du jeu."""

from random import choice
from config import PATH
from position.position import Position

class Items(Position):

    """Classe d'initialisation"""
    def __init__(self, map_ref, image):
        self.image = image
        self.ref = map_ref
        self.pathlist = Position.pos(map_ref, PATH)
        self.pos = choice(self.pathlist)
