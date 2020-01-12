from position.position import *

class Player(Position):

    def __init__(self, dico):
        self.image = "M"
        self.pos = Position.pos(dico, self.image)
        self.inventory = "empty"

    def way(self, way):
        if way == ('q' or 'Q'):
            return (self.pos[0] - 1)
        elif way == ('z' or 'Z'):
            return (self.pos[0] - 16)
        elif way == ('s' or 'S'):
            return (self.pos[0] + 16)
        elif way == ('d' or 'D'):
            return (self.pos[0] + 1)
        else:
            exit()
