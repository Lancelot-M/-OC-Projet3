"""File representing the hard parts of the card"""

from position.position import Position


class Structure(Position):

    """Class representing non-movable elements (walls / paths)."""
    def __init__(self, map_ref, image=""):
        self.pos = Position.pos(map_ref, image)
