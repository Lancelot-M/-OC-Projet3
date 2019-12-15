class Wall(Position):

    def __init__(self, map_ref):
        self.image = "X"
        self.pos = Position.pos(map_ref)
