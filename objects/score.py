#made by Quin smith (ludesdecay)
#2026-10-14

import pygame
import objects.label as label
import manager
import objects.text_files as text_files

class score(label):
    def __init__(self,start_x,start_y,width,height):
        super().__init__(start_x,start_y,width,height,font_name=None,font_size=24,text_color=(0,0,0),back_color=(0,0,0,0),text="",text_offset=(5,5),border_colour=(0,0,0),download_font_name=None,show_border=True)

    def updatehigh(self):
        if manager.playermode == 1:
            manager.onephigh = max(manager.onephigh, manager.currentscore)
        if manager.playermode == 2:
            manager.twophigh = max(manager.onephigh, manager.currentscore)
    def updatescore(self):
        self.text=(str(manager.currentscore))

    def writehigh(self):
        if manager.playermode == 1:
            with open("assets/savedata/singlehigh", 'w') as f:
                f.write(f"{manager.onephigh}\n")
        if manager.playermode == 2:
            with open("assets/savedata/singlehigh", 'w') as f:
                f.write(f"{manager.twophigh}")


