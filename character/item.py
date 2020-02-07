from position.position import Position
from config import *

class Items(Position):

    """Classe contenant la position des objets."""
    def __init__(self, dico):
        self.pos = Position.pos(dico, ITEM1)
