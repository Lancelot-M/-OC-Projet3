#! /usr/bin/python3.6

#---------------------------------------------------------------------------------

class Labyrinthe:
    """ Classe représantant les murs du labyrinthe."""

    def __init__(self, image, position):
        self.image = image
        self.pos = position

    def show_wall(self):
        for i in self.pos:
                display_surface.blit(self.image, (i[0] * 40, i[1] * 40))


class Joueur:
    """Classe représentant le héro incarné par le joueur."""

    def __init__(self, image, position):
        self.image = image
        self.pos = position
        self.inventaire = EMPTY

    def move(self):
        key = pygame.key.getpressed()
        if key[pygame.K_LEFT]:
            if self.pos[0] - 1 != laby.pos:
                self.pos = self.pos[0] - 1
        if key[pygame.K_DOWN]:
            if self.pos[1] + 1 != laby.pos:
                self.pos = self.pos[1] + 1
        if key[pygame.K_RIGHT]:
            if self.pos[0] + 1 != laby.pos:
                self.pos = self.pos[0] + 1
        if key[pygame.K_UP]:
            if self.pos[1] - 1 != laby.pos:
                self.pos = self.pos[1] - 1

class Ennemy:
    """Bad Guys"""
    
    def __init__(self, image, position):
        self.image = image
        self.pos = position

class Objet:
    """Objets pouvant être ramassé."""

    def __init__(self, image, position):
        self.image = image
        self.pos = position

# ----------------------------------------------------------------------------------------

import pygame
pygame.init()

display_surface = pygame.display.set_mode((600, 600))

white = (255, 255, 255)
image_wall = pygame.image.load("./ressources/floor-tiles-20x20.png")
image_swall = wall_image.subsurface((40,40,40,40))
image_hero = pygame.image.load("./ressources/MacGyver.png")
image_badguy = pygame.image.load("./ressources/Gardien.png")
image_seringue = pygame.image.load("./ressources/seringue40*40.png")

position_wall = [
        [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],
        [14,1],
        [0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[9,2],[10,2],[11,2],[12,2],[14,2],
        [0,3],[14,3],
        [0,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[9,4],[10,4],[11,4],[12,4],[13,4],[14,4],
        [0,5],[14,5],
        [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[8,6],[9,6],[10,6],[12,6],[14,6],
        [0,7],[10,7],[12,7],[14,7],
        [0,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8],[8,8],[9,8],[10,8],[12,8],[14,8],
        [0,9],[2,9],[12,9],[14,9],
        [0,10],[2,10],[4,10],[5,10],[6,10],[7,10],[8,10],[9,10],[10,10],[11,10],[12,10],[14,10],
        [0,11],[2,11],[4,11],[14,11],
        [0,12],[2,12],[4,12],[5,12],[6,12],[7,12],[8,12],[9,12],[10,12],[11,12],[12,12],[13,12],[14,12],
        [0,13],
        [0,14],[1,14],[2,14],[3,14],[4,14],[5,14],[6,14],[7,14],[8,14],[9,14],[10,14],[11,14],[12,14],[13,14],[14,14]]
position_hero = [14,14]
position_badguy = [0,0]
position_seringue = [9,7]

laby = Labyrinthe(image_swall, position_wall)
hero = Joueur(image_hero, position_hero)
badguy = Ennemy(image_badguy, position_badguy)
seringue = Objet(image_seringue, position_seringue)
#sprites = pygame.group

display_surface.fill(white)
display_surface.blits(sprites)
