import pygame
file_path="ship.bmp"
class Ship():
   def __init__(self,av_setting,screen):
      """Initialize the ship and set its starting position."""
      self.screen = screen
 # Load the ship image and get its rect.
      self.image = pygame.image.load(file_path)
      self.image=pygame.transform.scale(self.image,(50,50))
      self.rect = self.image.get_rect()
      self.screen_rect = screen.get_rect()
      self.av_setting=av_setting
 # Start each new ship at the bottom center of the screen.
      self.rect.centerx = self.screen_rect.centerx
      self.rect.bottom = self.screen_rect.bottom
#store a deciml value for the ship center
      self.center=float(self.rect.centerx)
#the movment flag of the ship
      self.moving_right=False
      self.moving_left=False
   def update_postion(self):
      if self.moving_right and self.rect.right<self.screen_rect.right:
         self.center+=self.av_setting.ship_speed_factor
      if self.moving_left and self.rect.left>0:
         self.center-=self.av_setting.ship_speed_factor
      self.rect.centerx=self.center


   def blitme(self):
     """Draw the ship at its current location."""
     self.screen.blit(self.image, self.rect)