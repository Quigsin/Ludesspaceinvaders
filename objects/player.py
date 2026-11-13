
#2026-10-5
#modified 2026-10-9 for space invaders
#player object file

import pygame
import objects.image as image
import objects.lasers as laser

class player(image.still):
    def __init__(self, x, y, width, height, image_to_use, speed, lives, cooldown):
        super().__init__(x, y, width, height, image_to_use)
        self.speed = speed
        self.lives = lives
        self.last_shot = 0
        self.cooldown = cooldown
    def move(self, key_right, key_left):
        key_input = pygame.key.get_pressed() 
        self.movex = (key_input[key_left] * -self.speed) + (key_input[key_right] * self.speed)
        self.rect.x += self.movex
    def movebackx(self, value):
        self.rect.x = value
    def movebacky(self, value):
        self.rect.y = value
    def coldamage(self, other, damage, otherlist):
        if pygame.sprite.collide_mask(self, other):
        #if self.rect.colliderect(other):
            self.lives -= damage
            otherlist.remove(other)

    def fire(self, key):
        current_time = pygame.time.get_ticks()
        key_input = pygame.key.get_pressed()
        if current_time - self.last_shot >= self.cooldown and key_input[key] == True:
            self.last_shot = current_time
            return laser.laser(self.rect.x+15,self.rect.y-50,25,50,"assets/images/f-laser.png",15)
        
        return None
