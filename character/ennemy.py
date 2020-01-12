from position.position import *

class Ennemy(Position):

    def __init__(self, dico):
        self.image = "G"
        self.pos = Position.pos(dico, self.image)
