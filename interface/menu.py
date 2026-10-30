#made by quin smith (ludesdecay)
#started 2026-10-9
#finished 2026-10-29
#space invaders main menu file
import pygame,sys
import manager
import objects.image
import objects.buttons
import objects.grid as grid

def output(window: pygame.Surface):
    pygame.display.set_caption("menu")
    font=pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 50)

    
    lbl_highscore1 = objects.label.label(150, 250, 500,
        40, download_font_name="assets/fonts/PixelifySans-Regular.ttf", 
        font_size=28,text_color=(235, 64, 52), text="solo highscore: " +str(manager.onephigh))
    
    lbl_highscore2 = objects.label.label(150, 325, 500,
        40, download_font_name="assets/fonts/PixelifySans-Regular.ttf",
        font_size=28,text_color=(235, 64, 52),  text="co-op highscore: " +str(manager.twophigh))

    lbl_instructions = objects.label.label(90, 80, 500, 500, download_font_name="assets/fonts/PixelifySans-Regular.ttf",
        font_size=20, text_color=(235,64,52), text="You are the last defender of humanity,\nYou have to fight off as many aliens as possible,\nto save the people below from endless torture.\nthe aliens are endless, but thats okay.\nYou have accepted that you will fight for the rest of your life." )
    
    btn_play = objects.buttons.no_background(
        260, 400, download_font_name="assets/fonts/PixelifySans-Regular.ttf", font_size=20,
        text_color=(235, 64, 52),
        hover_color=(98, 52, 235),
        text="Play"
        )
    label_group = pygame.sprite.Group(lbl_highscore1, lbl_highscore2,lbl_instructions)
    buttons_group = pygame.sprite.Group(btn_play)
    def display():
        window.fill((1, 1, 1))
        buttons_group.draw(window)
        label_group.draw(window)
        window.blit(font.render("Space Invaders", True, (235, 64, 52)), (115, 25))
        


    done = False
    while not done:
        display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if btn_play.update(pygame.mouse.get_pos(), event):
                manager.level = 1
                done = True
        pygame.display.flip()
        manager.fpsClock.tick(manager.fps)