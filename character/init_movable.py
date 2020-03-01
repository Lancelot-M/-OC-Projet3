"""File grouping moving objects."""

from character.ennemy import Ennemy
from character.player import Player
from character.item import Items
from config import ITEM1, ITEM2, ITEM3


class Movable(object):

    """Initialization class"""
    def __init__(self, map_ref):
        self.item1 = Items(map_ref, ITEM1)
        self.item2 = Items(map_ref, ITEM2)
        self.item3 = Items(map_ref, ITEM3)
        self.player = Player(map_ref)
        self.gardien = Ennemy(map_ref)
