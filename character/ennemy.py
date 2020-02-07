from position.position import Position
from config import *

class Ennemy(Position):

    """Classe contenant la position du gardien."""
    def __init__(self, dico):
        self.pos = Position.pos(dico, GARDIEN)
        self.coord = self.pos[0]
