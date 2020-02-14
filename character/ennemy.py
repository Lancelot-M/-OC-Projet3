"""Fichier contenant la position du gardien."""

from position.position import Position
from config import GARDIEN

class Ennemy(Position):

    """Classe d'initialisation"""
    def __init__(self, dico):
        self.pos = Position.pos(dico, GARDIEN)
        self.coord = self.pos[0]
