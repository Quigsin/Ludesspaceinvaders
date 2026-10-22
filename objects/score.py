#made by Quin smith (ludesdecay)
#2026-10-14

import pygame
import objects.labels as label
import manager

class score(label):
    def __init__(self, ):
        super().__init__()
        self.score = manager.currentscore
        if manager.playermode == 1:
            self.highscore = manager.onephigh
        elif manager.playermode == 2:
            self.highscore = manager.twophigh
