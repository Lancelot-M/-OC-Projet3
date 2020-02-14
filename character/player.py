"""Fichier contenant inventaire et position du joueur."""

from position.position import Position
from config import HERO

class Player(Position):

    """Classe contenant les stats du joueur."""
    def __init__(self, dico):
        self.pos = Position.pos(dico, HERO)
        self.coord = self.pos[0]
        self.inventory = []
