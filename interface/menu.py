#made by quin smith (ludesdecay)
#started 2026-10-9
#finished 2026-//-//
#space invaders main menu file
import pygame,sys
import manager
import objects.image
import objects.buttons
import objects.grid as grid

def output(window: pygame.Surface):
    pygame.display.set_caption("menu")
    font=pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 50)
    
    btn_play = objects.buttons.no_background(
        10, 100, download_font_name="assets/fonts/PixelifySans-Regular.ttf", font_size=20,
        text_color=(235, 64, 52),
        hover_color=(98, 52, 235),
        text="Play"
        )

    buttons_group = pygame.sprite.Group(btn_play)
    def display():
        window.fill((1, 1, 1))
        buttons_group.draw(window)
        window.blit(font.render("Space Invaders", True, (235, 64, 52)), (115, 25))
        grid.gridHelp(window,manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT)


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