"""Classe representant le gardien."""

from position.position import Position

class Ennemy(Position):

    def __init__(self, dico):
        self.image = "G"
        self.pos = Position.pos(dico, self.image)
        self.coord = self.pos[0]
