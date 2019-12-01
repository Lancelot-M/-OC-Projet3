#! /usr/bin/python3.6

import pygame

pygame.init()

white = (255, 255, 250)

display_surface = pygame.display.set_mode((750, 750))

pygame.display.set_caption('SuperMAC')

image = pygame.image.load(r'./ressources/MacGyver.png')

while True:

    display_surface.fill(white)
    display_surface.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()       
