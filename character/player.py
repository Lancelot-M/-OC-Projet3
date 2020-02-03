"""Classe gerant le joueur et ses intentions."""
from position.position import Position

class Player(Position):

    def __init__(self, dico):
        self.image = "M"
        self.pos = Position.pos(dico, self.image)
        self.coord = self.pos[0]
        self.inventory = "empty"

    def way(self, way):

        x = self.coord[0]
        y = self.coord[1]
        if way == ('q' or 'Q'):
            return (x - 1, y)
        elif way == ('z' or 'Z'):
            return (x, y - 1)
        elif way == ('s' or 'S'):
            return (x, y + 1)
        elif way == ('d' or 'D'):
            return (x + 1, y)
        else:
            exit()
