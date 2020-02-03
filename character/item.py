from position.position import Position

class Items(Position):

    def __init__(self, dico):
        self.image = "O"
        self.pos = Position.pos(dico, self.image)
