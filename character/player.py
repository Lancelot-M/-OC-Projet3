"""File containing player's inventory and position."""

from position.position import Position
from config import HERO


class Player(Position):

    """Class containing player stats."""
    def __init__(self, dico):
        self.pos = Position.pos(dico, HERO)
        self.coord = self.pos[0]
        self.inventory = []
