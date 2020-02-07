import pygame
from config import *
from mapp.labyrinthe import Labyrinthe

class Game(object):

    def __init__(self):
        self.game = Labyrinthe(GAME_MAP)
    
    def play(self):
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Labyrinthe de l'enfer")
        tempon = pygame.image.load(IMG_WALL)
        wall = tempon.subsurface((40, 40, 40, 40))
        gardien = pygame.image.load(IMG_GARDIEN)
        hero = pygame.image.load(IMG_HERO)
        item1 = pygame.image.load(IMG_ITEM1)
        running = True
        while running:          
            screen.fill((0, 0, 0))
            for key, value in self.game.ref.items():
                if value == HERO:
                    screen.blit(hero, key)
                elif value == GARDIEN:
                    screen.blit(gardien, key)
                elif value == WALL:
                    screen.blit(wall, key)
                elif value == ITEM1:
                    screen.blit(item1, key)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.game.move(event.key)

if __name__ == '__main__':

    luncher = Game()
    luncher.play()
