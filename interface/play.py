#made by quin smith (ludesdecay)
#started 2026-10-9
#finished 2026-//-//
#space invaders player choice file
import pygame,sys
import manager
import objects.buttons
import objects.grid as grid

def output(window: pygame.Surface):
    pygame.display.set_caption("menu")
    font=pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 50)
    with open("assets/savedata/singlehigh.txt", "r") as f:
        cont = f.read().strip()
        manager.onephigh = int(cont)
    with open("assets/savedata/multihigh.txt", "r") as f:
        cont = f.read().strip()
        manager.twophigh = int(cont)
        
    print(manager.onephigh)
    print(manager.twophigh)
    btn_1p = objects.buttons.no_background(
        225, 100, download_font_name="assets/fonts/PixelifySans-Regular.ttf", font_size=20,
        text_color=(235, 64, 52),
        hover_color=(98, 52, 235),
        text="Singleplayer"
        )
    btn_2p = objects.buttons.no_background(
        225, 300, download_font_name="assets/fonts/PixelifySans-Regular.ttf", font_size=20,
        text_color=(235, 64, 52),
        hover_color=(98, 52, 235),
        text="Co-op"
        )

    buttons_group = pygame.sprite.Group(btn_1p,btn_2p)
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
            if btn_1p.update(pygame.mouse.get_pos(), event):
                manager.playermode = 1
                manager.level = 2
                done = True
            if btn_2p.update(pygame.mouse.get_pos(), event):
                manager.playermode = 2
                manager.level = 2
                done = True
        pygame.display.flip()
        manager.fpsClock.tick(manager.fps)