"""File containing the guardian's position."""

from position.position import Position
from config import GARDIEN

class Ennemy(Position):

    """Initialization class"""
    def __init__(self, dico):
        self.pos = Position.pos(dico, GARDIEN)
        self.coord = self.pos[0]
