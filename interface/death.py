#made by quin smith (ludesdecay)
#started 2026-10-9
#finished 2026-10-29
#space invaders game over file

import pygame,sys
import manager
import objects.image
import objects.buttons
import objects.grid as grid
import objects.text_files as text_files
import objects.label as label

def output(window: pygame.Surface):
    pygame.display.set_caption("game over")
    font=pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 50)

    if manager.playermode == 1 and manager.currentscore >= manager.onephigh:
        manager.onephigh = manager.currentscore
        with open("assets/savedata/singlehigh.txt", 'w') as f:
            f.write(f"{manager.currentscore}")
    if manager.playermode == 2 and manager.currentscore >= manager.twophigh:
        manager.twophigh = manager.currentscore
        with open("assets/savedata/multighigh.txt", 'w') as f:
            f.write(f"{manager.currentscore}")
    if manager.playermode == 1:
        lbl_highscore = objects.label.label(150, 325, 500,
        40, download_font_name="assets/fonts/PixelifySans-Regular.ttf", 
        font_size=28,text_color=(235, 64, 52), text="solo highscore: " +str(manager.onephigh))
    if manager.playermode == 2:
        lbl_highscore = objects.label.label(150, 325, 500,
        40, download_font_name="assets/fonts/PixelifySans-Regular.ttf",
        font_size=28,text_color=(235, 64, 52),  text="co-op highscore: " +str(manager.twophigh))

    lbl_score = objects.label.label(150, 425, 220,
    40, download_font_name="assets/fonts/PixelifySans-Regular.ttf",
    font_size=28,text_color=(235, 64, 52), text="score: " +str(manager.currentscore))
    

    btn_retry = objects.buttons.no_background(
        125, 100, download_font_name="assets/fonts/PixelifySans-Regular.ttf", font_size=20,
        text_color=(235, 64, 52),
        hover_color=(98, 52, 235),
        text="Play Again"
        )
    btn_menu = objects.buttons.no_background(
        250, 100, download_font_name="assets/fonts/PixelifySans-Regular.ttf", font_size=20,
        text_color=(235, 64, 52),
        hover_color=(98, 52, 235),
        text="Exit to Menu"
        )
    btn_exit = objects.buttons.no_background(
        400, 100, download_font_name="assets/fonts/PixelifySans-Regular.ttf", font_size=20,
        text_color=(235, 64, 52),
        hover_color=(98, 52, 235),
        text="Close"
        )

    score_group = pygame.sprite.Group(lbl_highscore, lbl_score)
    buttons_group = pygame.sprite.Group(btn_retry, btn_menu, btn_exit)
    def display():
        window.fill((1, 1, 1))
        buttons_group.draw(window)
        score_group.draw(window)
        window.blit(font.render("Game Over!", True, (235, 64, 52)), (115, 25))
        

    done = False
    while not done:
        display()
        if manager.playermode == 1 and manager.currentscore >= manager.onephigh:
                with open("assets/savedata/singlehigh.txt", 'w') as f:
                    f.write(f"{manager.currentscore}")
        if manager.playermode == 2 and manager.currentscore >= manager.twophigh:
                with open("assets/savedata/multighigh.txt", 'w') as f:
                    f.write(f"{manager.currentscore}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if btn_retry.update(pygame.mouse.get_pos(), event):
                manager.level = 2
                done = True
            if btn_menu.update(pygame.mouse.get_pos(), event):
                manager.playermode = ""
                manager.level = 0
                done = True
            if btn_exit.update(pygame.mouse.get_pos(), event):
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        manager.fpsClock.tick(manager.fps)