"""File containing the labyrinth display."""

import pygame
from config import IMG_WALL


class Screen(object):
    """Initialization class."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Labyrinthe de l'enfer")
        tempon = pygame.image.load(IMG_WALL)
        self.wall = tempon.subsurface((40, 40, 40, 40))
