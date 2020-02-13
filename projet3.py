import pygame
import random
from config import *
from mapp.labyrinthe import Labyrinthe

class Game(object):

    def __init__(self):
        self.game = Labyrinthe(GAME_MAP)
        self.init_pygame_elements()
        self.game_status = ""

    def init_pygame_elements(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Labyrinthe de l'enfer")
        self.tempon = pygame.image.load(IMG_WALL)
        self.wall = self.tempon.subsurface((40, 40, 40, 40))
        self.init_pygame_items()
        self.init_pygame_characters()
    
    def init_pygame_items(self):
        self.item1 = pygame.image.load(IMG_ITEM1)
        self.item2 = pygame.image.load(IMG_ITEM2)
        self.item3 = pygame.image.load(IMG_ITEM3)
    
    def init_pygame_characters(self):
        self.gardien = pygame.image.load(IMG_GARDIEN)
        self.hero = pygame.image.load(IMG_HERO)

    def init_pygame_menu(self):
        self.font = pygame.font.SysFont("abyssinicasil", 50)
        self.font1 = pygame.font.SysFont("abyssinicasil", 20)
        self.text = self.font.render("Jeu Du Labyrinthe", True, (255, 255, 255))
        self.text1 = self.font1.render("Enter pour commencer un partie", True, (255, 255, 255))
        self.win = self.font.render("YOU WIN !!!", True, (0, 255, 0))
        self.loose = self.font.render("YOU LOOSE...", True, (255, 0, 0))


    def print_menu(self):
        self.init_pygame_menu()
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text, (90, 50))
        self.screen.blit(self.text1, (150, 200))
        if self.game_status == "WIN":
            self.screen.blit(self.win, (90, 400))
        elif self.game_status == "LOOSE":
            self.screen.blit(self.loose, (90, 400))
        pygame.display.flip()

    def print_screen(self):
        self.screen.fill((0, 0, 0))
        for key, value in self.game.ref.items():
            if value == HERO:
                self.screen.blit(self.hero, key)
            elif value == GARDIEN:
                self.screen.blit(self.gardien, key)
            elif value == WALL:
                self.screen.blit(self.wall, key)
            elif value == ITEM1:
                self.screen.blit(self.item1, self.game.item1.pos)
            elif value == ITEM2:
                self.screen.blit(self.item2, self.game.item2.pos)
            elif value == ITEM3:
                self.screen.blit(self.item3, self.game.item3.pos)
        pygame.display.flip()

    def new_round(self):
        self.game = Labyrinthe(GAME_MAP)
    
    def main_loop(self):
        running = True
        while running:          
            self.print_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.game_status = "play"
                        while self.game_status == "play":
                            self.print_screen()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    running = False
                                elif event.type == pygame.KEYDOWN:
                                    self.game_status = self.game.move(event.key)
                    self.new_round()

if __name__ == '__main__':

    launcher = Game()
    launcher.main_loop()
