from position.position import Position
from config import *
from random import choice

class Items(Position):

    """Classe contenant la position des objets."""
    def __init__(self, map_ref, image):
        self.image = image
        self.pathlist = Position.pos(map_ref, PATH)
        self.pos = choice(self.pathlist)
