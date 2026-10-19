#made by quin smith (ludesdecay)
#started 2026-10-9
#finished 2026-//-//
#space invaders gameplay file
import pygame,sys
import manager
import objects.player
import objects.image
import objects.grid as grid
import objects.enemy as enemy

def output(window: pygame.Surface):
    #different based on player mode selected in previous screen
    aliens = [enemy.enemy(125+i *50, 0 + j *50, 50, 50, "assets/images/player.png", 1, 1) for i in range(7) for j in range(5)]
    if manager.playermode == 1:
        player1 = objects.player.player(275, 950, 50, 50, "assets/images/player.png", 3, 3)

    elif manager.playermode == 2:
        player1 = objects.player.player(250, 950, 50, 50, "assets/images/player.png", 3, 3)
        player2 = objects.player.player(300, 950, 50, 50, "assets/images/player2.png", 3, 3)
    
    pygame.display.set_caption("menu")
    def display():
        window.fill((1,1,1))
        player1.draw(window)
        for i in aliens:
            i.draw(window)
        if manager.playermode == 2:
            player2.draw(window)
        grid.gridHelp(window,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT)
        
    done = False

    while not done:
        display()
        player1.move(pygame.K_d, pygame.K_a)
        if manager.playermode == 2:
            player2.move(pygame.K_RIGHT, pygame.K_LEFT)
        for i in aliens:
            i.moverl()
        
        if any(a.rect.right >= 600 or a.rect.left <= 0 for a in aliens):
            for a in aliens:
                a.xspeed *= -1





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        manager.fpsClock.tick(manager.fps)