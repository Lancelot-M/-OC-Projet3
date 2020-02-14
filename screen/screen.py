"""Fichier contenant l'affichage du labyrinthe."""

import pygame
from config import IMG_WALL

class Screen(object):
    """Classe d'initialisation."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Labyrinthe de l'enfer")
        tempon = pygame.image.load(IMG_WALL)
        self.wall = tempon.subsurface((40, 40, 40, 40))

