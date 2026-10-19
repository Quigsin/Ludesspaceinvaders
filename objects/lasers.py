#made by Quin smith (ludesdecay)
import pygame
import objects.image as image

class laser(image.still):
    def __init__(self, x, y, width, height, image_to_use, speed):
        super().__init__(x, y, width, height, image_to_use)
        self.speed = speed
    def collision(self, other):
        if self.rect.colliderect(other):
            self.kill()
            other.kill()
    def move(self):
        self.rect.y -= self.speed
    def damage(self, other):
        if self.rect.colliderect(other):
            self.kill()
            return True
    def lifetime(self):
        if self.rect.y < 0:
            self.kill()
    