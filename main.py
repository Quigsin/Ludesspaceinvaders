#made by quin smith (ludesdecay)
#started 2026-10-9
#finished 2026-//-//
#space invaders main.py file
import pygame,sys
import interface.menu
import interface.game
import interface.death
import manager
pygame.init()

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 600

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE)

while True:
    if manager.level == 0:
        interface.menu.output(window)
    elif manager.level == 1:
        interface.play.output(window)
    elif manager.level == 2:
        interface.death.output(window)