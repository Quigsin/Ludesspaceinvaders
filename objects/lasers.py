#made by Quin smith (ludesdecay)
import pygame
import objects.image as image
import manager

class laser(image.still):
    def __init__(self, x, y, width, height, image_to_use, speed):
        super().__init__(x, y, width, height, image_to_use)
        self.speed = speed
    def collision(self, other1, other2, other3):
        if self.rect.colliderect(other2):
            self.kill()
            other2.kill()
            other1.remove(other2)
            manager.currentscore += other3
            
    def move(self):
        self.rect.y -= self.speed
    def damage(self, other):
        if self.rect.colliderect(other):
            self.kill()
            return True
        
    def lifetime(self):
        if self.rect.y < 0 or self.rect.y > 1000:
            self.kill()
    