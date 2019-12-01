#! /usr/bin/python3.6

import pygame

pygame.init()

display_surface = pygame.display.set_mode((600, 600))

image = pygame.image.load("./ressources/floor-tiles-20x20.png")
seringue_image = pygame.image.load("./ressources/seringue40*40.png")
boudimage = image.subsurface((40, 40, 40, 40))
position = [
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

class Labyrinthe:
    """ Classe représantant les murs du labyrinthe."""

    def __init__(self, image, position):
        self.image = image
        self.pos = position

    def show_wall(self):
        for i in self.pos:
                display_surface.blit(self.image, (i[0] * 40, i[1] * 40))

laby = Labyrinthe(boudimage, position)

class Joueur:
    """Classe représentant le héro incarné par le joueur."""

    def __init__(self, image):
        self.image = image
        self.pos = position_hero
        self.inventaire = EMPTY

#   def move(self):
#       en fonction des touches du clavier impulsion
#       check la direction de l'impulsion
#       action en fn du retour

    

while True:

    laby.show_wall()
    display_surface.blit(seringue_image, (9 * 40, 7 * 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()

