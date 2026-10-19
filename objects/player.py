
#2026-10-5
#modified 2026-10-9 for space invaders
#player object file

import pygame
import objects.image as image

class player(image.still):
    def __init__(self, x, y, width, height, image_to_use, speed, lives):
        super().__init__(x, y, width, height, image_to_use)
        self.speed = speed
        self.lives = lives
    def move(self, key_right, key_left):
        key_input = pygame.key.get_pressed() 
        self.movex = (key_input[key_left] * -self.speed) + (key_input[key_right] * self.speed)
        self.rect.x += self.movex
    def movebackx(self, value):
        self.rect.x = value
    def movebacky(self, value):
        self.rect.y = value
    def collision(self, other):
        if self.rect.colliderect(other):
            return True
    def damage(self, lives):
        self.lives -= lives