#made by Quin smith (ludesdecay)
#2026-10-14
import pygame
import objects.image as image

class enemy(image.still):
    def __init__(self, x, y, width, height, image_to_use, speed, xspeed):
        super().__init__(x, y, width, height, image_to_use)
        self.speed = speed
        self.xspeed = xspeed
    def movedown(self):
        self.rect.y += self.speed
    def moverl(self):
        self.rect.x += self.xspeed
    def frame(self, image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height)).convert_alpha()