"""Fichier represant les parties en dur de la carte."""

from position.position import Position

class Structure(Position):

    """Classe representant les elements non mobiles (murs/chemins)"""
    def __init__(self, map_ref, image=""):
        self.pos = Position.pos(map_ref, image)
