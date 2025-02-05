import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """class handle bullets"""
    def __init__(self,av_settings,screen,ship):
        """creat a bullet object at the top of the ship"""
        super(Bullet,self).__init__()
        self.screen=screen
        #creat a bullet at (0,0) 
        # set it to the new postion#
        self.rect=pygame.Rect(0,0,av_settings.bullet_widith,av_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        # storing bullet postion at decimal value
        self.y=float(self.rect.y)
        self.colour=av_settings.bullet_colour
        self.speed_factor=av_settings.bullet_speed_factor
     
    def update(self):
        """update the bullet position"""
        self.y-=self.speed_factor
        self.rect.y=self.y
    def draw_bullet(self):
        # but this related to pygame class rect which i wish to understand some day ?
        # i don't understend it still
        pygame.draw.rect(self.screen,self.colour,self.rect)