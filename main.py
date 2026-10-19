#made by quin smith (ludesdecay)
#started 2026-10-9
#finished 2026-//-//
#space invaders main.py file
import pygame,sys
import interface.menu
import interface.play
import interface.game
import interface.death
import manager
pygame.init()



window = pygame.display.set_mode((manager.WINDOW_WIDTH, manager.WINDOW_HEIGHT), pygame.HWSURFACE)

while True:
    if manager.level == 0:
        interface.menu.output(window)
    elif manager.level == 1:
        interface.play.output(window)
    elif manager.level == 2:
        interface.game.output(window)
    elif manager.level == 3:
        interface.death.output(window)