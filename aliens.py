import pygame
from pygame.sprite import Sprite
class Aliens(Sprite):
    """a class representing a single alien"""
    def __init__(self,av_setting,screen):
        """initalize and set position"""
        super(Aliens,self).__init__()
        self.screen=screen
        self.av_setting=av_setting
        # load and get it's rect value
        self.image=pygame.image.load("alien.bmp")
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()
        # set the postion to the top right of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        # store the postion of x as floating point
        self.x=float(self.rect.x)
    def check_edge(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>screen_rect.right:
            return True
        elif self.rect.left<0:
            return True
        else:
            return False
    def update(self):
        """update the postion"""
        self.x+=(self.av_setting.alien_speed_factor*self.av_setting.moving_direction)
        self.rect.x=self.x
    def change_direction(self,aliens):
      for alien in aliens:
          alien.rect.y+=self.av_setting.drop_speed
      self.av_setting.moving_direction*=-1
    
    def blitme(self):
        """draw alien at it's CURRENT location"""
        self.screen.blit(self.image,self.rect) 