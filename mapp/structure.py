from position.position import *

"""Classe représentant les éléments composants la carte.(murs/chemins/portes...)"""

class Structure(Position):

    def __init__(self, map_ref, image=""):
        self.image = image
        self.pos = Position.pos(map_ref, self.image)
