"""File containing display elements of the labyrinth."""

import pygame
from config import IMG_GARDIEN, IMG_HERO, IMG_ITEM1, IMG_ITEM2, IMG_ITEM3


class Character(object):
    """Initialization class."""

    def __init__(self):
        self.gardien = pygame.image.load(IMG_GARDIEN)
        self.hero = pygame.image.load(IMG_HERO)
        self.item1 = pygame.image.load(IMG_ITEM1)
        self.item2 = pygame.image.load(IMG_ITEM2)
        self.item3 = pygame.image.load(IMG_ITEM3)
