from position.position import *

class Structure(Position):

    """Classe représentant les éléments composants la carte.(murs/chemins/portes...)"""
    def __init__(self, map_ref, image=""):
        self.pos = Position.pos(map_ref, image)
