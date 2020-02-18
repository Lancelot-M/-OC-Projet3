""" File containing the main fonction."""

import pygame
from config import GAME_MAP, GARDIEN, ITEM1, ITEM2, ITEM3, HERO, WALL
from mapp.labyrinthe import Labyrinthe
from screen.screen import Screen
from screen.characters import Character
from screen.menu import Menu

class Game(object):
    """ Class representative of the game. Interaction pygame and labyrinthe."""

    def __init__(self):
        self.game = Labyrinthe(GAME_MAP)
        self.screen = Screen()
        self.menu = Menu()
        self.character = Character()
        self.game_status = ""

    def print_menu(self):
        """Function to display menu."""
        self.screen.screen.fill((0, 0, 0))
        self.screen.screen.blit(self.menu.text, (90, 50))
        self.screen.screen.blit(self.menu.text1, (150, 200))
        if self.game_status == "WIN":
            self.screen.screen.blit(self.menu.win, (90, 400))
        elif self.game_status == "LOOSE":
            self.screen.screen.blit(self.menu.loose, (90, 400))
        pygame.display.flip()
    def print_screen(self):
        """Function to display labyrinth."""
        self.screen.screen.fill((0, 0, 0))
        for key, value in self.game.ref.items():
            if value == HERO:
                self.screen.screen.blit(self.character.hero, key)
            elif value == GARDIEN:
                self.screen.screen.blit(self.character.gardien, key)
            elif value == WALL:
                self.screen.screen.blit(self.screen.wall, key)
            elif value == ITEM1:
                self.screen.screen.blit(self.character.item1, self.game.movable.item1.pos)
            elif value == ITEM2:
                self.screen.screen.blit(self.character.item2, self.game.movable.item2.pos)
            elif value == ITEM3:
                self.screen.screen.blit(self.character.item3, self.game.movable.item3.pos)
        pygame.display.flip()
    def new_round(self):
        """Reset labyrinth."""
        self.game = Labyrinthe(GAME_MAP)
    def quit_game(self):
        pygame.quit()
        exit()
    def round_loop(self):
        """Loop display and move in labyrinth."""
        while self.game_status == "play":
            self.print_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit_game()
                    else:
                        self.game_status = self.game.move(event.key)
    def main_loop(self):
        """Main function"""
        running = True
        while running:
            self.print_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.new_round()
                        self.game_status = "play"
                    elif event.key == pygame.K_ESCAPE:
                        self.quit_game()
            if self.game_status == "play":
                self.round_loop()

if __name__ == '__main__':

    def launcher():
        """Function to start the game."""
        game = Game()
        game.main_loop()

    launcher()
