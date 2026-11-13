#made by quin smith (ludesdecay)
#started 2026-10-9
#finished 2026-10-29
#space invaders gameplay file
import pygame,sys
import manager
import objects.player
import objects.image
import objects.grid as grid
import objects.enemy as enemy
import objects.lasers as laser
import objects.label
import random

def output(window: pygame.Surface):
    #different based on player mode selected in previous screen
    def spawnenemies():
        
        return [enemy.enemy(125+i *50, 0 + j *50, 50, 50, "assets/images/alien.png", 10, 1, 25) for i in range(9) for j in range(7)]
    aliens = spawnenemies()
    if manager.playermode == 1:
        player1 = objects.player.player(275, 950, 50, 50, "assets/images/player.png", 3, 3, 1200)
    
    elif manager.playermode == 2:
        player1 = objects.player.player(250, 950, 50, 50, "assets/images/player.png", 3, 3, 1500)
        player2 = objects.player.player(300, 950, 50, 50, "assets/images/player2.png", 3, 3, 1500)

    lbl_lives = objects.label.label(10, 10, 500,
            55, download_font_name="assets/fonts/PixelifySans-Regular.ttf", 
            font_size=25,text_color=(235, 64, 52), text="lives: "+str(player1.lives), show_border=False)
    
    lastshot = pygame.time.get_ticks()
    shotdelay = 2000
    
    fired = pygame.sprite.Group()
    efired = pygame.sprite.Group()
    
    labels = pygame.sprite.Group(lbl_lives)

    pygame.display.set_caption("score: "+str(manager.currentscore) +"lives: " +str(player1.lives))
    def display():
        window.fill((255,255,255))
        player1.draw(window)
        
        for i in aliens:
            i.draw(window)
        if manager.playermode == 2:
            player2.draw(window)
        
        for i in fired:
            i.move()
            i.draw(window)
            i.lifetime()
        for i in efired:
            i.move()
            i.draw(window)
            i.lifetime()
        labels.draw(window)
        
        pygame.display.set_caption("score: "+str(manager.currentscore) +"| lives: " +str(player1.lives))


    done = False

    while not done:
        display()
        # playermovement
        p1prevx = player1.rect.x
        player1.move(pygame.K_d, pygame.K_a)
        if player1.rect.x <= 0 or player1.rect.x >=550:
            player1.movebackx(p1prevx)
        
        if manager.playermode == 2:
            p2prevx = player2.rect.x
            player2.move(pygame.K_RIGHT, pygame.K_LEFT)
            if player2.rect.x <= 0 or player2.rect.x >=550:
                player2.movebackx(p2prevx)
        # playermovement

        #player laser firing
        laserfired = player1.fire(pygame.K_w)
        if laserfired is not None:
            fired.add(laserfired)
        if manager.playermode == 2:
            laserfired2 = player2.fire(pygame.K_UP)
            if laserfired2 is not None:
                fired.add(laserfired2)
        #player laser firing
        #damage and killing
            #laser damage
        for i in fired:
            for j in aliens:
                i.collision(aliens, j, j.value)
        for i in efired:
            player1.coldamage(i, 1, efired)
            if manager.playermode == 2:
                player2.coldamage(i,1,efired)
        for i in fired:
            for j in efired:
                i.collision(efired, j, 10)
            
            #laser damage
            #player collision damage
        for i in aliens:
            player1.coldamage(i, 1, aliens)
            if manager.playermode == 2:
                player2.coldamage(i, 1, aliens)
            #player collision damage
        #enemy firing
        ct = pygame.time.get_ticks()
        if aliens and ct - lastshot >= shotdelay:
            firer = random.choice(aliens)
            efired.add(firer.firing())
            lastshot = ct
        #enemy firing
        if manager.playermode == 2:
            player1.lives= min(player1.lives,player2.lives)
            player2.lives= min(player1.lives,player2.lives)
        


        # alien movement
        for i in aliens:
            i.moverl()
        if any(a.rect.right >= 600 or a.rect.left <= 0 for a in aliens):
            for a in aliens:
                a.xspeed *= -1
                a.movedown()
        #alien movement
        #alien laser firing

        #alien laser firing

        #alien respawning
        if len(aliens) == 0:
            aliens.extend(spawnenemies())
        
        #alien respawning

        if player1.lives == 0:
            done = True
            manager.level = 3
        if manager.playermode == 2 and player2.lives == 0:
            done = True
            manager.level = 3

        lbl_lives.set_text("lives: "+ str(player1.lives))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
                manager.level = 3

            
        pygame.display.flip()
        manager.fpsClock.tick(manager.fps)