"""File containing the menu display."""

import pygame


class Menu(object):
    """Initialization class."""

    def __init__(self):
        self.font = pygame.font.SysFont("abyssinicasil", 50)
        self.font1 = pygame.font.SysFont("abyssinicasil", 20)
        self.text = self.font.render("Jeu Du Labyrinthe",
                                     True, (255, 255, 255))
        self.text1 = self.font1.render("Enter pour commencer un partie",
                                       True, (255, 255, 255))
        self.win = self.font.render("YOU WIN !!!", True, (0, 255, 0))
        self.loose = self.font.render("YOU LOOSE...", True, (255, 0, 0))
