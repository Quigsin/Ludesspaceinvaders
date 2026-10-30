#made by Quin smith (ludesdecay)


import pygame
import manager
import objects.image as image

class shield(image.still):
    def __init__(self, x, y, width, height, image_to_use, health):
        super().__init__(x, y, width, height, image_to_use)
        self.health = health
        
    def block(self, other, damage, otherlist):
        if self.rect.colliderect(other):
            self.health -= damage
            otherlist.remove(other)